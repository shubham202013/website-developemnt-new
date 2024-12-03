# """'
# Redis operation
# '"""

# from database.db import redis_db


# def delete_to_redis(key):
#     """
#     delete value to redis
#     """
#     print('set_to_redis key', key)
#     try:
#         redis_db.delete(key)
#         return True
#     except Exception as e:
#         print('set_to_redis e', e)
#         return 0


# def set_to_redis(key, value):
#     """
#     set value to redis
#     """
#     print('set_to_redis key', key)
#     print('set_to_redis value', value)
#     try:
#         redis_db.set(key, value)
#         return True
#     except Exception as e:
#         print('set_to_redis e', e)
#         return 0


# def get_data(key, field):
#     try:
#         data = redis_db.hget(key, field)
#         return data
#     except Exception as e:
#         print("get error", e)
#         return None


# def get_from_redis(key):
#     """
#     get value from redis
#     """
#     try:
#         return redis_db.get(key)
#     except Exception as e:
#         print('get_from_redis e', e)
#         return 0


# import json


# def get_all_data(name):
#     """
#     get all data
#     """
#     result = redis_db.hgetall(name=name)
#     result = [json.loads(value) for key, value in result.items()]

#     return result


# def set_data(key, field, value):
#     try:
#         print('set redis')
#         redis_db.hset(key, field, json.dumps(value))
#         # print("get_data(key, field) -------------------  ",get_data(key, field))
#         return True
#     except Exception as e:
#         print("get error", e)
#         return None


# def remove_data(key, field):
#     try:
#         data = redis_db.hdel(key, field)
#         # print('delete ----------------  ', data)
#     except Exception as e:
#         print("del error", e)
#         data = None
#     return data


# def set_data_multipledata(key, field=None, data=None):
#     if field == None:
#         field = "id"
#     for obj in data:
#         set_data(key, obj.get(field), obj)
