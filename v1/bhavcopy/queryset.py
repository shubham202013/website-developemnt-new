from database.helper import memsql
from v1.bhavcopy.models import Bhavcopy


def get_all_bhavcopy_data(where_query=dict(), select_column=[], offset=0, limit=0, order_by=[]):
    return memsql.get_all_data(model=Bhavcopy, where_query=where_query,
                               select_column=select_column, offset=offset,
                               limit=limit, order_by=order_by)



def delete_bhavcopy_data(where_condition):
    return memsql.delete_data(model=Bhavcopy, where_query=where_condition)


def insert_bhavcopy_bulk_data(data):
    return memsql.insert_many_data(data=data)

# def insert_bhavcopy_bulk_data(data):
#     return memsql.insert_bulk_data(model=Bhavcopy,data=data)

def insert_data(data):
    return memsql.insert_data(model=Bhavcopy,data=data)
