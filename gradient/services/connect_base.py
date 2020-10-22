import os
import sys
import vertica_python
from gradient.core.config import DEFAULT_CONFIG_JSON_PATH, _connection_params
from gradient.utils.json_utils import _load_json_data


class Connect:
    """
    Base class for database interaction.

    ...

    Attributes
    ----------
    self.connection_params : (dict) app user and secret for Vertic connection
    self.query : (str) name of query being executed

    Methods
    -------
    _db_connect(): Method to instantiate database connection.
    _db_sever(cursor, connection): Method to force close database connection.
    """

    def __init__(self, object, query):
        """Special initializer to assign connection parameters from db_config.json

        : param object: (str) one of 'vertica', 'mysql, 'kusto'
        : param query (str) specifies query for execution
        """
        if object == 'mysql':
            self.connection_params = _connection_params()['mysql_params']
        elif object == 'kusto':
            self.connection_params = _connection_params()['kusto_params']
        else:
            self.connection_params = _connection_params()['vertica_params']

        self.query = query

    def _db_connect(self):
        """Returns connection object for queries
        """
        if self.connection_params is not None:
            print("Connection to DB is open")
            return vertica_python.connect(**self.connection_params)
        return "connection_params not defined"

    def _db_sever(self, cursor, connection):
        """Force closes database connection

        :param cursor: (dict) database cursor object
        :param connection: (dict) database connection object
        """
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()
            print("Connection successfully closed")
