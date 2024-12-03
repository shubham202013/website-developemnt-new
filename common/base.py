import datetime
import os

# import barcode
from flask import request
from flask_apispec import MethodResource, marshal_with, use_kwargs, Ref, doc

from api_doc.templates.__common import DeleteResponseSchema, NoSchema, CommonResponseSchema
from common.config import get_page_size
from common.messages import api_message
from common.utils import success_response, error_response, get_filter_query, get_search_query
from common.website_datetime import current_datetime, current_timestamp
from config.authentication import current_identity, get_api_key

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S3_PUBLIC_URL = os.environ.get("S3_PUBLIC_URL", "")
# EAN = barcode.get_barcode_class('ean13')


class BaseListResource(MethodResource):
    """
    Get all data and create new data
    """

    model = None
    get_all_data = None
    count_data = None
    sort_by = []
    apply_pagination = True

    search_fields = None
    is_active = False
    filter_fields = None
    order_by = {}
    data_label = 'data'
    name = None
    check_is_deleted = False
    created_date = False
    manager_filter_field = None

    # api doc
    doc_tags = []
    get_description = ""
    post_description = ""
    get_request_schema = NoSchema
    get_response_schema = None
    post_request_schema = NoSchema
    post_response_schema = CommonResponseSchema

    def redis_pagination_list(self, data, company_id):
        import math
        page_size = get_page_size()
        page_size = int(request.args.get('size', page_size))
        current_page = request.args.get('page', '1')
        current_page = int(current_page) if current_page.isdigit() else 1
        limit = page_size * current_page
        print("page_size ------------   ", page_size)
        print("current_page ------------   ", current_page)
        offset = limit - page_size
        if offset < 0:
            offset = 0
        if offset == 0 and current_page == 0:
            limit = None
        all_data = data[offset:limit]
        if int(current_page) == 0:
            all_data = data
        data_count = len(data)

        total_pages = math.ceil(data_count / page_size)

        pagination_data = dict()
        pagination_data['has_previous'] = True if (total_pages and current_page) > 1 else False
        pagination_data['has_next'] = True if (total_pages and current_page) < total_pages else False
        pagination_data['total_page'] = total_pages
        pagination_data['current_pages'] = current_page
        pagination_data['count'] = data_count

        # if self.get_response_schema:
        # all_data = self.get_response_schema().dump(all_data, many=True)

        data = {
            self.data_label: all_data if all_data else [],
            'pagination': pagination_data
        }
        return data

    def pagination_list(self, where_query):
        import math
        page_size = get_page_size()
        page_size = int(request.args.get('size', page_size))
        current_page = request.args.get('page', '1')
        current_page = int(current_page) if current_page.isdigit() else 1
        limit = page_size * current_page
        offset = limit - page_size
        offset = 0 if offset < 0 else offset
        limit = None if offset == 0 and current_page == 0 else page_size

        all_data = self.get_all_data(where_query=where_query, limit=limit,
                                     offset=offset,
                                     order_by=self.order_by)
        data_count = self.count_data(where_query=where_query)

        total_pages = math.ceil(data_count / page_size)

        pagination_data = dict()
        pagination_data['has_previous'] = True if (total_pages and current_page) > 1 else False
        pagination_data['has_next'] = True if (total_pages and current_page) < total_pages else False
        pagination_data['total_page'] = total_pages
        pagination_data['current_pages'] = current_page
        pagination_data['count'] = data_count

        if self.get_response_schema:
            all_data = self.get_response_schema().dump(all_data, many=True)

        data = {
            self.data_label: all_data if all_data else [],
            'pagination': pagination_data
        }
        return data

    @marshal_with(Ref('get_response_schema'), code=200)
    @use_kwargs(Ref('get_request_schema'), apply=False)
    @doc(description=Ref('get_description'), summary="", tags=Ref('doc_tags'))
    def get(self):
        """
        get all data with or without pagination
        """
        where_query = {}
        # company_id = get_company_id_from_token()
        # company_id = get_company_id_from_token()

        # if self.check_company:
        #     where_query['company_id'] = company_id

        where_query['is_active'] = True

        if request.args.get("is_active"):
            where_query.pop("is_active")

        search_condition = get_search_query(self.search_fields, request) if self.search_fields else dict()
        filter_condition = get_filter_query(self.filter_fields, request) if self.filter_fields else dict()
        if search_condition:
            where_query.update(**search_condition)
        if filter_condition:
            where_query.update(**filter_condition)
        if self.check_is_deleted:
            where_query.update({'is_deleted': False})
        if self.apply_pagination:
            # print('where_query', where_query)
            data = self.pagination_list(where_query)
        else:
            data = self.get_all_data(where_query=where_query, order_by=self.order_by)
            data = {
                self.data_label: self.get_response_schema().dump(data, many=True) if self.get_response_schema else data
            }
            # print(">>>>>>", data)
        return success_response(data=data)

    @marshal_with(Ref('post_response_schema'), code=200)
    @use_kwargs(Ref('post_request_schema'), apply=False)
    @doc(description=Ref('post_description'), summary="", tags=Ref('doc_tags'))
    def post(self):
        """
        create new data
        """
        json_data = request.form or request.get_json()
        errors = self.post_request_schema().validate(data=json_data)
        current_user_id = current_identity['user_id'] if current_identity else None
        if errors:
            return error_response(message=errors)
        default_data = dict(json_data)
        #
        # if self.check_company:
        #     default_data['company_id'] = get_company_id_from_token()

        if self.is_active:
            default_data['is_active'] = True

        if self.created_date:
            default_data['created_date'] = current_timestamp()

        default_data['created_by'] = current_user_id

        data = self.insert_data(default_data)

        data = self.post_response_schema().dump(data)
        return success_response(data=data)


class BaseDetailsResource(MethodResource):
    """
    get base, delete and update by id
    """
    model = None
    pk = "id"
    name = None
    # api doc
    get_request_schema = NoSchema
    get_response_schema = NoSchema
    put_request_schema = NoSchema
    put_response_schema = NoSchema
    delete_response_schema = DeleteResponseSchema
    doc_tags = []
    get_description = ""
    put_description = ""
    delete_description = ""

    @marshal_with(Ref('get_response_schema'), code=200)
    @use_kwargs(Ref('get_request_schema'), apply=False)
    @doc(description=Ref('get_description'), summary="", tags=Ref('doc_tags'))
    def get(self, id):
        """
        get data by id
        :param id: string
        :return: object
        """
        _id = self.pk
        data = self.get_data({_id: id})
        # print('data', data)
        if not data:
            return error_response(message=api_message.get('no_data_fount'))

        data = self.get_response_schema().dump(data)
        return success_response(data=data)

    @marshal_with(Ref('delete_response_schema'), code=200)
    @doc(description=Ref('delete_description'), summary="", tags=Ref('doc_tags'))
    def delete(self, id):
        """
        delete data by id
        :param id: string
        :return: object
        """
        _id = self.pk
        data = self.get_data({_id: id})
        if not data:
            return error_response(message=api_message.get('no_data_fount'))
        else:
            self.delete_data({_id: id})
        return success_response(message='Deleted successfully')

    @marshal_with(Ref('put_response_schema'), code=200)
    @use_kwargs(Ref('put_request_schema'), apply=False)
    @doc(description=Ref('put_description'), summary="", tags=Ref('doc_tags'))
    def put(self, id):
        """
        update data by id
        :param id: string
        :return: object
        """
        _id = self.pk
        data = self.get_data({_id: id})
        if not data:
            return error_response(message=api_message.get('no_data_fount'))
        else:

            current_user_id = current_identity['user_id'] if current_identity else None
            json_data = request.form or request.get_json()
            errors = self.put_request_schema().validate(data=json_data)
            if errors:
                return error_response(message=errors)
            default_data = dict(json_data)
            default_data['updated_by'] = current_user_id
            default_data['updated_date'] = current_timestamp()

            updated = self.update_data({_id: id}, default_data)
            data = self.get_data({_id: id}) if updated == 1 else None

            data = self.put_response_schema().dump(data) if data else None
        return success_response(data=data, message='Updated successfully')

    @marshal_with(Ref('put_response_schema'), code=200)
    @use_kwargs(Ref('put_request_schema'), apply=False)
    @doc(description=Ref('patch_description'), summary="", tags=Ref('doc_tags'))
    def patch(self, id):
        """
        patch update data by id
        :param id: string
        :return: object
        """
        _id = self.pk
        data = self.get_data({_id: id})
        if not data:
            return error_response(message=api_message.get('no_data_fount'))
        else:
            _dd = dict()
            if data['is_active']:
                _dd['is_active'] = False
            else:
                _dd['is_active'] = True
            self.update_data({_id: id}, _dd)
            data = {'is_active': _dd['is_active']}
        return success_response(data=data, message='Updated successfully')


class BaseDropdownResource(MethodResource):
    """
    get base, delete and update by id
    """
    model = None
    pk = "id"
    label = "name"
    db_helper = None
    choices = None
    check_company = True
    check_is_deleted = False

    def get(self):
        """
        get data by id
        :param id: string
        :return: object
        """
        result = list()
        if self.choices:
            for k, v in dict(self.choices).items():
                result.append({
                    'value': k,
                    'label': v,
                })
        else:
            where_query = {}
            company_id = get_api_key()
            if self.check_company:
                where_query['company_id'] = company_id

            if self.check_is_deleted:
                where_query['is_deleted'] = False
            data = self.get_all(self.model, where_query=where_query)

            for i in data:
                result.append({
                    'value': i[self.pk],
                    'label': i[self.label],
                })

        return success_response(data=result)


def get_random_string() -> str:
    return str(datetime.datetime.now().timestamp()).replace('.', '')[0:13]


# def get_barcode_and_image_url(barcode_no=None):
#     if not barcode_no:
#         barcode_no = get_random_string()
#     from barcode.writer import ImageWriter
#     EAN = barcode.get_barcode('code128')
#     bar_code = EAN(barcode_no, writer=ImageWriter(format="PNG", mode="RGB"))
#     print(">>", BASE_DIR, bar_code)

#     path_image: str = '{}/media/default/{}'.format(BASE_DIR, bar_code)
#     fullname = bar_code.save(path_image)
#     print('fullname', fullname)
#     print('bar_code >>>', bar_code)

#     push_picture_to_s3(file_path=path_image + '.png', file_name=f"{bar_code}.png")

#     s3_link = "{s3_url}/{s3_file_name}".format(s3_url=S3_PUBLIC_URL, s3_file_name=f"{bar_code}.png")
#     print("s3_link: ", s3_link)
#     os.remove(path_image + '.png')

#     data: dict = dict()
#     data['barcode_no']: str = str(bar_code)
#     data['barcode_image']: str = s3_link
#     return data


# def save_image_and_get_url(filename):
#     path_image: str = '{}/media/default/{}'.format(BASE_DIR, filename)
#     fullname = filename.save(path_image)
#     print('fullname', fullname)
#     print('bar_code >>>', filename)

#     push_picture_to_s3(file_path=path_image + '.png', file_name=f"{filename}.png")

#     s3_link = "{s3_url}/{s3_file_name}".format(s3_url=S3_PUBLIC_URL, s3_file_name=f"{filename}.png")
#     print("s3_link: ", s3_link)
#     os.remove(path_image + '.png')

#     data: dict = dict()
#     data['barcode_no']: str = str(filename)
#     data['barcode_image']: str = s3_link
#     return data


def p_print(title, data=None):
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    print("\n========== {} ==================\n".format(title))
    pp.pprint(data)
    print("\n===================================\n")


def get_constant_drop_down(
        label: int = 1, value: int = 0, constant: tuple = None, get_extra_detail: bool = False
) -> list:
    """
    you can customize label, value by passing them into the function
    :param label: which label you want it's in the indexing in the constant drop-down
    :param value: which value you want it's in the indexing in the constant drop-down
    :param constant: it's the list of tuples. Constant tuple of tuple
    :param get_extra_detail: need to fetch the extra detail dict.
    :return: return the list of objects. object has the label and value field.
    """
    if get_extra_detail:
        return [
            {
                **obj[2],
                "label": obj[label],
                "value": obj[value],
            }
            for obj in constant
        ]
    else:
        return [{"label": obj[label], "value": obj[value]} for obj in constant]


class BaseQueryset:
    model = None
    db_helper = None

    def insert_data(self, data):
        return self.db_helper.insert_data(self.model, data)

    def insert_bulk_data(self, data):
        return self.db_helper.insert_many_data(data=data)

    def update_data(self, where_condition, data):
        return self.db_helper.update_data(self.model, where_condition, data)

    def delete_data(self, where_condition):
        return self.db_helper.delete_data(model=self.model, where_query=where_condition)

    def get_count(self, where_query):
        return self.db_helper.get_count(model=self.model, where_query=where_query)

    def get_data(self, where_condition, select_column=[]):
        return self.db_helper.get_data(model=self.model, where_query=where_condition, select_column=select_column)

    def get_all_data(self, where_query=dict(), select_column=[], offset=0, limit=0, order_by=[]):
        print("-------------------", where_query)
        return self.db_helper.get_all_data(model=self.model, where_query=where_query,
                                           select_column=select_column, offset=offset,
                                           limit=limit, order_by=order_by)
