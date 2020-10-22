from gradient.services.connect_base import Connect
from gradient.queries.test_query import TEST_QUERY
from gradient.utils.json_utils import data_json_formatter
from gradient.core.logging import GradientLogger

class TestDBService(Connect):

    @GradientLogger()
    def _test_query(self):
        try:
            # create DB connection object
            connection = self._db_connect()
            # create connection cursor object
            cursor = connection.cursor()
            # execute query
            cursor.execute(TEST_QUERY())
            # pass the response through the JSON formatter
            response_cursor = data_json_formatter(cursor, date_bool=True)
            # sever DB connection
            self._db_sever(cursor, connection)
            return response_cursor
        except BaseException as e:
            raise e



if __name__ == '__main__':
    x = TestDBService('vertica', 'test_query')
    response = x._test_query()
    print(response)