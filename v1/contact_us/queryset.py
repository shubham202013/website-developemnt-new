from typing import Optional

from common.password import generate_password
from database.helper import memsql
from v1.contact_us.models import ContactUs


def insert_data(data):
    return memsql.insert_data(ContactUs, data)


def update_data(where_condition, data):
    return memsql.update_data(ContactUs, where_condition, data)


def delete_data(where_condition):
    return memsql.delete_data(model=ContactUs, where_query=where_condition)


def get_count(where_query):
    return memsql.get_count(model=ContactUs, where_query=where_query)


def get_data(where_condition, select_column=[]):
    return memsql.get_data(model=ContactUs, where_query=where_condition, select_column=select_column)


def get_all_data(where_query=dict(), select_column=[], offset=0, limit=0, order_by=[]):
    return memsql.get_all_data(model=ContactUs, where_query=where_query,
                               select_column=select_column, offset=offset,
                               limit=limit, order_by=order_by)

