import os
import json
from datetime import date,datetime
import decimal

def _load_json_data(path):
    """Simple path execution to read json files
    """
    if os.path.exists(path):
        with open(path) as outfile:
            json_data = json.load(outfile)
            return json_data

def _write_json_to_file(json_data, path):
    """Method to write json to file
    """
    if not os.path.exists(path):
        dir_path = os.path.dirname(path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    with open(path, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code

    :param obj:
    :return:
    """
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return str(obj)
    raise TypeError ("Type {} not serializable" .format(type(obj)))

def data_json_formatter(cursor_obj, date_bool=False):
    """
    Formats cursor obj from DB response to meet JSON standards

    :param cursor_obj: (dict)
    :param date_bool: (bool) If true, serializes datetime obj for JSON
    :return: (dict) JSON-formatted response
    """
    json_data = []
    if not cursor_obj or not cursor_obj.description:
        return json_data
    try:
        row_headers = [x[0] for x in cursor_obj.description]
        rv = cursor_obj.fetchall()
        if not rv:
            response_object = {
                'state': 'error',
                'message': 'Results could not be parsed'
            }
            return response_object
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))

        if date_bool:
            return json.loads(json.dumps(json_data, default=json_serial))
        return json_data
    except BaseException as error:
        raise error