# from flask import request
# from mongoengine import Q


# def get_data(model=None, where_query=None, select_column={}):
#     """
#     get data
#     """
#     _query = query_build(where_query)
#     if select_column:
#         result = model.objects.filter(_query).only(*select_column).first()
#     else:
#         result = model.objects.filter(_query).first()
#     result = row2dict(result, many=False)
#     return result


# def get_all_data(model=None, where_query=None, select_column=None, offset=0, limit=0, order_by=None):
#     """
#     get all data
#     """
#     _query = query_build(where_query)
#     if not select_column:
#         select_column = []

#     page_size = limit
#     current_page = request.args.get('page', '1')
#     current_page = int(current_page) if current_page.isdigit() else 1
#     limit = page_size * current_page
#     order_by = sort_build(order_by)
#     if limit:
#         result = model.objects.filter(_query).only(*select_column).order_by(*order_by)[offset:limit]
#     else:
#         result = model.objects.filter(_query).only(*select_column).order_by(*order_by)
#     result = row2dict(result, many=True)
#     return result


# def get_count(model, where_query):
#     """
#     get count
#     """
#     _query = query_build(where_query)
#     return model.objects.filter(_query).count()


# def insert_data(model, data):
#     """
#     insert data
#     """
#     result = model.objects.create(**data)
#     result = row2dict(result, many=False)
#     return result


# def insert_bulk_data(model, data):
#     """
#     insert data
#     """
#     for d in data:
#         model.objects.create(**d)
#     return True


# def insert_many_data(model, data):
#     """
#         for in docker usage
#         insert many data
#     """
#     result = model.objects.insert(data)
#     return result


# def update_data(model=None, where_query=None, data=None):
#     """
#     Update data
#     """
#     _query = query_build(where_query)
#     result = model.objects.filter(_query).update(**data)
#     return result


# def delete_data(model, where_query):
#     """
#     Delete data
#     """
#     _query = query_build(where_query)
#     model.objects.filter(_query).delete()
#     return True


# def raw_query(model=None, query=None, many=False):
#     """
#     fire raw query using model
#     """
#     if many:
#         result = model.objects(__raw__=query)
#         result = row2dict(result, many=True)
#     else:
#         # print('query', query)
#         result = model.objects(__raw__=query).first()
#         result = row2dict(result, many=False)
#     return result


# def get_aggregate_data(model=None, where_query={}, select_column=None, aggregate_condition={}):
#     """
#     get aggregate data
#     """
#     obj = model.objects.filter(where_query)
#     if select_column:
#         obj = obj.only(*select_column)
#     if aggregate_condition:
#         obj = obj.aggregate(aggregate_condition)
#     return obj


# def get_aggregate_data_v2(model=None, where_query={},  aggregate_condition={}):
#     """
#     get aggregate data
#     """
#     _query = query_build(where_query)
#     obj = model.objects.aggregate(aggregate_condition)

#     return obj


# def query_build(where_query):
#     """
#     query builder
#     """
#     _query = Q()
#     _search = Q()
#     _filter = Q()
#     _or_query = Q()
#     for key, value in where_query.items():
#         if type(value) == dict:
#             if value.get('$in'):
#                 in_list = value.get('$in')
#                 _query &= eval("Q({0}__in={1})".format(key, in_list))
#             if value.get('$ne'):
#                 ne_value = value.get('$ne')
#                 _query &= eval("Q({0}__ne='{1}')".format(key, ne_value))
#             if value.get('$nin'):
#                 in_list = value.get('$nin')
#                 _query &= eval("Q({0}__nin={1})".format(key, in_list))
#             if key == "$or":
#                 or_dict = value
#                 for ok, ov in or_dict.items():
#                     _or_query |= Q(**{format(ok): ov})
#             if '$lt' in value.keys():
#                 lt_value = value.get('$lt')
#                 _query &= eval("Q({0}__lt='{1}')".format(key, lt_value))
#             if '$gt' in value.keys():
#                 gt_value = value.get('$gt')
#                 _query &= eval("Q({0}__gt='{1}')".format(key, gt_value))
#             if '$gte' in value.keys():
#                 gte_value = value.get('$gte')
#                 _query &= eval("Q({0}__gte='{1}')".format(key, gte_value))
#             if '$lte' in value.keys():
#                 lte_value = value.get('$lte')
#                 _query &= eval("Q({0}__lte='{1}')".format(key, lte_value))
#         else:
#             if "_search" in key:
#                 key = key.replace("_search", "")
#                 _search = _search | Q(**{"{0}__icontains".format(key): value})
#             elif "_filter" in key:
#                 key = key.replace("_filter", "")
#                 _filter = _filter | Q(**{format(key): value})
#             elif key == "$or":
#                 for or_k, or_v in value.items():
#                     _filter = _filter | Q(**{format(or_k): or_v})
#             else:
#                 _query &= Q(**{key: value})
#     _query &= _search
#     _query &= _filter
#     _query &= _or_query
#     return _query


# def sort_build(sort_data=None):
#     """
#     query sort builder
#     """
#     if not sort_data:
#         sort_data = []
#     query = list()
#     for i in sort_data:
#         if len(i) == 2:
#             if i[1] == 'desc':
#                 query.append("-{0}".format(i[0]))
#             else:
#                 query.append(i[0])
#         else:
#             query.append(i[0])

#     return query


# def row2dict(row, many=False):
#     """
#     convert raw to dict
#     """
#     if not row:
#         return dict()
#     if many:
#         result = list()
#         for i in row:
#             rr = i.to_mongo().to_dict()
#             rr['id'] = rr['_id']
#             del rr['_id']
#             result.append(rr)
#     else:
#         result = row.to_mongo().to_dict()
#         result['id'] = result['_id']
#         del result['_id']
#     return result
