from flask import request
from flask_apispec import MethodResource, use_kwargs

from common.constants import CURRENT_USER, USER_TYPE_SUPER_ADMIN, USER_TYPE_COMPANY_ADMIN, USER_TYPE_EMPLOYEE, \
    ERROR_CODE_DATA_NOT_FOUND, ERROR_CODE_WRONG_PASSWORD, USER_TYPE_CLIENT, USER_TYPE_CRM
from common.messages import api_message
# from common.notification.notification import init_forgot_password_v1
from common.notification.notification import init_forgot_password_v1
from common.password import verify_password, generate_password
from common.website_datetime import current_timestamp
# from common.rediscomponant.redisware import delete_to_redis, remove_data
from common.utils import error_response, generate_8_digit_string, success_response, generate_activation_token, \
    error_response_for_under_maintenance
from config.authentication import authenticated, current_identity
from v1.auth import schema
from v1.auth.helper import get_login_user_dict
from v1.auth.queryset import create_token
from v1.auth.schema import ResetPasswordSchema, SetPasswordSchema
# from v1.under_maintenance import queryset as under_maintenance_queryset
from v1.users import queryset as user_queryset
from v1.users.schema import GetUserSchema




class LoginView(MethodResource):

    @use_kwargs(schema.LoginSchema, apply=False)
    def post(self):
        """
        create new data
        """
        json_data = request.form or request.get_json()
        print('json data: %s' % json_data)
        errors = schema.LoginSchema().validate(data=json_data)
        print("Login errors ------------   ", errors)
        if errors:
            return error_response(message=errors)
        # user_type = [USER_TYPE_SUPER_ADMIN, USER_TYPE_COMPANY_ADMIN, USER_TYPE_EMPLOYEE, USER_TYPE_CLIENT, USER_TYPE_CRM]
        default_data = dict(json_data)
        is_google_signup = default_data.get('is_google_signup')
        
        if is_google_signup:
            google_signup_details = default_data.get('google_signup_details')
            user_obj = user_queryset.get_data({"email": google_signup_details.get('email')})
            if user_obj:
                if user_obj.get('google_auth_id') and user_obj.get('google_auth_id') == google_signup_details.get('jti'):
                    token = create_token(user_obj.get('user_id'))
                    data = get_login_user_dict(user_obj, token)

                    message = api_message["login_success"]
                    response_data = success_response(data, message)
                    return response_data
                else:
                    user_queryset.update_data({'user_id': user_obj.get('user_id')}, {"google_auth_id": google_signup_details.get('jti')} )
                    token = create_token(user_obj.get('user_id'))
                    data = get_login_user_dict(user_obj, token)

                    message = api_message["login_success"]
                    response_data = success_response(data, message)
                    return response_data
            else:
                user_detail = {
                    "full_name": google_signup_details.get("name"),
                    "email": google_signup_details.get('email'),
                    "is_active": True,
                    "google_auth_id": google_signup_details.get('jti'),
                    "referral_code" : generate_8_digit_string(),
                    "created_date": current_timestamp()
                }

                user_data = user_queryset.insert_data(user_detail)
                data = GetUserSchema().dump(user_data)
                token = create_token(data.get('user_id'))
                data = get_login_user_dict(data, token)

                message = api_message["login_success"]
                response_data = success_response(data, message)
                return response_data

        else:
            where_condition = {"email": default_data.get("email")}
            user_obj = user_queryset.get_data(
                where_condition={"email": default_data.get("email"), 'is_active': True})
            print('user_obj', user_obj)
            if user_obj:
            
                hash_password = user_obj.get('password')
                password = str(default_data.get('password'))
                print("hash_password", hash_password)
                print("password", password)
                if not verify_password(password, hash_password):

                    response_data = error_response(message=api_message["invalid_credentials"])
                    return response_data
                else:

                    token = create_token(user_obj.get('user_id'))
                    print("token", token)
                    data = get_login_user_dict(user_obj, token)

                    # last login changes
                    # login_update_data = dict()
                    # login_update_data['last_login'] = current_timestamp()  # datetime.now(tz=timezone.utc)

                    # login_update_data['is_first_login'] = False if user_obj.get("is_first_login") else True

                    # # if default_data.get("device_id"):
                    # #     login_update_data['device_id'] = default_data.get("device_id")
                    # #     login_update_data['device_type'] = default_data.get("device_type")

                    # user_queryset.update_data(where_condition={"user_id": user_obj.get('user_id')},
                    #                             data=login_update_data)

                    # saving to redis
                    # set_data(CURRENT_USER, token, user_obj)
                    message = api_message["login_success"]

                    response_data = success_response(data, message)
                    return response_data

            else:

                response_data = error_response(message=api_message["wrong_credentials"])
        return response_data


class LogoutResource(MethodResource):
    """
    Authentication Logout
    """
    decorators = [authenticated()]

    # @use_kwargs(schema.LogoutSchema, apply=False)
    def get(self):
        """
        get all data with or without pagination
        """
        user_id = current_identity['user_id'] if current_identity else None
        user = user_queryset.get_data(where_condition={'user_id': user_id})
        if user:
            # try:
            #     token = request.headers['Authorization']
            #     # auth_header = token.split(' ')
            #     # key = auth_header[1]
            #     # remove_data(CURRENT_USER, key)
            # except Exception as e:
            #     print('e Error to decode token >>', e)
            #     return success_response(message=api_message["invalid_token"])

            user_queryset.delete_token({'user': user_id})

        return success_response(message=api_message["success_logout"], code=200)


class ResetPasswordListResource(MethodResource):
    """
    ResetPassword
    """

    # @use_kwargs(ResetPasswordResSchema, apply=False)
    # @marshal_with(ResetPasswordResSchema)
    def get(self, id):
        get_user = user_queryset.get_data(where_condition={"forgot_password_verify_code": id})
        curr_datetime = current_timestamp()
        print(curr_datetime)
        if get_user:
            token_generate_time = get_user.get('forgot_password_verify_code_date')
            remaining_datetime = curr_datetime - token_generate_time
            if remaining_datetime > 3600:
                response_data = {"success": False}
            else:
                response_data = {"success": True}
        else:
            response_data = {"success": False}
        return success_response(response_data)

    @use_kwargs(ResetPasswordSchema, apply=False)
    # @marshal_with(ResetPasswordResSchema)
    def post(self, id):
        """
        create new data
        """
        json_data = request.form or request.get_json()
        errors = ResetPasswordSchema().validate(data=json_data)
        if errors:
            return error_response(errors)

        password = json_data.get('password', None)
        confirm_password = json_data.get('confirm_password', None)

        user = user_queryset.get_data(where_condition={"forgot_password_verify_code": id})

        if user:
            if password and confirm_password:
                if password != confirm_password:
                    return error_response(error_code=ERROR_CODE_WRONG_PASSWORD,
                                          message="Passwords don't match")
                else:
                    password = generate_password(password)
                    user_queryset.update_data({"user_id": user["user_id"]}, {"password": password})

                    return success_response(message=api_message["password_updated"], code=200)
            else:
                return error_response(error_code=ERROR_CODE_DATA_NOT_FOUND, message=api_message['data_not_found'])
        else:
            return error_response(error_code=ERROR_CODE_DATA_NOT_FOUND, message=api_message['user_not_found'])


class ForgotPasswordResource(MethodResource):
    """
    ForgotPasswordResource
    """

    def post(self):
        """
        create new data
        """
        json_data = request.form or request.get_json()
        errors = schema.ForgotPasswordSchema().validate(data=json_data)
        if errors:
            return error_response(errors)

        email = json_data.get('email')
        if not email:
            return error_response(error_code=ERROR_CODE_DATA_NOT_FOUND, message=api_message['user_not_found'])

        where_condition = {'email': email}
        user = user_queryset.get_data(where_condition=where_condition)

        if not user:
            return error_response(error_code=ERROR_CODE_DATA_NOT_FOUND, message=api_message['user_not_found'])

        forgot_code = generate_activation_token()
        forgot_time = current_timestamp()
        user_queryset.update_data({"user_id": user["user_id"]},
                                  {"forgot_password_verify_code": str(forgot_code),
                                   "forgot_password_verify_code_date": forgot_time})

        # init forgot password email
        to_email_list = [email]
        init_forgot_password_v1(to_email_list=to_email_list, forgot_code=forgot_code, company_id=user.get('company_id'))

        return success_response(data=[], message="Check your email to reset password", code=200)


class ChangePasswordResource(MethodResource):
    """
    ForgotPasswordResource
    """
    decorators = [authenticated()]

    def post(self):
        """
        create new data
        """
        json_data = request.form or request.get_json()
        errors = schema.ChangePasswordSchema().validate(data=json_data)
        if errors:
            return error_response(errors)

        old_password = json_data.get('old_password', None)
        new_password = json_data.get('new_password', None)
        confirm_password = json_data.get('new_password', None)

        user_id = current_identity['user_id'] if current_identity else None
        user = user_queryset.get_data(where_condition={'user_id': user_id})

        if new_password != confirm_password:
            return error_response(error_code=ERROR_CODE_WRONG_PASSWORD,
                                  message="Passwords don't match")
        else:
            if user:
                if old_password and new_password:
                    hash_password = user["password"]
                    verify_password_ = verify_password(old_password, hash_password)
                    print('verify_password', verify_password)
                    if verify_password_:
                        new_password = generate_password(new_password)
                        user_queryset.update_data({"user_id": user["user_id"]}, {"password": new_password})
                    else:
                        return error_response(error_code=ERROR_CODE_WRONG_PASSWORD,
                                              message=api_message['old_password_wrong'])
                return success_response(message=api_message["password_updated"], code=200)
            else:
                return error_response(error_code=ERROR_CODE_DATA_NOT_FOUND, message=api_message['user_not_found'])


class SetPasswordListResource(MethodResource):
    """
    SetPassword
    """

    @use_kwargs(SetPasswordSchema, apply=False)
    # @marshal_with(ResetPasswordResSchema)
    def post(self, id):
        """
        create new data
        """
        json_data = request.form or request.get_json()
        errors = ResetPasswordSchema().validate(data=json_data)
        if errors:
            return error_response(errors)

        password = json_data.get('password', None)
        confirm_password = json_data.get('confirm_password', None)

        user = user_queryset.get_data(where_condition={"user_id": id})

        if user:
            if password and confirm_password:
                if password != confirm_password:
                    return error_response(error_code=ERROR_CODE_WRONG_PASSWORD,
                                          message="Passwords don't match")
                else:
                    password = generate_password(password)
                    user_queryset.update_data({"user_id": user["user_id"]}, {"password": password})

                    return success_response(message=api_message["password_updated"], code=200)
            else:
                return error_response(error_code=ERROR_CODE_DATA_NOT_FOUND, message=api_message['data_not_found'])
        else:
            return error_response(error_code=ERROR_CODE_DATA_NOT_FOUND, message=api_message['user_not_found'])
