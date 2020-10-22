import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("API_KEY")
IS_DEBUG = os.getenv("IS_DEBUG")
DEFAULT_CONFIG_JSON_PATH = os.getenv("DEFAULT_CONFIG_JSON_PATH")
DEFAULT_LOG_PATH = os.getenv("DEFAULT_LOG_PATH")

API_PREFIX = os.getenv("API_PREFIX")
APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

# set path for log files. Variable must be set in .env
# root_directory = os.path.split(os.path.abspath(''))[0]
# DEFAULT_LOG_PATH = '{}{}'.format(root_directory, os.getenv("DEFAULT_LOG_PATH"))


def _connection_params(is_prod=False):
    global LOCAL_USER, LOCAL_PASSWORD

    LOCAL_USER = os.getenv("LOCAL_USER")
    LOCAL_PASSWORD = os.getenv("LOCAL_PASSWORD")

    if is_prod:
        LOCAL_USER = ''
        LOCAL_PASSWORD = ''

    return {
            "meta": {
                "name": "Database Configuration",
                "author": "richard_scheiwe",
                "recency": "10 Oct 2020",
                "description": "Configuration variables for databases",
                "keywords": [
                    "database",
                    "data"
                ],
                "allowed": [
                    "[a-zA-Z0-9_]"
                ]
            },
            "vertica_params": {
                "host": "",
                "port": "",
                "user": LOCAL_USER,
                "password": LOCAL_PASSWORD,
                "database": "",
                "connection_timeout": 120
            },
            "mysql_params": {

            },
            "kusto_params": {

            }
        }
