import json
import os

from flask import request
from common.base import BaseListResource
from common.utils import error_response, success_response
from v1.chrome_extention_registratioin import models as chrome_extention_registratioin_models
from v1.chrome_extention_registratioin import queryset as chrome_extention_registratioin_queryset

class ChromeExtentionRegistrationResource(BaseListResource):

    def post(self):
        json_data = request.form or request.get_json()

        default_data = dict(json_data)

        email = default_data.get('email')
        check_exists = chrome_extention_registratioin_queryset.get_data({"email":email })
        if check_exists:
            return error_response(message="User already exists")
        
        chrome_extention_registratioin_queryset.insert_data(default_data)

        return success_response(data="User Add Successfully")
    
class VerifyChromeExtentionUserResource(BaseListResource):

    def post(self):
        json_data = request.form or request.get_json()

        default_data = dict(json_data)

        email = default_data.get('email')
        check_exists = chrome_extention_registratioin_queryset.get_data({"email":email })
        result = False
        if check_exists:
            result = True

        return success_response(data=True)