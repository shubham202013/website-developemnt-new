from sqlalchemy import desc, asc
from sqlalchemy import or_, and_
from sqlalchemy.orm import load_only

from database.db import mem_db


def get_data(model=None, where_query=None, select_column=None):
    """
    get data
    """
    query = mem_db.session.query(model)
    query = query_build(model, query, where_query)
    if select_column:
        query = query.options(load_only(*select_column))
    query = query.first()
    query = row2dict(query)
    return query


def get_all_data(model=None, where_query=None, select_column=None, offset=0, limit=0, order_by=None):
    """
    get all data
    """
    query = mem_db.session.query(model)
    query = query_build(model, query, where_query)
    if select_column:
        query = query.options(load_only(*select_column))
    _order_by = order_build(order_by)
    if limit:
        result = query.order_by(*_order_by).limit(limit).offset(offset)
    else:
        result = query.order_by(*_order_by).all()
    result = row2dict(result, many=True) if result else []
    return result


def get_count(model, where_query):
    """
    get count
    """
    query = mem_db.session.query(model)
    result = query_build(model, query, where_query).count()
    return result


def get_custom_count(model, where_query, count_field, group_by):
    """
    get count by aggregation
    out put will be like
    [(gopup_filed, count_total), ('6095205aceff13af08006a4a', 5), ('60824f3d00edf7d86cc91232', 1)]
    """
    from sqlalchemy import func
    _count_field = getattr(model, count_field)
    _group_by = getattr(model, group_by)
    query = mem_db.session.query(model)
    return query_build(model, query, where_query).with_entities(_group_by, func.count(count_field)).group_by(
        _group_by).all()


def insert_data(model, data):
    """
    Insert data
    """
    me = None
    try:
        me = model(**data)
        mem_db.session.add(me)
        mem_db.session.commit()
    except Exception as e:
        print(e)

    return me


def create_all():
    return mem_db.create_all()


def insert_many_data(data):
    """
        batch insert
        Ex.
            objects = [
                User(name="u1"),
                User(name="u2"),
                User(name="u3")
            ]
            s.bulk_save_objects(objects)
            s.commit()
        """
    mem_db.session.bulk_save_objects(data, return_defaults=True)
    mem_db.session.commit()
    return True


def insert_bulk_data(model, data):
    """
    it will create list of objects;
    """
    data_list = []
    for i in data:
        # print(i)
        try:
            d = insert_data(model, i)
            data_list.append(d)
        except Exception as e:
            print("insert_bulk_data error -->", e)
            print("not add --------  ", i)
    return data_list


def batch_insert_data(objects):
    """
    batch insert
    Ex.
        objects = [
            User(name="u1"),
            User(name="u2"),
            User(name="u3")
        ]
        s.bulk_save_objects(objects)
        s.commit()
    """
    mem_db.session.bulk_save_objects(objects, return_defaults=True)
    mem_db.session.commit()
    return True


def update_data(model=None, where_query=dict(), data=dict()):
    """
    Update data
    """
    query = mem_db.session.query(model)
    instance = query_build(model, query, where_query)
    res = instance.update(data, synchronize_session='fetch')
    mem_db.session.commit()
    return res


def delete_data(model, where_query):
    """
    delete data
    """
    query = mem_db.session.query(model)
    query_build(model, query, where_query).delete(synchronize_session=False)
    mem_db.session.commit()
    return True


def query_build(model, query, where_dict):
    """
    query builder
    """
    for key, value in where_dict.items():
        if type(value) == dict:
            if value.get('$in'):
                fld = getattr(model, key)
                in_list = value.get('$in')
                query = query.filter(fld.in_(in_list))
            if value.get('$eq'):
                fld = getattr(model, key)
                eq_list = value.get('$eq')
                query = query.filter(fld.contains(eq_list))
            if value.get('$nin'):
                fld = getattr(model, key)
                nin_list = value.get('$nin')
                query = query.filter(~fld.in_(nin_list))
            if value.get('$ne') or '$ne' in value.keys():
                fld = getattr(model, key)
                not_value = value.get('$ne')
                query = query.filter(fld != not_value)
            if '$lt' in value.keys():
                fld = getattr(model, key)
                le_value = value.get('$lt')
                query = query.filter(fld < le_value)
            if '$lte' in value.keys():
                fld = getattr(model, key)
                lte_value = value.get('$lte')
                query = query.filter(fld <= lte_value)
            if '$gte' in value.keys():
                fld = getattr(model, key)
                gte_value = value.get('$gte')
                query = query.filter(fld >= gte_value)
            if key == "$or":
                or_dict = value
                or_parse = list()
                for ok, ov in or_dict.items():
                    if ok == '$and':
                        for o in ov:
                            if type(o) == dict:
                                o_parse = list()
                                for o_field, o_value in o.items():
                                    print("o_value", o_value)
                                    o_field = getattr(model, o_field)
                                    if type(o_value) == dict:
                                        if o_value.get('$in', None):
                                            in_list = o_value.get('$in')
                                            o_parse.append(o_field.in_(in_list))
                                    else:
                                        o_parse.append(o_field == o_value)
                                or_parse.append(and_(*o_parse))
                    else:
                        ok_fld = getattr(model, ok)
                        if type(ov) == dict:
                            if ov.get('$in', None):
                                in_list = ov.get('$in')
                                or_parse.append(ok_fld.in_(in_list))
                            if ov.get('$eq'):
                                in_list = ov.get('$eq')
                                or_parse.append(ok_fld.contains(in_list))
                            if '$lte' in ov.keys() and '$gte' in ov.keys():
                                lte_value = ov.get('$lte')
                                gte_value = ov.get('$gte')
                                o_parse = list()
                                o_parse.append(ok_fld <= lte_value)
                                o_parse.append(ok_fld >= gte_value)
                                or_parse.append(and_(*o_parse))
                            else:
                                if '$lte' in ov.keys():
                                    lte_value = ov.get('$lte')
                                    or_parse.append(ok_fld <= lte_value)
                                if '$gte' in ov.keys():
                                    lte_value = ov.get('$gte')
                                    or_parse.append(ok_fld >= lte_value)
                        else:
                            or_parse.append(ok_fld == ov)
                query = query.filter(or_(*or_parse))
            if "_search" in key:
                search_dict = value
                search_parse = list()

                for ok, ov in search_dict.items():
                    ok_fld = getattr(model, ok)
                    search_parse.append(ok_fld.contains(ov))

                query = query.filter(or_(*search_parse))
        else:
            if "_search" in key:
                key = key.replace("_search", "")
                fld = getattr(model, key)
                query = query.filter(fld.contains(value))

            # for multiple search from a string
            # eg. key = 'val1,val2,val3'
            # Now I need to filter like this val1,val2
            if "_msearch" in key:
                key = key.replace("_msearch", "")
                fld = getattr(model, key)
                value_list = value.split(',')
                query = query.filter(or_(*[fld.like(f"%{i}%") for i in value_list]))

            elif "_filter" in key:
                key = key.replace("_filter", "")
                fld = getattr(model, key)
                query = query.filter(fld == value)
            elif key == "$or":
                or_dict = value
                or_parse = list()
                for ok, ov in or_dict.items():
                    ok_fld = getattr(model, ok)
                    if type(ov) == dict:
                        if ov.get('$in', None):
                            in_list = ov.get('$in')
                            or_parse.append(ok_fld.in_(in_list))
                    else:
                        or_parse.append(ok_fld == ov)
                query = query.filter(and_(*or_parse))
            else:
                fld = getattr(model, key)
                query = query.filter(fld == value)

    # print('query------------->', query)
    return query


def generate_key(model, key):
    """
    generate key
    refrence
    # https://stackoverflow.com/questions/31804378/how-to-query-on-a-json-type-field-with-sqlalchemy
    # https://stackoverflow.com/questions/29974143/python-sqlalchemy-and-postgres-how-to-query-a-json-element
    """
    if '.' in key:
        if len(key.split('.')) == 2:
            rr = key.split('.')
            key = rr[0]
            fld = getattr(model, key)
            return fld.sub_key
        return key
    else:
        return key


def order_build(order_list):
    """
    query order builder
    """
    result = []
    if order_list:
        for i in order_list:
            if type(i) == list:
                if len(i) == 2:
                    if i[1] == 'desc':
                        result.append(desc(i[0]))
                    else:
                        result.append(asc(i[0]))
                elif len(i) == 1:
                    result.append(asc(i[0]))
            else:
                result.append(asc(i))
    return result


def row2dict(row, many=False):
    """
    convert raw to dict
    """
    if not row:
        return None

    if many:
        result = list()
        for i in row:
            rr = i.__dict__
            if '_sa_instance_state' in (rr.keys()):
                del rr['_sa_instance_state']
            result.append(rr)
    else:
        result = dict(row.__dict__)
        if '_sa_instance_state' in (result.keys()):
            del result['_sa_instance_state']
    return result


def get_aggregate_data_v2(model, where_query, group_by, limit=None):
    """
    get count by aggregation
    out put will be like
    [(gopup_filed, count_total), ('6095205aceff13af08006a4a', 5), ('60824f3d00edf7d86cc91232', 1)]
    """
    query = mem_db.session.query(model)

    if limit:
        return query_build(model, query, where_query).group_by(group_by).limit(limit)
    return query_build(model, query, where_query).group_by(group_by).all()
