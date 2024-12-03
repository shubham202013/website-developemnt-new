import json
import os

from flask import request
from common.password import generate_password
# from flask_apispec import MethodResource

from common.base import BaseListResource, BaseDetailsResource
from common.choices import USER_ROLE_MANAGER
from common.constants import CURRENT_USER, USER_TYPE_EMPLOYEE, USER_TYPE_CRM, USER_TYPE_COMPANY_ADMIN
from common.helper import generate_otp
from common.inline_base import InlineBaseResource
from common.messages import api_message
from common.website_datetime import current_timestamp
from common.utils import error_response, generate_8_digit_string, success_response, get_search_query, get_filter_query
from config.authentication import authenticated, current_identity
from database.helper import memsql as memsql_base
from v1.auth import helper as auth_helper
from v1.auth.helper import get_user_detail
# from v1.company.helper import send_verification_mail
from v1.users import models as user_models
from v1.users import queryset as user_queryset
from v1.users.helper import add_referral
from v1.users.schema import GetUserSchema, CreateUserSchema

class UserListResource(BaseListResource):
    # decorators = [authenticated()]

    get_data = user_queryset.get_data
    get_all_data = staticmethod(user_queryset.get_all_data)
    insert_data = staticmethod(user_queryset.insert_data)
    count_data = staticmethod(user_queryset.get_count)

    apply_pagination = True
    check_company = True

    model = user_models.User

    search_fields = ['job_name']
    filter_fields = []
    order_by = [['created_date', 'desc']]
    data_label = 'data'

    post_request_schema = CreateUserSchema
    post_response_schema = GetUserSchema
    get_response_schema = GetUserSchema

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

        query_condition = {'email': default_data.get("email")}

        user_object = user_queryset.get_data(where_condition=query_condition)
        if user_object:
            return error_response(message="Email Already Exist !")

        if self.is_active:
            default_data['is_active'] = True

        if self.created_date:
            default_data['created_date'] = current_timestamp()

        default_data['created_by'] = current_user_id
        create_user_referral_code = generate_8_digit_string()
        default_data['referral_code'] = create_user_referral_code

        invite_referral_code = default_data.get('invite_referral_code')
        # if invite_referral_code:
        #     invite_referral_code = default_data.pop('invite_referral_code')

        data = self.insert_data(default_data)
        if invite_referral_code and invite_referral_code != "null" and invite_referral_code != "":
            add_referral(invite_referral_code, data.user_id)

        data = self.post_response_schema().dump(data)
        return success_response(data=data)
