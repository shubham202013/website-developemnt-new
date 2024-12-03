from database.helper import memsql
from v1.referral.models import Referral

def insert_referral_data(data):
    return memsql.insert_data(Referral, data)


def update_referral_data(where_condition, data):
    return memsql.update_data(Referral, where_condition, data)


def delete_referral_data(where_condition):
    return memsql.delete_data(model=Referral, where_query=where_condition)


def get_referral_count(where_query):
    return memsql.get_count(model=Referral, where_query=where_query)


def get_referral_data(where_condition, select_column=[]):
    return memsql.get_data(model=Referral, where_query=where_condition, select_column=select_column)


def get_all_referral_data(where_query=dict(), select_column=[], offset=0, limit=0, order_by=[]):
    return memsql.get_all_data(model=Referral, where_query=where_query,
                               select_column=select_column, offset=offset,
                               limit=limit, order_by=order_by)

