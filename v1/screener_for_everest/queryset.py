from database.helper import memsql
from v1.screener_for_everest.models import ScreenerForEverest

def insert_screener_for_everest_data(data):
    return memsql.insert_data(ScreenerForEverest, data)

def insert_screener_for_everest_bulk_data(data):
    return memsql.insert_many_data(data=data)


def update_screener_for_everest_data(where_condition, data):
    return memsql.update_data(ScreenerForEverest, where_condition, data)


def delete_screener_for_everest_data(where_condition):
    return memsql.delete_data(model=ScreenerForEverest, where_query=where_condition)


def get_screener_for_everest_count(where_query):
    return memsql.get_count(model=ScreenerForEverest, where_query=where_query)


def get_screener_for_everest_data(where_condition, select_column=[]):
    return memsql.get_data(model=ScreenerForEverest, where_query=where_condition, select_column=select_column)


def get_all_screener_for_everest_data(where_query=dict(), select_column=[], offset=0, limit=0, order_by=[]):
    return memsql.get_all_data(model=ScreenerForEverest, where_query=where_query,
                               select_column=select_column, offset=offset,
                               limit=limit, order_by=order_by)
