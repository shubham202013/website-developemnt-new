import base64
import datetime
import html
import json
import os
import random

from flask import jsonify

from common.constants import ERROR_CODE_DATA_NOT_FOUND, COUNTRY
from common.internal_request import post_request

PAGE_SIZE = 10
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

def generate_uuid():
    """
    Generate uuid
    """
    from bson import ObjectId
    return str(ObjectId())


def html_response(data=''):
    """
    Common response
    """
    from flask import make_response
    headers = {'Content-Type': 'text/html'}
    return make_response(data, 200, headers)



def success_response(data={}, message="", code=200, success=True):
    """
    Common success response
    """
    response_data = dict()
    response_data["data"] = data

    if message:
        response_data["message"] = message
    if code:
        response_data["code"] = code
    response_data['success'] = success
    response_data["error"] = []

    return jsonify(response_data)


def internal_success_response(data={}, message="", code=200, success=True):
    """
    Common success response
    """
    response_data = dict()
    # if not data:
    response_data["data"] = data

    if message:
        response_data["message"] = message
    if code:
        response_data["code"] = code
    response_data['success'] = success
    response_data["error"] = []

    return jsonify(response_data)


def error_response(error_code=ERROR_CODE_DATA_NOT_FOUND, message="", success=False):
    """
    Common Error response
    """
    response_data = dict()
    response_data["data"] = {}
    response_data["message"] = message
    response_data["error_code"] = error_code
    response_data["success"] = success
    return jsonify(response_data)

def error_response_for_under_maintenance(error_code=ERROR_CODE_DATA_NOT_FOUND, message="", success=False,data={}):
    response_data = dict()
    response_data["data"] = {}
    response_data["message"] = message
    response_data["error_code"] = error_code
    response_data["success"] = success
    response_data['data'] =data
    return jsonify(response_data)


def get_search_term(search_term):
    """
    get/filter search term
    """
    search_term = search_term.replace("'", " ")
    search_term = search_term.replace('"', " ")
    search_term = search_term.replace('\\', " ")

    return search_term


def get_search_query(search_fields, request):
    """
    generate common search query for mysql
    """

    query_condition = dict()
    if search_fields and request.args.get('search', None):
        search = request.args.get('search')
        search = search.lower()
        search_term = search.split(' ')
        if search_term:
            query_condition['_search'] = dict()
            for i in search_fields:
                query_condition['_search'].update({i: search_term[0]})

    return query_condition


def generate_txn_no():
    import random as r

    otp_str = "TXN_"
    for i in range(4):
        otp_str += str(r.randint(1, 9))
    otp = otp_str
    return otp


def get_filter_query(filter_fields, request):
    """
    Generate common filter query
    """
    query_condition = dict()
    for field in filter_fields:
        if request.args.get(field, None):
            value = request.args.get(field)
            if isinstance(value, list):
                query_condition["{0}".format(field)] = {"$in": value}
            else:
                query_condition["{0}".format(field)] = value

    return query_condition


def tuple_to_dict(tuple_list):
    """
    tuple to dict converter
    """
    result = list()
    for data in tuple_list:
        data_dict = dict()
        data_dict['id'] = data[0]
        data_dict['value'] = data[1]
        result.append(data_dict)
    return result


def currency_tuple_to_dict(tuple_list):
    """
    currency to dict convert
    """
    result = list()
    for data in tuple_list:
        data_dict = dict()
        data_dict['id'] = data[0]
        data_dict['value'] = f"{data[0]} ({html.unescape(data[1])}) "
        result.append(data_dict)
    return result


def allowed_file(filename):
    """
    allowed file for validation
    """
    ALLOWED_EXTENSIONS = {'csv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def divide_chunks(l, n):
    """
    will make chunk of n for given l(list)
    """
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


def eta_display(seconds):
    """
    second parsing to display eta
    """
    if seconds:
        seconds = float(seconds)
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            hour = round(hour)
            minutes = round(minutes)
            minutes = "{:02d}".format(minutes)
            hour = "{:02d}".format(hour)
            return "{0}.{1} h".format(hour, minutes)
        else:
            minutes = round(minutes)
            minutes = "{:02d}".format(minutes)
            return "00.{0} h".format(minutes)
    elif seconds == 0:
        return "{0}.{1} h".format(0, 0)
    else:
        return None



def get_country_constant():
    """ get country constant """
    res = {}
    for k, v in COUNTRY.items():
        res[k] = v['name']
    return res


def generate_activation_token():
    """ generate activation toke for company"""
    length = 32
    import uuid
    return str(uuid.uuid4().hex[:length].upper())


def default_timezone():
    return 'UTC'


KAFKA_HOST = os.environ.get('KAFKA_HOST')


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

def get_document_type(type):
    if type == "release":
        return 1
    elif type == "task-list":
        return 2
    elif type == "task":
        return 3
    elif type == "bug":
        return 5
    else:
        return 4


def convert_float(data=None):
    result = None
    try:
        result = float(data)
    except Exception as e:
        print("convert_float error", e)
    return result


def get_object_from_choices(value, dit):
    data_info = dict()
    data_dict = dict(dit)
    try:
        data_info["value"] = value
        data_info["label"] = html.unescape(data_dict[value])
    except Exception as e:
        print("get_object_from_choices error -->", e)
        data_info["value"] = None
        data_info["label"] = None
    return data_info



def generate_8_digit_string():
    import uuid

    # Generate a random UUID (Universally Unique Identifier)
    random_uuid = uuid.uuid4()

    # Extract the hexadecimal representation from the UUID
    hex_string = random_uuid.hex

    # Take the first 8 characters from the hexadecimal string
    eight_digit_string = hex_string[:8]

    return eight_digit_string
