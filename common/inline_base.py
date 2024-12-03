import json

from flask import request
from flask_apispec import MethodResource

from common.utils import internal_success_response


def json_loads_data(data):
    try:
        data = json.loads(data)
    except Exception as e:
        print("json_loads_data error -->", e)
    return data


class InlineBaseResource(MethodResource):
    """
    inline base get data
    """

    model = None
    db_helper = None
    data_label = 'data'
    get_response_schema = None

    def post(self):
        """
        create new data
        """
        json_data = request.form or request.get_json()
        print('json_data >>>', json_data)
        try:
            json_data = json_loads_data(json_data)
        except Exception as e:
            print("InlineBaseResource error -->", e)
        _method = json_data.get('method')
        data = json_data.get('data', None)
        select_column = json_data.get('select_column', None)
        do_serialize = json_data.get('do_serialize', False)
        where_query = json_data.get('where_query', None)
        order_by = json_data.get('order_by', None)
        bulk = json_data.get('bulk', False)
        aggregate = json_data.get('aggregate', False)
        pipeline = json_data.get('pipeline', None)
        offset = json_data.get('offset', 0)
        limit = json_data.get('limit', 0)

        if do_serialize and data:
            try:
                data = json.loads(data)
            except Exception as e:
                print('do_serialize decode error', e)

        result = None
        if _method == 'GET':
            if aggregate:
                result = self.db_helper.get_aggregate_data(self.model, aggregate_condition=pipeline)
                result = [r for r in result]
            else:
                result = self.db_helper.get_all_data(self.model, where_query=where_query, order_by=order_by,
                                                     offset=offset, limit=limit, select_column=select_column)

            if self.get_response_schema:
                result = self.get_response_schema().dump(result, many=True)

        elif _method == 'POST':
            if bulk:
                result = self.db_helper.insert_bulk_data(self.model, data)
            else:
                result = self.db_helper.insert_data(self.model, data)

            if self.get_response_schema:
                if bulk:
                    result = self.get_response_schema().dump(result, many=True)
                else:
                    result = self.get_response_schema().dump(result)
            else:
                result = {"id": result.id}
        elif _method == 'PUT':
            result = self.db_helper.update_data(self.model, where_query, data)
        elif _method == 'DELETE':
            result = self.db_helper.delete_data(self.model, where_query)
        elif _method == 'COUNT':
            result = self.db_helper.get_count(self.model, where_query)

        return internal_success_response(data=result)
