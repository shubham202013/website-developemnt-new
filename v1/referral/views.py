import json
import os
from flask import request

from common.base import BaseListResource, BaseDetailsResource
from common.website_datetime import current_timestamp
from common.utils import error_response, get_filter_query, get_search_query, success_response
from config.authentication import authenticated, current_identity
from database.helper import memsql as memsql_base
from v1.auth import helper as auth_helper
# from v1.company.helper import send_verification_mail
from v1.referral import models as referral_models
from v1.referral import queryset as referral_queryset
from v1.referral.schema import GetReferralSchema, CreateReferralSchema

class ReferralListResource(BaseListResource):
    decorators = [authenticated()]

    # get_data = user_queryset.get_data
    get_all_data = staticmethod(referral_queryset.get_all_referral_data)
    insert_data = staticmethod(referral_queryset.insert_referral_data)
    count_data = staticmethod(referral_queryset.get_referral_count)

    apply_pagination = True

    model = referral_models.Referral

    search_fields = ['title']
    filter_fields = []
    order_by = [['created_date', 'desc']]
    data_label = 'data'

    post_request_schema = CreateReferralSchema
    post_response_schema = GetReferralSchema
    get_response_schema = GetReferralSchema

    def get(self):
        """
        get all data with or without pagination
        """
        where_query = {}

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
        return success_response(data=data)

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

        default_data['is_active'] = False

        if self.created_date:
            default_data['created_date'] = current_timestamp()

        default_data['created_by'] = current_user_id
        data = self.insert_data(default_data)

        data = self.post_response_schema().dump(data)
        return success_response(data=data)



class ReferralDetailResource(BaseDetailsResource):
    decorators = [authenticated()]
    pk = "id"
    methods = ['GET', 'PUT', 'DELETE', 'PATCH']

    model = referral_models.Referral
    put_request_schema = CreateReferralSchema
    get_response_schema = GetReferralSchema

    get_data = staticmethod(referral_queryset.get_referral_data)
    update_data = staticmethod(referral_queryset.update_referral_data)
    delete_data = staticmethod(referral_queryset.delete_referral_data)


    def put(self, id):
        """
        update data by id
        :param id: string
        :return: object
        """
        _id = self.pk
        data = self.get_data({_id: id})
        if not data:
            return error_response(message='Data not found!!')
        else:

            current_user_id = current_identity['user_id'] if current_identity else None
            json_data = request.form or request.get_json()
            errors = self.put_request_schema().validate(data=json_data)
            if errors:
                return error_response(message=errors)
            default_data = dict(json_data)

            query_condition = {'title': default_data.get("title"),
                               _id: {"$ne": id}}

            referral_object = referral_queryset.get_referral_data(where_condition=query_condition)
            if referral_object:
                return error_response(message="Title Already Exist !")

            default_data['updated_by'] = current_user_id
            default_data['updated_date'] = current_timestamp()

            updated = self.update_data({_id: id}, default_data)
            data = self.get_data({_id: id}) if updated == 1 else None

            data = self.put_response_schema().dump(data) if data else None
        return success_response(data=data, message='Updated successfully')
