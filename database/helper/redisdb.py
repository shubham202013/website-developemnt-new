# import os
# import redis
# import datetime
# import json

# # redis
# from common.base import p_print

# REDIS_HOST = os.environ.get("REDIS_HOST", None)
# REDIS_PORT = os.environ.get("REDIS_PORT", None)

# r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


# def datetime_handler(x):
#     if isinstance(x, datetime.datetime):
#         return x.isoformat()
#     raise TypeError("Unknown type")


# def get_all_data(name):
#     """
#     get all data
#     """
#     result = r.hgetall(name=name)

#     # key decode
#     result = {key.decode('utf-8'): value for key, value in result.items()}

#     # value decode and dumps
#     result = [json.loads(value.decode('utf-8')) for key, value in result.items()]

#     return result


# def insert_data(name, key, value):
#     """
#         insert data
#     """
#     result = r.hset(name=name, key=key, value=value)

#     return result


# def update_data(name, key, value):
#     """
#         update data
#     """
#     data = json.dumps(value, default=datetime_handler)
#     result = r.hset(name=name, key=key, value=data)

#     return result


# def get_filter_data(name, keys):
#     """
#     get filter data
#     :only filter by keys
#     """
#     data_list = list()

#     result = r.hmget(name=name, keys=keys)
#     for d in result:
#         data_list.append(json.loads(d.decode('utf-8')))

#     return data_list


# def get_data(name, key):
#     """
#     get data
#     """
#     result = r.hget(name=name, key=key)
#     result = result.decode("utf-8")

#     return result


# def delete_data(name, key):
#     """
#         delete data
#     """
#     result = r.hdel(name, *[key])

#     return result
