from typing import Optional

from common.password import generate_password
from database.helper import memsql
from v1.users.models import User, Token, UserWallet


def make_password(
        password: Optional[str], salt: Optional[str] = ..., hasher: str = ...
) -> str: ...


def insert_data(data):
    if data.get("password"):
        data['password'] = generate_password(data.get("password"))
    print("data --------------------     ", data)
    return memsql.insert_data(User, data)


def update_data(where_condition, data):
    return memsql.update_data(User, where_condition, data)


def delete_data(where_condition):
    return memsql.delete_data(model=User, where_query=where_condition)


def get_count(where_query):
    return memsql.get_count(model=User, where_query=where_query)


def get_data(where_condition, select_column=[]):
    return memsql.get_data(model=User, where_query=where_condition, select_column=select_column)


def get_all_data(where_query=dict(), select_column=[], offset=0, limit=0, order_by=[]):
    return memsql.get_all_data(model=User, where_query=where_query,
                               select_column=select_column, offset=offset,
                               limit=limit, order_by=order_by)


# TOKEN

def insert_token(data):
    return memsql.insert_data(Token, data)


def update_token(where_condition, data):
    return memsql.update_data(Token, where_condition, data)


def delete_token(where_condition):
    return memsql.delete_data(model=Token, where_query=where_condition)


def get_count_token(where_query):
    return memsql.get_count(model=Token, where_query=where_query)


def get_token(where_condition, select_column=[]):
    return memsql.get_data(model=Token, where_query=where_condition, select_column=select_column)


def get_all_token(where_query=dict(), select_column=[], offset=0, limit=0, order_by=[]):
    return memsql.get_all_data(model=Token, where_query=where_query,
                               select_column=select_column, offset=offset,
                               limit=limit, order_by=order_by)

def get_user_det(user_id_list):
    user_objects = get_all_data(where_query={"user_id": {"$in": user_id_list}},
                                select_column=['user_id', "full_name", "phone_number", "dial_code",
                                               "email", "date_of_birth", "role_id", "image",
                                               "is_superuser", "timezone","date_format"])
    # print('user',user_objects)
    user_det = {i['user_id']: i for i in user_objects}

    return user_det


def get_user_det_by_email(email_id_list, field):
    user_objects = get_all_data(where_query={field: {"$in": email_id_list}},
                                select_column=['user_id', "full_name", "phone_number", "dial_code",
                                               "email", "date_of_birth", "role_id", "image",
                                               "is_superuser"])
    # print('user',user_objects)
    user_det = {i[field]: i for i in user_objects}

    return user_det


def active_get_user_det(user_id_list):
    user_objects = get_all_data(where_query={"user_id": {"$in": user_id_list}, 'is_active': True},
                                select_column=['user_id', "full_name", "phone_number", "dial_code",
                                               "email", "date_of_birth", "role_id", "image",
                                               "is_superuser"])
    # print('user',user_objects)
    user_det = {i['user_id']: i for i in user_objects}

    return user_det


def get_user_object(where_query):
    user_object = get_data(where_condition=where_query)

    user_dict = {
        "user_id": user_object.get('user_id'),
        "full_name": user_object.get('full_name'),
        "phone_number": user_object.get('phone_number'),
        "dial_code": user_object.get('dial_code'),
        "email": user_object.get('email'),
        "image": user_object.get('image'),
        "is_superuser": user_object.get('is_superuser')
    } if user_object else {}
    return user_dict



# User Wallet

def insert_user_wallet(data):
    return memsql.insert_data(UserWallet, data)


def update_user_wallet(where_condition, data):
    return memsql.update_data(UserWallet, where_condition, data)


def delete_user_wallet(where_condition):
    return memsql.delete_data(model=UserWallet, where_query=where_condition)


def get_count_user_wallet(where_query):
    return memsql.get_count(model=UserWallet, where_query=where_query)


def get_user_wallet(where_condition, select_column=[]):
    return memsql.get_data(model=UserWallet, where_query=where_condition, select_column=select_column)


def get_all_user_wallet(where_query=dict(), select_column=[], offset=0, limit=0, order_by=[]):
    return memsql.get_all_data(model=UserWallet, where_query=where_query,
                               select_column=select_column, offset=offset,
                               limit=limit, order_by=order_by)