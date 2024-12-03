import json
import calendar

from common.internal_request import post_request
import os
import time
from datetime import datetime
from flask import request

import pytz

from common.constants import TIMEZONE_OFFSET_CHOICES
# from common.rediscomponant.redisware import get_from_redis, set_to_redis
# from v1.company import queryset as company_queryset

GET_DATE_FORMAT = "%d-%m-%Y"
DATE_FORMAT = "%d/%m/%Y"
TIME_FORMAT = "%I:%M %p"
DATE_TIME_FORMAT = "{} {}".format(DATE_FORMAT, TIME_FORMAT)
GET_TIME_FORMAT = "%H:%M:%S"
DATE_TIME_FORMAT_2 = "{} {}".format(GET_DATE_FORMAT, GET_TIME_FORMAT)


# def convert_datetime_to_display(datetime_obj=None, company_id=None, timezone="UTC"):
#     """
#     Created By : Naim
#     Created Date : 14-Dec-2019
#     Note: For convert datetime obj from db to view (frontend side)
#     """
#     result = None
#     if datetime_obj:
#         old_tz = "UTC"
#         new_tz = timezone
#         if company_id:
#             new_tz = pms_dt_timezone(company_id)
#         if type(datetime_obj) == str:
#             datetime_obj = string_to_datetime(datetime_obj, "%Y-%m-%dT%H:%M:%S")
#         res = convert_datetime_timezone(datetime_obj, old_tz, new_tz)
#         result = res.strftime(DATE_TIME_FORMAT)
#     return result


# def convert_datetime_to_display_custom(datetime_obj=None, company_id=None, timezone="UTC",
#                                        date_format=DATE_TIME_FORMAT):
#     """
#     Created By : Naim
#     Created Date : 14-Dec-2019
#     Note: For convert datetime obj from db to custom view (frontend side)
#     """
#     result = None
#     if datetime_obj:
#         old_tz = "UTC"
#         new_tz = timezone
#         if company_id:
#             new_tz = pms_dt_timezone(company_id)
#         if type(datetime_obj) == str:
#             datetime_obj = string_to_datetime(datetime_obj, "%Y-%m-%dT%H:%M:%S")
#         res = convert_datetime_timezone(datetime_obj, old_tz, new_tz)
#         result = res.strftime(date_format)
#     return result


# def convert_date_to_display(datetime_obj=None, company_id=None, timezone="UTC"):
#     """
#     Created By : Naim
#     Created Date : 22-02-2020
#     Note: For convert datetime obj from db to view (frontend side)
#     """
#     result = None
#     if datetime_obj:
#         if datetime_obj.date() == datetime.today().date():
#             return result
#         old_tz = "UTC"
#         new_tz = timezone
#         if company_id:
#             new_tz = pms_dt_timezone(company_id)
#         res = convert_datetime_timezone(datetime_obj, old_tz, new_tz)
#         result = res.strftime(DATE_FORMAT)
#     return result


# def convert_datetime_tz(datetime_obj=None, company_id=None, timezone="UTC"):
#     def _datetime_es(dt):
#         import datetime
#         try:
#             res = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S.%f")
#         except Exception as e:
#             print("convert_datetime_tz e", e)
#             res = None
#         return res

#     result = None
#     datetime_obj = _datetime_es(datetime_obj)
#     if datetime_obj:
#         old_tz = "UTC"
#         new_tz = timezone
#         if company_id:
#             new_tz = pms_dt_timezone(company_id)
#         result = convert_datetime_timezone(datetime_obj, old_tz, new_tz)
#     return result


def convert_date_to_utc(timezone=None):
    """
    Convert Datetime to UTC datetime object
    :param timezone:
    :return: datetime object
    """
    import datetime
    import pytz

    if not timezone:
        timezone = 'UTC'

    time_zone = pytz.timezone(timezone)
    # get naive date
    date = datetime.datetime.now().date()

    # get naive time
    time = datetime.time(0, 0)

    # combite to datetime
    date_time = datetime.datetime.combine(date, time)

    # make time zone aware
    date_time = time_zone.localize(date_time)

    # convert to UTC
    utc_date_time = date_time.astimezone(pytz.utc)

    return utc_date_time


def convert_datetime_timezone(datetime_obj, old_tz, new_tz):
    """
    :param datetime_obj: datetime object
    :param old_tz: ex. "Asia/Kolkata"
    :param new_tz: ex. "UTC"
    :return: converted datetime object
    """
    result = None
    if datetime_obj:
        old_timezone = pytz.timezone(old_tz)
        new_timezone = pytz.timezone(new_tz)
        if datetime_obj and datetime_obj.tzinfo is not None:
            result = datetime_obj.replace(tzinfo=old_timezone).astimezone(new_timezone)
        else:
            result = old_timezone.localize(datetime_obj).replace(tzinfo=old_timezone).astimezone(new_timezone)
    return result


def convert_datetime_timezone_v2(datetime_obj, old_tz, new_tz):
    """
    UPDATED BY NAIM MALEK FIX ISSUE (WHILE CONVERTING TO OLD TZ THERE IS ISSUE IN OFFSET of 13 MIN)
    :param datetime_obj: datetime object
    :param old_tz: ex. "Asia/Kolkata"
    :param new_tz: ex. "UTC"
    :return: converted datetime object
    """
    result = None
    if datetime_obj:
        old_timezone = pytz.timezone(old_tz)
        new_timezone = pytz.timezone(new_tz)
        if datetime_obj and datetime_obj.tzinfo is not None:
            datetime_obj = old_timezone.localize(datetime_obj.replace(tzinfo=None))
            res = datetime_obj
            result = res.astimezone(new_timezone)
        else:
            res = old_timezone.localize(datetime_obj, is_dst=None).replace(tzinfo=old_timezone)
            result = res.astimezone(new_timezone)
    return result


def timezone_offset_from_timezone(item):
    """
    get timezone offset from timezone
    :param item:
    :return:str
    """
    tz_dict = dict(TIMEZONE_OFFSET_CHOICES)
    tz_dict = dict((v, k) for k, v in tz_dict.items())
    return tz_dict.get(item, 'UTC')


def timezone_offset_from_timezone_name(item):
    """
    get timezone offset from timezone name
    :param item:
    :return:str
    """
    tz_dict = dict(TIMEZONE_OFFSET_CHOICES)
    tz_dict = dict((k, v) for k, v in tz_dict.items())
    return tz_dict.get(item, 'UTC')


def get_time_from_second(second):
    """
    get time from second
    :param second:
    :return: srt
    """
    result = None
    if second:
        result = time.strftime('%Hh %Mmin', time.gmtime(second))
    return result


def convert_timestamp_to_date(target_date):
    """
    convert to date from timestamp
    :param target_date:
    :param timezone:
    :param company_id:
    :return:
    """
    if target_date and target_date != "":
        if type(target_date) != float:
            target_date = float(target_date)
        try:
            result = datetime.fromtimestamp(target_date)
        except Exception as error:
            print("convert_timestamp_to_date error: ", error)
            result = None
        return result

    else:
        return None


def timestamp_to_datetime_v2(timestamp):
    """
    As per the PMS

    :param timestamp:
    :return:
    """
    try:
        return datetime.fromtimestamp(float(timestamp))
    except Exception as e:
        print("timestamp_to_datetime_v2 error -->", e)
        return None


def timestamp_to_datetime(timestamp, tz_offset=None, timezone=None):
    """
    :param timestamp: timestamp
    :param tz_offset: ex. +05:30
    :param timezone: ex. Asia/Kolkata
    :return: date
    """
    result = None
    if timestamp:
        try:
            if tz_offset:
                timezone = timezone_offset_from_timezone(tz_offset)
                utc_dt = datetime.utcfromtimestamp(timestamp)
                aware_utc_dt = utc_dt.replace(tzinfo=pytz.utc)
                date = aware_utc_dt.astimezone(pytz.timezone(timezone))
                result = date.strftime(DATE_TIME_FORMAT)
            elif timezone:
                utc_dt = datetime.utcfromtimestamp(timestamp)
                aware_utc_dt = utc_dt.replace(tzinfo=pytz.utc)
                date = aware_utc_dt.astimezone(pytz.timezone(timezone))
                result = date.strftime(DATE_TIME_FORMAT)
            else:
                utc_dt = datetime.utcfromtimestamp(timestamp)
                result = utc_dt.strftime(DATE_TIME_FORMAT)
        except Exception as error:
            print("Exception error: ", error)
            result = timestamp
    print("result----------_>", type(result))
    return result


def timestamp_to_datetime_new(timestamp):
    try:
        return datetime.fromtimestamp(float(timestamp))
    except Exception as e:
        print("timestamp_to_datetime_new error -->", e)
        return None


def datetime_to_string_using_tz(date, tz_offset=None):
    """
    :param date: datetime
    :param tz_offset: ex. +05:30
    :return: date
    """
    if date:
        if tz_offset:
            try:
                timezone = timezone_offset_from_timezone(tz_offset)
                date = date.astimezone(pytz.timezone(timezone))
                date = date.strftime(DATE_TIME_FORMAT)
            except Exception as error:
                print("Exception error: ", error)
        else:
            try:
                date = date.strftime(DATE_TIME_FORMAT)
            except Exception as e:
                print("datetime_to_string_using_tz error -->", e)
    return date


def time24_to_12(dt_obj=None, c_timezone=None):
    """
    :param time: datetime (object)
    :return: 01:00 PM (String)
    """
    result = dt_obj
    if dt_obj:
        try:
            start_time = convert_datetime_timezone(dt_obj, 'UTC', c_timezone)
            result = start_time.strftime(TIME_FORMAT)
        except Exception as e:
            print(">>>> eeeeeeee", e)
            result = dt_obj
    return result


def string_to_datetime(date, i_format=DATE_TIME_FORMAT):
    """
    String to date time
    :param date:
    :param i_format:
    :return: date object
    """
    result = None
    if date:
        try:
            result = datetime.strptime(date, i_format)
        except Exception as e:
            print("string_to_datetime e", e)
            result = date
    return result


def time_to_save(c_time, d_format=None):
    """
    convert time to dattime for save to DB
    :param c_time:
    :return:
    """
    if not d_format:
        d_format = "%Y-%m-%d %H:%M:%S"
    if c_time:
        tdate = datetime.date(datetime.now())
        try:
            start_time = datetime.strptime("{} {}".format(tdate, c_time), d_format)
            return start_time
        except Exception as e:
            print("e==>>", e)
            return c_time


def current_datetime():
    """
    get current datetime
    """
    # company_id = request.headers['apikey'] if 'apikey' in request.headers else None
    # if company_id:
    #     date = datetime.utcnow()
    #     timezone = get_company_tz(company_id)
    #     return convert_datetime_timezone(datetime_obj=date, old_tz="UTC", new_tz=timezone)

    return datetime.now()


# def get_company_tz(company_id):
#     """
#     get company timezone offset
#     :param company_id:
#     :return: str
#     """
#     result = "UTC"
#     company_data = get_from_redis(company_id)
#     if company_data:
#         # print('company_data from redis', company_data)
#         rr = json.loads(company_data)
#         if rr:
#             result = rr['timezone'] if rr['timezone'] else 'UTC'
#     else:
#         res = get_company_data(where_query={'company_id': company_id})
#         if res:
#             set_to_redis(company_id, json.dumps(res, default=str))
#             result = res['timezone'] if res['timezone'] else 'UTC'
#     return result


# def pms_dt_timezone(company_id):
#     """
#     get company timezone offset
#     :param company_id:
#     :return: str
#     """
#     result = "UTC"
#     company_data = get_from_redis(company_id)
#     if company_data:
#         # print('company_data from redis', company_data)
#         rr = json.loads(company_data)
#         if rr:
#             result = rr['timezone'] if rr['timezone'] else 'UTC'
#     else:
#         rr = company_queryset.get_data(where_condition={'company_id': company_id})
#         if rr:
#             set_to_redis(company_id, json.dumps(rr, default=str))
#             result = rr['timezone'] if rr['timezone'] else 'UTC'
#     return result


BASE_URL = os.environ.get("BASE_URL", "")


def get_company_data(where_query=None, select_column=None):
    if where_query is None:
        where_query = {}
    if select_column is None:
        select_column = []
    payload = {
        'where_query': where_query,
        'select_column': select_column,
        'method': 'GET'
    }
    url = f"{BASE_URL}/api/internal/company"
    res = post_request(url, payload)
    result = res.get('data') if res else None
    result = result[0] if result else None
    return result


def current_timestamp():
    return float(datetime.now().timestamp())


# def date_to_company_timezone_date(company_id, date):
#     if not date:
#         return None
#     company_timezone = get_company_tz(company_id)
#     new_timezone = pytz.timezone("UTC")
#     old_timezone = pytz.timezone(company_timezone)

#     rr = old_timezone.localize(date).astimezone(new_timezone).timestamp()
#     return int(rr)


def string_to_date(date):
    if date:
        # try:
        date = datetime.strptime(date, GET_DATE_FORMAT)
        # except ValueError:
        #     date = date
    return date


def date_string_to_date(date):
    if date:
        date = datetime.strptime(date, GET_DATE_FORMAT)
    return date


def date_to_timestamp(date):
    return int(date.timestamp())


def month_start_date_and_end_date(date_obj=None):
    if not date_obj:
        date_obj = datetime.now()

    _, num_days = calendar.monthrange(date_obj.year, date_obj.month)
    m_sd = datetime(date_obj.year, date_obj.month, 1)
    m_ed = datetime(date_obj.year, date_obj.month, num_days)

    return m_sd, m_ed


def date_string_to_datetime(date):
    try:
        date = datetime.strptime(date + " 00:00:00", DATE_TIME_FORMAT_2)
    except Exception as e:
        print("date_string_to_datetime error -->", e)
        date = None
    return date


def timestamp_for_today():
    today_utc = datetime.utcnow().date()

    # Convert to timestamp (seconds since epoch)
    timestamp = float(today_utc.strftime('%s'))

    return timestamp

def combine_date_and_time(date_timestamp, time_timestamp):
    # Convert both timestamps to datetime objects
    date_datetime = datetime.utcfromtimestamp(date_timestamp)
    time_datetime = datetime.utcfromtimestamp(time_timestamp)

    # Extract the date from the first datetime and the time from the second datetime
    date_part = date_datetime.date()
    time_part = time_datetime.time()

    # Combine the date and time into a new datetime object
    combined_datetime = datetime.combine(date_part, time_part)

    # Convert the combined datetime object back to a timestamp
    combined_timestamp = combined_datetime.timestamp()

    return combined_timestamp
