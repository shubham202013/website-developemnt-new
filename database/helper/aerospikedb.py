# import os
# import aerospike
#
# # from aerospike import predexp
# AEROSPIKE_HOST = str(os.environ.get("AEROSPIKE_HOST"))
# AEROSPIKE_PORT = int(os.environ.get("AEROSPIKE_PORT"))
#
# config = {
#     'hosts': [
#         (AEROSPIKE_HOST, AEROSPIKE_PORT)
#     ],
#     'policies': {
#         'timeout': 10000  # milliseconds
#     }
# }
# client = aerospike.client(config)
# client.connect()
#
#
# def insert_data(key, bins):
#     """
#     insert data
#     """
#     client = aerospike.client(config)
#     client.connect()
#
#     return client.put(key, bins)
#
#
# def get_data(key):
#     """
#     get data
#     """
#     client = aerospike.client(config)
#     client.connect()
#     try:
#         (key, meta, record) = client.get(key)
#     except:
#         record = {}
#
#     return record
#
#
# def delete_data(key):
#     """
#         delete_data
#     """
#     client = aerospike.client(config)
#     client.connect()
#
#     try:
#         client.remove(key)
#     except:
#         pass
#
#     return True
#
#
# def get_filter_data(namespace, set, keys):
#     client = aerospike.client(config)
#     client.connect()
#
#     keylist = []
#     for key in keys:
#         individualKey = (namespace, set, key)
#         keylist.append(individualKey)
#
#     data = client.get_many(keylist)
#
#     res = list()
#     for rr in data:
#         if rr[2]:
#             res.append(rr[2])
#     return res
#
#
# def get_geo_data_str(where_query, db_name, select_column=None):
#     from aerospike import predexp as predexp
#     client = aerospike.client(config)
#     client.connect()
#
#     query = client.query("test", db_name)
#     if select_column:
#         for i in select_column:
#             query.select(i)
#     predexps = list()
#     count = 0
#     for i in where_query.items():
#         if type(i[1]) == type(dict()):
#             in_query = list(i[1].values())
#             in_query = in_query[0]
#
#             for j in range(len(in_query)):
#                 predexps.append(predexp.string_bin(i[0]))
#                 predexps.append(predexp.string_value(in_query[j]))
#                 predexps.append(predexp.string_equal())
#                 count = count + 1
#         else:
#             predexps.append(predexp.string_bin(i[0]))
#             predexps.append(predexp.string_value(i[1]))
#             predexps.append(predexp.string_equal())
#     predexps.append(predexp.predexp_or(count))
#
#     query.predexp(predexps)
#
#     big_records = query.results()
#
#     res = list()
#     for rr in big_records:
#         if rr[2]:
#             res.append(rr[2])
#
#     return res
#
#
# def get_geo_data(where_query, db_name, select_column=None):
#     from aerospike import predexp as predexp
#     client = aerospike.client(config)
#     client.connect()
#     query = client.query('test', db_name)
#     if select_column:
#         for i in select_column:
#             query.select(i)
#
#     predexps = list()
#
#     count = 0
#     for i in where_query.items():
#         if type(i[1]) == type(dict()):
#             in_query = list(i[1].values())
#             in_query = in_query[0]
#
#             for j in range(len(in_query)):
#                 predexps.append(predexp.integer_bin(i[0]))
#                 predexps.append(predexp.integer_value(in_query[j]))
#                 predexps.append(predexp.integer_equal())
#                 count = count + 1
#         else:
#             predexps.append(predexp.integer_bin(i[0]))
#             predexps.append(predexp.integer_value(i[1]))
#             predexps.append(predexp.integer_equal())
#     predexps.append(predexp.predexp_or(count))
#     query.predexp(predexps)
#
#     big_records = query.results()
#
#     res = list()
#     for rr in big_records:
#         if rr[2]:
#             res.append(rr[2])
#
#     return res
