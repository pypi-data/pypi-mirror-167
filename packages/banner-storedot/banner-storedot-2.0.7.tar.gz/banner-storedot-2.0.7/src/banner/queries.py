from re import split
from typing import Union, Dict
from numbers import Number
from threading import Thread
from functools import wraps, partial
from collections.abc import Iterable
from collections import ChainMap
from datetime import datetime

import MySQLdb as mysql
from MySQLdb.cursors import DictCursor
from MySQLdb._exceptions import OperationalError, ProgrammingError
import pandas as pd
import numpy as np
from joblib import Parallel, delayed

from banner.utils.const import (
    FIRST_NEWARE_DATA_TABLE, SECOND_NEWARE_DATA_TABLE, FIRST_NEWARE_AUX_TABLE, SECOND_NEWARE_AUX_TABLE, 
    NW_TEMP, CACHE_CONNECTION_KWARG, TTL_KWARG, NW_DATA_SIGNIFICANT_COLUMNS, NW_AUX_SIGNIFICANT_COLUMNS,
    NW_AUX_CHANNEL, NW_UNIT, NW_CHANNEL, NW_TEST, NW_CYCLE, NW_SEQ, NW_STEP, NW_STEP_TYPE, NW_TIMESTAMP, 
    NW_VOLTAGE, NW_CURRENT, NW_STEP_RANGE
)
from banner.utils.neware import calculate_neware_columns, calculate_dqdv, merge_cache, query_cache
from banner.utils.web2py import parse_w2p_to_mysql_query, COLUMN_TO_LABEL as W2P_COLUMN_TO_LABEL, LABEL_TO_COLUMN as W2P_LABEL_TO_COLUMN, represent as w2p_repr
from banner.utils.misc import is_non_string_iterable, to_sql_range, key_value_to_string, to_list
from banner.connection import Connection, Storage, RelationalConnection, MySqlConnection

class Queries(object): #TODO Statements
    @staticmethod
    def CONNECTIONS(conns: Dict[str, Connection] = {}):
        ''' 
            Dict of pre existing Connection Objects (name: connection)
            Setup new connections, returns all available
        '''
        try:
            Queries.CONNECTIONS.__CONNECTIONS.update(conns)

        except AttributeError:
            Queries.CONNECTIONS.__CONNECTIONS = {**conns}

        if not Queries.CONNECTIONS.__CONNECTIONS:
            return {None: None}

        return Queries.CONNECTIONS.__CONNECTIONS

    @staticmethod
    def CACHE(con: Storage = None):
        ''' 
            Sets a Storage Connection as default Cache
        '''
        try:
            assert(Queries.CACHE.__CACHE_CONNECTION)

        except (AssertionError, AttributeError):
            Queries.CACHE.__CACHE_CONNECTION = None

        if isinstance(con, Storage):
            Queries.CACHE.__CACHE_CONNECTION = con
        
        return Queries.CACHE.__CACHE_CONNECTION

    @staticmethod
    def __get_known_connection(connection: Union[Connection, str], typ: type = Connection):
        # If no connection is provided, grab first available
        if not connection:
            connections = [
                _connection for _connection in Queries.CONNECTIONS().values() if isinstance(_connection, typ)
            ]

            if not connections:
                raise IndexError('No Connections could be found')

            connection = connections[0]

        # Provided connection is not a Connection, is it a key?
        if not isinstance(connection, Connection):
            connection = Queries.CONNECTIONS().get(str(connection), connection)
        
        # No connection could be found
        if not isinstance(connection, Connection):
            raise KeyError(f'Unknown Connection', connection)

        if not isinstance(connection, typ):
            raise TypeError('Wrong Connection type', connection)

        return connection

    def __cache_query(value, cache: Storage, func: callable, args, ttl, kwargs):
        try:
            assert(isinstance(cache, Storage))
            
            return cache.store(
                value, 
                func, 
                *args,
                ttl=ttl,
                **kwargs
            )

        except AssertionError:
            pass
        
        except Exception as e:
            raise ValueError(f'Failed Caching {value} into {cache}', e)
    
    def __cached_query(cache: Storage, func: callable, *args, **kwargs):
        try:
            assert(isinstance(cache, Storage))
            
            cached = cache.retrieve(
                func, *args, **kwargs
            )
            
            return cached

        except AssertionError:
            return pd.DataFrame()

    def __cache(func):
        @wraps(func)
        def inner(*args, **kwargs):
            cache = kwargs.pop(CACHE_CONNECTION_KWARG, None)

            if cache is None: # Specifically checking for None, If False Do not cache!
                cache = Queries.CACHE()
            
            ttl = kwargs.pop(TTL_KWARG, None)

            value = Queries.__cached_query(cache, func, *args, **kwargs)
            
            if not value.empty:
                return value
            
            value = func(*args, **kwargs)
            
            # Cache TODO USE CELERY
            Thread(
                target=Queries.__cache_query, 
                kwargs=dict(
                    value=value.copy(),
                    cache=cache,
                    func=func,
                    args=args,
                    ttl=ttl,
                    kwargs=kwargs
                )
            ).start()
            
            return value
        
        return inner

    @staticmethod
    def __query(query: str, connection=None, cache=None, ttl=None, w2p_parse=True) -> pd.DataFrame:
        if not isinstance(query, str):
            return pd.DataFrame()

        connection = Queries.__get_known_connection(connection)
        
        if w2p_parse:
            query = parse_w2p_to_mysql_query(query)
        #TODO CHANGE TO LABELS?! NEEDS TO KNOW RAW
        return connection.retrieve(query)
    
    @staticmethod
    @__cache
    def simple_query(query: str, connection: Union[Connection, str] = None, cache: Storage = None, ttl: int = None, w2p_parse: bool = True) -> pd.DataFrame:
        '''
            Queries a given Connection/str of a known connection (or first known) return result as DataFrame
            Cache if cache or first known with ttl or default ttl for cache
            Raises KeyError and OperationalError
        '''
        return Queries.__query(
            query, 
            connection=connection, 
            cache=cache, 
            ttl=ttl, 
            w2p_parse=w2p_parse
        )

    @staticmethod
    def simple_edit(query: str, connection: Union[Connection, str] = None):
        '''
            Queries (Edit statements) a given Connection/str of a known connection (or first known)
            
            Raises KeyError and OperationalError
        '''
        connection = Queries.__get_known_connection(connection)
        
        return connection.store(query)

    @staticmethod
    def delete_from(table: str, condition: str, connection: Union[Connection, str] = None):
        '''
            DELETE from table Statement by condition for a given connection
            
            Raises KeyError and OperationalError
        '''
        query = f"""
            DELETE FROM {table}
            WHERE {condition};
        """

        return Queries.simple_edit(query, connection=connection)

    @staticmethod
    def insert_update_into(table: str, **kwargs):
        '''
            INSERT INTO table Statement for a given connection(kwarg)
            If condition(kwarg) is present UPDATE instead
            Raises KeyError and OperationalError
        '''

        connection = kwargs.pop('connection', None)
        condition = kwargs.pop('condition', False)
        
        keys, values = map(str, kwargs.keys()), map(repr, kwargs.values())
        
        query = f"""
            UPDATE {table}
            SET {
                ', '.join([key_value_to_string(key, val) for key, val in zip(keys, values)])
            }
            WHERE {condition}; 
        """ if condition else f"""
            INSERT INTO {table} ({', '.join(keys)})
            VALUES ({', '.join(values)});
        """
        
        return Queries.simple_edit(query, connection=connection)

    @staticmethod
    def describe_table(table: str, connection: Union[RelationalConnection, str] = None) -> pd.DataFrame:
        '''
            Describes a table in connection
            Raises OperationalError and KeyError(Failed to find a connection for given key) 
        '''
        if not isinstance(table, str):
            return pd.DataFrame()

        connection = Queries.__get_known_connection(connection, RelationalConnection)
        
        data = connection.describe(table)
        
        data.insert(0, "Label", data['Field'].map(W2P_COLUMN_TO_LABEL))

        return data

    @staticmethod
    def describe(connection: Union[RelationalConnection, str] = None) -> pd.DataFrame:
        '''
            Describe Table names in connection
            Raises OperationalError and KeyError(Failed to find a connection for given key) 
        '''
        
        return Queries.__get_known_connection(connection, RelationalConnection).describe()

    @staticmethod
    @__cache
    def table_query(
        table: str, columns: Union[list, str] = '*', condition: str = 'TRUE', 
        connection: Union[RelationalConnection, str] = None, 
        represent: bool = False, raw: bool = False, 
        cache: Storage=None, ttl: bool = None
    ) -> pd.DataFrame:
        '''
            Queries a given connection for 'SELECT {columns} FROM {table} WHERE {condition}'
            Accepts both column values and labels
            raw=True - column names as in db
            Queries a given Connection(ip)/str of a known connection (or first known) return result as DataFrame
            Cache if cache or first known with ttl or default ttl for cache
            Raises OperationalError and KeyError(Failed to find a connection for given key) 
        '''
        if isinstance(columns, str):
            columns = list(
                map(
                    str.strip,
                    filter(
                        None, 
                        split(
                            ' , |, | ,|,',
                            columns
                        )
                    )
                )
            )
        
        _columns = [W2P_LABEL_TO_COLUMN.get(column, column) for column in columns]
        
        data = Queries.__query(
            f"SELECT {', '.join(_columns)} FROM {table} WHERE {condition}",
            connection=connection,
            cache=cache,
            ttl=ttl
        )
        
        if not raw:
            try:
                #Columns as requested!
                data.columns = columns 

            except ValueError:
                # Case columns contain *
                data.columns = [W2P_COLUMN_TO_LABEL.get(column, column) for column in data.columns]
                pass
            
        data._tables = [table]
        
        if represent:
            data = w2p_repr(data)

        return data

    @staticmethod
    @__cache
    def neware_query(
        device: int, unit: int, channel: int, test: int, connection: Union[MySqlConnection, str] = None, 
        columns: Union[list, str] = [NW_UNIT, NW_CHANNEL, NW_TEST, NW_CYCLE, NW_SEQ, NW_STEP, NW_STEP_TYPE, NW_TIMESTAMP, NW_VOLTAGE, NW_CURRENT], 
        condition: str = 'TRUE', raw: bool = False, dqdv: bool = False, temperature: bool = False,
        cache_data: pd.DataFrame = pd.DataFrame(), cache: Storage = None, ttl: int = None,
    ) -> pd.DataFrame:
        '''
            Queries a given Connection(ip)/str of a known connection (or first known) return result as DataFrame
            Cache if cache or first known with ttl or default ttl for cache
            If dqdv -> neware.calc_dq_dv
            Raises KeyError and OperationalError
        '''
        connection = Queries.__get_known_connection(connection, MySqlConnection)
        
        # Look for the tables
        try:
            neware_data = Queries.__query(
                f'SELECT * FROM h_test WHERE dev_uid = {device} AND unit_id = {unit} AND chl_id = {channel} AND test_id = {test}',
                connection=connection
            ).iloc[0] # A single row is returned since we looked by primary key

            first_main_table = neware_data[FIRST_NEWARE_DATA_TABLE]
            first_aux_table = neware_data[FIRST_NEWARE_AUX_TABLE]

            second_main_table = neware_data[SECOND_NEWARE_DATA_TABLE] # May be None
            second_aux_table = neware_data[SECOND_NEWARE_AUX_TABLE] # May be None

        except IndexError:
            raise TypeError(f'{connection.name} has No data for device:{device}, unit:{unit}, channel:{channel}') 
        
        if isinstance(columns, str): # Determine what columns are requested
            columns = NW_DATA_SIGNIFICANT_COLUMNS if columns == '*' else to_list(columns)
        
        nw_columns = [column for column in columns if column in NW_DATA_SIGNIFICANT_COLUMNS] # Requested neware columns
        nw_cache_columns = [column for column in columns if column not in NW_DATA_SIGNIFICANT_COLUMNS] # Requested neware cache columns (only other source)
        
        try: # neware_cache contains the calculated cycle
            nw_cache_columns.append(
                nw_columns.pop(nw_columns.index(NW_CYCLE))
            )

        except ValueError: # Cycle was not requested
            pass
        
        if not nw_columns: # Case No neware columns were requested
            nw_columns.append(NW_SEQ) # Handle by appending seq_id
        
        # Parse W2P query
        condition = parse_w2p_to_mysql_query(condition)
        
        # Try to adjust query condition!
        if isinstance(cache_data, pd.DataFrame) and not cache_data.empty:
            try:
                condition = query_cache(
                    cache_data, str(condition)
                )
                
            except pd.core.computation.ops.UndefinedVariableError:
                pass
        
        required_columns = set([
            NW_SEQ, NW_TIMESTAMP, NW_STEP_RANGE, NW_VOLTAGE, NW_CURRENT, *nw_columns
        ]) # The actually needed columns (requested + required) 
        
        required_columns = ', '.join(required_columns) # to string
        
        first_data = Queries.__query(
            f'SELECT {required_columns} FROM {first_main_table} WHERE unit_id = {unit} AND chl_id = {channel} AND test_id = {test} AND {condition}', 
            connection=connection
        )

        second_data = Queries.__query(
            f'SELECT {required_columns} FROM {second_main_table} WHERE unit_id = {unit} AND chl_id = {channel} AND test_id = {test} AND {condition}', 
            connection=connection
        ) if second_main_table else pd.DataFrame() # There is a second main table for the test

        if temperature: # Temperature requested
            nw_aux_columns = ', '.join(NW_AUX_SIGNIFICANT_COLUMNS)

            if not first_data.empty: # If we have data in first_data then we will have from first_aux_table
                first_aux_data = Queries.__query(
                    f'SELECT {nw_aux_columns} FROM {first_aux_table} WHERE unit_id = {unit} AND chl_id = {channel} AND test_id = {test} AND {condition}', 
                    connection=connection
                )

                if not first_aux_data.empty:
                    first_data = pd.merge(first_data, first_aux_data, on=NW_SEQ) # Merge Aux from first_aux_table

            if second_aux_table and not second_data.empty: # There is a second aux table for the test and we have data in second_data then we will have from second_aux_table
                second_aux_data = Queries.__query(
                    f'SELECT {nw_aux_columns} FROM {second_aux_table} WHERE unit_id = {unit} AND chl_id = {channel} AND test_id = {test} AND {condition}', 
                    connection=connection
                )
                second_data = pd.merge(second_data, second_aux_data, on=NW_SEQ) # Merge Aux from second_aux_table

        # Into a single Dataframe
        data = pd.concat([first_data, second_data], ignore_index=True)

        try:
            data = data.group_by_auxchl() # Banner method, neware.group_by_auxchl
            nw_columns.extend([column for column in data.columns if column.startswith(NW_TEMP)]) # nw_columns add temp columns
            
        except KeyError:
            pass
        
        if not raw:
            data = calculate_neware_columns(data, cache_df=cache_data) # Calculate neware columns

        if dqdv:
            data['dqdv'] = calculate_dqdv(data, raw=raw) # Calculate dqdv
            nw_columns.append('dqdv')

        try:
            data = merge_cache(data, cache_data, columns=nw_cache_columns) # Merge requested cache columns

        except KeyError:
            pass

        data = data[[*nw_columns, *nw_cache_columns]] # Keep requested columns
            
        return data
        

    @staticmethod
    def __neware_queries(
        devices: list, units: list, channels: list, tests: list, connection: Union[MySqlConnection, str] = None, 
        columns: Union[list, str] = [NW_UNIT, NW_CHANNEL, NW_TEST, NW_CYCLE, NW_SEQ, NW_STEP, NW_STEP_TYPE, NW_TIMESTAMP, NW_VOLTAGE, NW_CURRENT], condition: str = 'TRUE',  
        temperature: bool = False, dqdv: bool = False, cache_data: pd.DataFrame = pd.DataFrame(),
        cache: Storage = None, ttl: int = None, raw: bool = False, 
    ):  
        _connection_key = connection

        if isinstance(connection, Connection):
            _connection_key = str(name)

        data = dict()
        
        for device, unit, channel, test in zip(devices, units, channels, tests):
            try:
                data.update({
                    tuple([_connection_key, device, unit, channel, test]): Queries.neware_query(
                        device, unit, channel, test,
                        connection=connection,
                        cache=cache,
                        ttl=ttl,
                        raw=raw, 
                        dqdv=dqdv, 
                        condition=condition,
                        columns=columns,
                        temperature=temperature, 
                        cache_data=cache_data[
                            (cache_data.dev_uid == int(device)) &
                            (cache_data.unit_id == int(unit)) & 
                            (cache_data.chl_id == int(channel)) & 
                            (cache_data.test_id == int(test))
                        ]
                    )
                })

            except (TypeError, KeyError, ValueError):
                pass
        
        return data

    @staticmethod
    @__cache
    def neware_cache_query(
        keys: Iterable, columns: Union[list, str] = '*', 
        condition: str = 'TRUE', connection: Union[MySqlConnection, str] = None, 
        cache: Storage = None, ttl: int = None
    ) -> pd.DataFrame:
        '''
            Queries a given Connection(ip)/str of a known connection (or first known) return result as DataFrame
            Keys in the form (ip, device, unit, channel, test)
            Cache if cache or first known with ttl or default ttl for cache
            Raises KeyError and OperationalError
        '''
        connection = Queries.__get_known_connection(connection, MySqlConnection)

        multiple = True if len(keys) > 1 else False
        
        if not isinstance(columns, str):
            columns = ','.join(columns)

        try:
            if (all(isinstance(item, Iterable) for item in keys)):
                _keys = [tuple(key) for key in keys] # Make sure each key(collection) is a tuple
                
            else:
                _keys = [tuple(keys)] # Single entry was given
            
            _keys = [
                f'({ip},{device},{unit},{channel},{test})' for ip, device, unit, channel, test in _keys
            ]

        except (TypeError, ValueError):
            raise ValueError(f'Bad Input, Expected List(Tuple)')
        
        _keys = f'(ip,dev_uid,unit_id,chl_id,test_id) IN ({",".join(_keys)})'
        
        if not isinstance(columns, str):
            columns = ','.join(columns)

        cache_data = pd.DataFrame()

        for cache_table in ('neware_cache', 'neware_pulses_cache', 'neware_cache_anode'):
            cache_data = pd.concat([
                cache_data,
                Queries.__query(f"""
                        SELECT {columns} FROM {cache_table} 
                        WHERE {_keys}
                        AND {condition} 
                    """,
                    connection=connection
                )
            ])
            
            if not multiple and not cache_data.empty:
                return cache_data
        
        cache_data._tables = ['neware_cache'] # All table formats are the same!

        return cache_data

    @staticmethod
    def __neware_tests_query(
        table: str, experiments: str = '', templates: str = '', tests: str = '', cells: str = '', 
        columns: Union[list, str] = [NW_UNIT, NW_CHANNEL, NW_TEST, NW_CYCLE, NW_SEQ, NW_STEP, NW_STEP_TYPE, NW_TIMESTAMP, NW_VOLTAGE, NW_CURRENT],
        condition: str = 'TRUE', raw: bool = False, dqdv: bool = False, temperature: bool = False, 
        connection: Union[MySqlConnection, str] = None, cache: Storage = None, ttl: int = None
    ):  
        if not any([experiments, templates, tests, cells]):
            raise ValueError('A combination of experiments, templates, tests, cells is Required')
        
        connection = Queries.__get_known_connection(connection, MySqlConnection)

        __tests_query = f"""
            SELECT 
                {table}_test.ip, {table}_test.device, {table}_test.unit, {table}_test.channel, {table}_test.test_id
            FROM {table}
            LEFT JOIN {table}_test
            ON {table}.id = {table}_test.{table}_id
            LEFT JOIN {table}_test_template
            ON {table}_test.test_type_id = {table}_test_template.id
            WHERE 1
        """
        
        if experiments and isinstance(experiments, str):
            __tests_query += f' AND {experiments}'
        
        if templates and isinstance(templates, str):
            __tests_query += f' AND {templates}'

        if tests and isinstance(tests, str):
            __tests_query += f' AND {tests}'

        if cells and isinstance(cells, str):
            __tests_query += f' AND {cells}'
        
        __tests = Queries.__query(
            __tests_query,
            connection=connection,
            cache=cache,
            ttl=ttl
        ).dropna()
        
        if __tests.empty:
            return {}

        # Make sure all data is numeric
        __tests = __tests.astype(int, errors='ignore')
        
        __cached_data = Queries.neware_cache_query(
            list(__tests.itertuples(index=False, name=None)),
            connection=connection,
            cache=cache,
            ttl=ttl
        )
        
        __tests_by_ip = __tests.groupby('ip')
        
        data = Parallel(n_jobs=__tests_by_ip.ngroups, require='sharedmem', verbose=0)(
            delayed(Queries.__neware_queries)(
                df['device'].values, df['unit'].values, df['channel'].values, df['test_id'].values,
                connection=name, cache=cache, ttl=ttl, raw=raw, columns=columns,
                dqdv=dqdv, condition=condition, temperature=temperature,
                cache_data=__cached_data[__cached_data.ip == int(name)]
            )
            for name, df in __tests_by_ip
        )
        
        return dict(ChainMap(*data))

    @staticmethod
    def neware_tests_query(
        table: str, experiments: Union[list, Number, str] = [], templates: Union[list, Number, str] = [], 
        tests: Union[list, Number, str] = [], cells: Union[list, Number, str] = [], 
        columns: Union[list, str] = [NW_UNIT, NW_CHANNEL, NW_TEST, NW_CYCLE, NW_SEQ, NW_STEP, NW_STEP_TYPE, NW_TIMESTAMP, NW_VOLTAGE, NW_CURRENT], 
        condition: str = 'cycle < 2', raw: bool = False, dqdv: bool = False, temperature: bool = False,
        connection: Union[MySqlConnection, str] = None, cache: Storage = None, ttl: int = None
    ):
        if not any([experiments, templates, tests, cells]):
            raise ValueError('A combination of experiments, templates, tests, cells is Required')
        
        if experiments and not isinstance(experiments, str):
            experiments = to_sql_range(experiments, 'experiments', table, 'REGEXP')

        if templates and not isinstance(templates, str):
            templates = to_sql_range(templates, 'id', f'{table}_test_template')

        if tests and not isinstance(tests, str):
            tests = to_sql_range(tests, 'id', f'{table}_test')

        if cells and not isinstance(cells, str):
            cells = to_sql_range(cells, 'id', table)
        
        return Queries.__neware_tests_query(
            table, experiments, templates, 
            tests, cells, columns, condition, raw, 
            dqdv, temperature, connection, cache, ttl
        )
    
class AugmentQueries(object):
    PER_CYCLE_TABLE = 'augm_per_cycle'
    PER_CELL_TABLE = 'augm_per_cell'
    PER_TEST_TABLE = 'augm_per_test'
    PER_PULSE_TABLE = 'augm_per_pulse'

    AUGMENT_TABLES = (
        PER_CYCLE_TABLE,
        PER_CELL_TABLE,
        PER_TEST_TABLE,
        # PER_PULSE_TABLE
    )

    __REQUIRED_COLUMNS_PER_TABLE = {
        PER_CYCLE_TABLE: ['ip', 'dev_uid', 'unit_id', 'chl_id', 'test_id', 'cycle'],
        PER_CELL_TABLE: ['cell_table', 'cell_id'],
        PER_TEST_TABLE: ['augm_per_cell', 'test_id'],
    }

    TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

    COLUMN_DESCRIPTION_INDEX = '_description'
    COLUMN_UPDATED_ON_INDEX = '_updated_on'

    def __init__(self, connection: RelationalConnection):
        self._connection = connection

    def __assert_augment_table(self, table: str):
        if table not in AugmentQueries.AUGMENT_TABLES:
            raise ValueError(f'Available Augment Tables: {AugmentQueries.AUGMENT_TABLES}')
    
    def set_features(self, table: str, features: pd.DataFrame, columns: list, validate=True): # TABLE, CELL, TEST_ID, CYCLE 
        self.__assert_augment_table(table)

        features = features.copy()

        if validate:
            features = self.__filter_non_existant(table, features)
        
        try:
            keys = [f'("{row.cell_table}",{row.cell_id})' for _, row in features.iterrows()]
            
            self.__create_rows_per_cell(keys) # Create Per Cell Rows!

            features = features.merge(
                self.__get_per_cell_rows(keys), # Relevant Rows
                how='left', on=['cell_table', 'cell_id']
            ) # Add params
            
            if table != AugmentQueries.PER_CELL_TABLE: # Tests/Cycles/Pulses
                keys = [f'("{row.augm_per_cell}",{row.test_id})' for _, row in features.iterrows()]
                
                self.__create_rows_per_test(keys) # Create Per Test Rows!
                
                features = features.merge(
                    self.__get_per_test_rows(keys), # Relevant Rows
                    how='left', 
                    left_on=['augm_per_cell', 'test_id'], 
                    right_on=['augm_per_cell', 'augm_per_test_id']
                ) # Add params
                
                if table != AugmentQueries.PER_TEST_TABLE: # Cycles/Pulses
                    features = self.__create_and_get_rows_per_cycle_or_pulse(features, table)
            
            for part in features.split(): # Banner function 
                self.__set_feature(table, part, columns) # Set feature into table
        
        except KeyError:
            pass
        
    def add_feature(self, table: str, name: str, dtype: str, index=False, description=False, updated_on=False):
        self.__assert_augment_table(table)
        
        self.__add_column(table, name, dtype)

        if index:
            self.__add_index(table, name)

        if description:
            self.__add_column(table, f'{str(name)}{AugmentQueries.COLUMN_DESCRIPTION_INDEX}', 'VARCHAR(255)')

        if updated_on:
            self.__add_column(table, f'{str(name)}{AugmentQueries.COLUMN_UPDATED_ON_INDEX}', 'DATETIME')

    def __add_column(self, table: str, name: str, dtype: str):
        Queries.simple_edit(
            f'ALTER TABLE {table} ADD COLUMN {str(name)} {str(dtype)}',
            connection=self._connection
        )

    def __add_index(self, table: str, name: str):
        Queries.simple_edit(
            f'ALTER TABLE {table} ADD INDEX ({str(name)})',
            connection=self._connection
        )

    def __get_per_cell_rows(self, keys: Iterable):
        condition = f'(cell_table, cell_id) IN ({",".join(keys)})'
        
        return Queries.simple_query(
            f'SELECT id as augm_per_cell, cell_table, cell_id FROM {AugmentQueries.PER_CELL_TABLE} WHERE {condition}',
            connection=self._connection
        )

    def __create_rows_per_cell(self, keys: Iterable):
        Queries.simple_edit(
            f"""
                INSERT INTO {AugmentQueries.PER_CELL_TABLE} (cell_table, cell_id) 
                VALUES {",".join(keys)}
                ON DUPLICATE KEY
                UPDATE cell_table=cell_table, cell_id=cell_id;
            """,
            connection=self._connection
        )

    def __get_per_test_rows(self, keys: Iterable):
        condition = f'(augm_per_cell, test_id) IN ({",".join(keys)})'
        
        return Queries.simple_query(
            f'SELECT id as augm_per_test, augm_per_cell, test_id as augm_per_test_id FROM {AugmentQueries.PER_TEST_TABLE} WHERE {condition}',
            connection=self._connection
        )

    def __create_rows_per_test(self, keys: Iterable):
        Queries.simple_edit(
            f"""
                INSERT INTO {AugmentQueries.PER_TEST_TABLE} (augm_per_cell, test_id)
                VALUES {",".join(keys)}
                ON DUPLICATE KEY
                UPDATE augm_per_cell=augm_per_cell, test_id=test_id;
            """,
            connection=self._connection
        )

    def __set_feature(self, table: str, features: pd.DataFrame, columns: list):
        if not columns:
            return
        
        columns = list(columns)
        
        _columns = [*AugmentQueries.__REQUIRED_COLUMNS_PER_TABLE[table], *columns]
        
        _features = features[_columns] # augm_per_test requires id!
        
        table_description = Queries.describe_table(table, connection=self._connection)
        
        updated_on_columns = list()

        for column in columns:
            if (column_updated_on_index := f'{column}{AugmentQueries.COLUMN_UPDATED_ON_INDEX}') in table_description.Field.values:
                updated_on_columns.append(column_updated_on_index)
        
        _features = _features.assign(**{
            column: datetime.now().strftime(AugmentQueries.TIMESTAMP_FORMAT) for column in updated_on_columns
        })
        
        columns.extend(updated_on_columns)

        values = [
            str(tuple(row)) for row in _features.values.tolist() # Iterate every row
        ]
        
        columns_as_str = ', '.join(_features.columns)
        
        on_duplicate = [f'{column}=VALUES({column})' for column in columns]
        
        Queries.simple_edit(
            f"""
                INSERT INTO {table} ({columns_as_str})
                VALUES {','.join(values)}
                ON DUPLICATE KEY 
                UPDATE {','.join(on_duplicate)};
            """,
            connection=self._connection
        )

    def __create_and_get_rows_per_cycle_or_pulse(self, data: pd.DataFrame, table: str):
        column = 'cycle' if AugmentQueries.PER_CYCLE_TABLE else 'pulse'

        def __create_augm_per_pk(group):
            data = Queries.table_query(
                f'{group.name}_test', 
                columns=['id', 'ip', 'device', 'unit', 'channel', 'test_id', 'full_cycles'], 
                condition=f"id IN ({', '.join(group['augm_per_test_id'].astype(str))})"
            )
            
            group.drop(['id', 'ip', 'device', 'unit', 'channel', 'test_id', 'dev_uid', 'unit_id', 'chl_id'], inplace=True, axis=1, errors='ignore')
            joined_group = group.merge(data, how='left', left_on='augm_per_test_id', right_on=f'id')
            joined_group['device'] = pd.to_numeric(joined_group['device']) # device is originally a string
            
            joined_group = joined_group[joined_group['full_cycles'] >= joined_group['cycle']]

            if joined_group.empty:
                return joined_group

            values = [
                f'({row.augm_per_test}, {row.ip}, {row.device}, {row.unit}, {row.channel}, {row.test_id}, {row[column]})' # in the form (augm_per_cell, ip, dev_uid, unit_id, chl_id, test_id, column)
                for _, row in joined_group.iterrows() # Iterate every row
            ]
            
            values_as_string = ", ".join(values)
            
            # Set rows
            Queries.simple_edit(
                f"""
                    INSERT INTO {table} (augm_per_test, ip, dev_uid, unit_id, chl_id, test_id, {column}) 
                    VALUES {values_as_string}
                    ON DUPLICATE KEY
                    UPDATE ip=ip, dev_uid=dev_uid, unit_id=unit_id, chl_id=chl_id, test_id=test_id, {column}={column};
                """,
                connection=self._connection
            )
            
            _data = Queries.simple_query(
                f'SELECT id as augm_per_{column}, ip, dev_uid, unit_id, chl_id, test_id, {column} FROM {table} WHERE (augm_per_test, ip, dev_uid, unit_id, chl_id, test_id, {column}) IN ({values_as_string})',
                connection=self._connection
            )
            
            return joined_group.merge(
                _data, how='left', 
                left_on=['ip', 'device', 'unit', 'channel', 'test_id', 'cycle'],
                right_on=['ip', 'dev_uid', 'unit_id', 'chl_id', 'test_id', 'cycle']
            )
        
        return data.groupby('cell_table').apply(__create_augm_per_pk)

    def __filter_non_existant(self, table: str, data: pd.DataFrame):
        def __filter_by_cells(group):
            condition=f"id IN ({', '.join(group['cell_id'].astype(str))})"

            valid_ids = Queries.table_query(
                group.name, condition=condition, columns='id'
            )
            
            if valid_ids.empty:
                return valid_ids

            return group.merge(valid_ids, how='right', left_on='cell_id', right_on='id')

        def __filter_by_tests(group):
            query_table = f'{group.name}_test'
            
            values = [str(tpl) for tpl in group[['test_id', 'cell_id']].itertuples(index=False, name=None)]
            condition = f"(id, {group.name}_id) IN ({', '.join(values)})"
            
            valid_ids = Queries.table_query(
                query_table, condition=condition, columns='id'
            )

            if valid_ids.empty:
                return valid_ids

            return group.merge(valid_ids, how='right', left_on='test_id', right_on='id')

        filter_func = __filter_by_cells if table == AugmentQueries.PER_CELL_TABLE else __filter_by_tests

        return data.groupby('cell_table', as_index=False).apply(filter_func)

