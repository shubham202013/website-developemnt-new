from database.helper import memsql
from v1.etf_plantation.models import ETFPlantationSymbols

def insert_etf_plantation_symbols_data(data):
    return memsql.insert_data(ETFPlantationSymbols, data)

def insert_etf_plantation_symbols_bulk_data(data):
    return memsql.insert_many_data(data=data)


def update_etf_plantation_symbols_data(where_condition, data):
    return memsql.update_data(ETFPlantationSymbols, where_condition, data)


def delete_etf_plantation_symbols_data(where_condition):
    return memsql.delete_data(model=ETFPlantationSymbols, where_query=where_condition)


def get_etf_plantation_symbols_count(where_query):
    return memsql.get_count(model=ETFPlantationSymbols, where_query=where_query)


def get_etf_plantation_symbols_data(where_condition, select_column=[]):
    return memsql.get_data(model=ETFPlantationSymbols, where_query=where_condition, select_column=select_column)


def get_all_etf_plantation_symbols_data(where_query=dict(), select_column=[], offset=0, limit=0, order_by=[]):
    return memsql.get_all_data(model=ETFPlantationSymbols, where_query=where_query,
                               select_column=select_column, offset=offset,
                               limit=limit, order_by=order_by)

