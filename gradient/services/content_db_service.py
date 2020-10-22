from gradient.services.connect_base import Connect
from gradient.queries.content_queries import WOW_AGGREGATE
from gradient.utils.json_utils import data_json_formatter
from gradient.core.logging import GradientLogger


class ContentDBService(Connect):

    @GradientLogger()
    def _wow_aggregate(self):
        try:
            # create DB connection object
            connection = self._db_connect()
            # create connection cursor object
            cursor = connection.cursor()
            # execute query
            cursor.execute(WOW_AGGREGATE())
            # pass the response through the JSON formatter
            response_cursor = data_json_formatter(cursor, date_bool=True)
            # sever DB connection
            self._db_sever(cursor, connection)
            return response_cursor
        except BaseException as e:
            raise e

    @GradientLogger()
    def _unfamiliar_crit_one_day(self):
        return 0


if __name__ == '__main__':
    x = ContentDBService('vertica', 'unfamiliar_query')
    response = x._wow_aggregate()
    print(response)