# import uuid

# from database.db import es_db


# def get_data(model=None, query_dict=None, select_column=None, order_by=None):
#     """
#     get data using model and query
#     "sort" : [
#                 {"price" : {"order" : "asc"}}
#              ]
#     """
#     must_list, must_not_list, should_list = query_build(where_query=query_dict)
#     body = {
#         "query": {
#             "bool": {
#                 "must": must_list,
#                 "must_not": must_not_list,
#                 "should": should_list,
#             },
#         }
#     }
#     if select_column:
#         body["_source"] = select_column

#     if order_by:
#         body["sort"] = order_by

#     res_ins = es_db.search(index=model, request_timeout=90, ignore=[404], doc_type='_doc', body=body)
#     res_ins_list = res_ins.get('hits', dict()).get('hits', list())
#     result = res_ins_list[0] if res_ins_list else dict()
#     return result


# def get_all_data(model=None, where_query=None, select_column=None, offset=0, limit=0, order_by=None):
#     """
#     get all data
#     """
#     must_list, must_not_list, should_list, = query_build(where_query=where_query)
#     body = {
#         "query": {
#             "bool": {
#                 "must": must_list,
#                 "must_not": must_not_list,
#                 "should": should_list,
#             },
#         }
#     }

#     if limit == 0:
#         res_count = es_db.count(index=model, request_timeout=90, ignore=[404], doc_type='_doc', body=body)
#         limit = res_count.get('count', 0) if res_count else 0

#     if select_column:
#         body["_source"] = select_column
#     if order_by:
#         body["sort"] = order_by
#         """
#         "sort" : [
#                     {"price" : {"order" : "asc"}}
#                  ]
#         """
#     res_ins = es_db.search(index=model, request_timeout=90, ignore=[404], size=limit, from_=offset,
#                            doc_type='_doc',
#                            body=body)
#     res_ins_list = res_ins.get('hits', dict()).get('hits', list())
#     result = [i['_source'] for i in res_ins_list] if res_ins_list else []
#     return result


# def get_count(model, where_query=dict()):
#     """
#     get count
#     """
#     must_list, must_not_list, should_list = query_build(where_query=where_query)
#     body = {
#         "query": {
#             "bool": {
#                 "must": must_list,
#                 "must_not": must_not_list,
#                 "should": should_list,
#             },
#         }
#     }
#     res_count = es_db.count(index=model, request_timeout=90, ignore=[404], doc_type='_doc', body=body)
#     return res_count.get('count', 0) if res_count else 0


# def insert_data(model, data):
#     """
#     insert data
#     """
#     print('insert_data model', model)
#     print('insert_data data', data)
#     es_db.index(
#         index=model,
#         doc_type='_doc',
#         id=uuid.uuid4(),
#         body=data,
#         refresh=True,
#     )
#     result = None
#     return result


# def insert_bulk_data():
#     """
#     insert data
#     """
#     return True


# def update_data(model=None, query_dict=dict(), data=dict()):
#     """
#     Update data
#     """
#     res_obj = get_data(model, query_dict)
#     result = dict()
#     if res_obj:
#         es_db.update(
#             index=model,
#             doc_type='_doc',
#             id=res_obj['_id'],
#             refresh=True,
#             body={'doc': data}
#         )
#         res_obj = get_data(model, query_dict)
#         result = res_obj['_source'] if res_obj else {}
#     return result


# def update_all_data(model=None, query_dict=dict(), data=dict()):
#     """
#     Update all data
#     """
#     must_list, must_not_list, should_list, = query_build(where_query=query_dict)
#     body = {
#         "query": {
#             "bool": {
#                 "must": must_list,
#                 "must_not": must_not_list,
#                 "should": should_list,
#             },
#         }
#     }

#     res_count = es_db.count(index=model, request_timeout=90, ignore=[404], doc_type='_doc', body=body)
#     limit = res_count.get('count', 0) if res_count else 0

#     res_ins = es_db.search(index=model, request_timeout=90, ignore=[404], size=limit, from_=0,
#                            doc_type='_doc',
#                            body=body)
#     res_ins_list = res_ins.get('hits', dict()).get('hits', list())

#     for res_obj in res_ins_list:
#         es_db.update(
#             index=model,
#             doc_type='_doc',
#             id=res_obj['_id'],
#             refresh=True,
#             body={'doc': data}
#         )
#     return []


# def delete_data(model, where_query=dict()):
#     """
#     delete data
#     """
#     res_obj = get_data(model, where_query)
#     if res_obj:
#         es_db.delete(
#             index=model,
#             doc_type='_doc',
#             refresh=True,
#             id=res_obj['_id'],
#         )

#     return True


# def create_index_mapping(model):
#     """
#     create mappings
#     """
#     index = model
#     mappings = model['mappings']
#     if not es_db.indices.exists(index=index):
#         settings = {
#             "mappings": {
#                 "properties": mappings
#             }
#         }
#         es_db.indices.create(index=index, ignore=400, body=settings)
#     return True


# def get_all_raw_query(model, body, offset, limit=0, order_by=None):
#     """
#     get raw query
#     Ex.
#     body = {
#         "query": {
#             "bool": {
#                 "must": must_list,
#                 "must_not": must_not_list,
#                 "should": should_list,
#             },
#         }
#     }
#     """

#     if order_by:
#         body["sort"] = order_by

#     if limit > 0:
#         _limit = limit
#     else:
#         res_count = es_db.count(index=model, request_timeout=90, ignore=[404], doc_type='_doc', body=body)
#         _limit = res_count.get('count', 0) if res_count else 0

#     res_ins = es_db.search(index=model, request_timeout=90, ignore=[404], size=_limit, from_=offset,
#                            doc_type='_doc',
#                            body=body)
#     result = res_ins.get('hits', dict()).get('hits', list())
#     return result


# def get_only_raw_query(model, body, limit=0):
#     """
#     get using only raw query
#     """
#     if limit:
#         res_ins = es_db.search(index=model, request_timeout=90, ignore=[404],
#                                doc_type='_doc', size=limit,
#                                body=body)
#     else:
#         res_ins = es_db.search(index=model, request_timeout=90, ignore=[404],
#                                doc_type='_doc', body=body, size=0)
#     result = res_ins
#     return result


# def get_count_raw_query(model, body):
#     """
#     get count by raw query
#     """
#     res_count = es_db.count(index=model, request_timeout=90, ignore=[404], doc_type='_doc', body=body)
#     result = res_count.get('count', 0) if res_count else 0
#     return result


# def query_build(where_query):
#     """
#     elasticsearch query builder
#     """
#     must_list = []
#     must_not_list = []
#     should_list = []
#     for key, value in where_query.items():
#         if type(value) == dict:
#             if value.get('$in'):
#                 in_list = value.get('$in')
#                 must_list.append({"terms": {key: in_list}})
#             if value.get('$ne'):
#                 ne_value = value.get('$ne')
#                 must_not_list.append({"term": {key: ne_value}})
#             if value.get('$nin'):
#                 in_list = value.get('$nin')
#                 must_not_list.append({"terms": {key: in_list}})
#             if value.get('$lte') and value.get('$lte'):
#                 date_filter = {
#                     "bool": {
#                         "should": [
#                             {
#                                 "range": {
#                                     key: {
#                                         "gte": value.get('$gte'),
#                                         "lte": value.get('$lte')
#                                     }
#                                 }
#                             }
#                         ]
#                     }
#                 }
#                 must_list.append(date_filter)
#         else:
#             if "_search" in key:
#                 key = key.replace("_search", "")
#                 must_list.append({"match_phrase_prefix": {key: {"query": value}}})
#             elif "_filter" in key:
#                 key = key.replace("_filter", "")
#                 must_list.append({"term": {key: value}})
#             else:
#                 must_list.append({"term": {key: value}})

#     return must_list, must_not_list, should_list
