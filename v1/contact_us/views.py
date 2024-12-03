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
from v1.contact_us import models as contact_us_models
from v1.contact_us import queryset as contact_us_queryset
from v1.contact_us.schema import GetContactUsSchema, CreateContactUsSchema

class ContactUsListResource(BaseListResource):
    # decorators = [authenticated()]

    get_data = contact_us_queryset.get_data
    get_all_data = staticmethod(contact_us_queryset.get_all_data)
    insert_data = staticmethod(contact_us_queryset.insert_data)
    count_data = staticmethod(contact_us_queryset.get_count)

    apply_pagination = True
    check_company = True

    model = contact_us_models.ContactUs

    search_fields = []
    filter_fields = []
    order_by = [['created_date', 'desc']]
    data_label = 'data'

    post_request_schema = CreateContactUsSchema
    post_response_schema = GetContactUsSchema
    get_response_schema = GetContactUsSchema
