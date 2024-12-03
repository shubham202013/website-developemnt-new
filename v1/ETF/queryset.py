from database.helper import memsql
from v1.ETF.models import ETFSymbols

def insert_etfSymbols_data(data):
    return memsql.insert_data(ETFSymbols, data)

def insert_etfSymbols_bulk_data(data):
    return memsql.insert_many_data(data=data)


def update_etfSymbols_data(where_condition, data):
    return memsql.update_data(ETFSymbols, where_condition, data)


def delete_etfSymbols_data(where_condition):
    return memsql.delete_data(model=ETFSymbols, where_query=where_condition)


def get_etfSymbols_count(where_query):
    return memsql.get_count(model=ETFSymbols, where_query=where_query)


def get_etfSymbols_data(where_condition, select_column=[]):
    return memsql.get_data(model=ETFSymbols, where_query=where_condition, select_column=select_column)


def get_all_etfSymbols_data(where_query=dict(), select_column=[], offset=0, limit=0, order_by=[]):
    return memsql.get_all_data(model=ETFSymbols, where_query=where_query,
                               select_column=select_column, offset=offset,
                               limit=limit, order_by=order_by)

