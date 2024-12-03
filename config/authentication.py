import hashlib
import hmac
import json
import os
from functools import wraps

from flask import request, g
from werkzeug.local import LocalProxy

from common.messages import api_message
# from common.rediscomponant.redisware import get_data, set_to_redis
from common.utils import error_response
# from v1.company import queryset as company_queryset
from v1.users import queryset as user_queryset


# Use 'g' for storing request-specific data
current_identity = LocalProxy(lambda: getattr(g, 'current_identity', None))
SECRET_KEY = os.environ.get('SECRET_KEY')


def authenticated():
    """
    View decorator that requires a valid JWT token to be present in the request
    :param realm: an optional realm
    """

    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            # apikey = request.headers['apikey'] if 'apikey' in request.headers else None
            token = None
            checksum = None

            if 'Authorization' in request.headers:
                token = request.headers['Authorization']
            if not token:
                return error_response(message=api_message["token_required"], error_code=401)

            # if 'signature' in request.headers:
            #     checksum = request.headers['signature']
            # if not checksum:
            #     return error_response(message=api_message["not_authorized"],
            #                           error_code=401)

            auth_header = token.split(' ')
            try:
                pre_txt = auth_header[0]
                key = auth_header[1]
            except Exception as e:
                print('e Error to decode token >>', e)
                return error_response(message=api_message["invalid_token"], error_code=401)
            if pre_txt != 'Token':
                return error_response(message=api_message["invalid_token"], error_code=401)

            # secret = bytes(SECRET_KEY, 'utf-8')
            # message = bytes(key, 'utf-8')
            # signature = hmac.new(secret, message, digestmod=hashlib.sha256).hexdigest()

            # if signature != checksum:
            #     # if given checksum of token is different from key checksum then error
            #     return error_response(message=api_message["not_authorized"], error_code=401)

            current_user = None
            # is_redis = get_data("CURRENT_USER", key)
            # print('is_redis--->',is_redis)
            # if is_redis:
            #     # print('get token from redis', is_redis)
            #     current_user = json.loads(is_redis)
            # else:
            token_res = user_queryset.get_token(where_condition={"key": key})
            if token_res:
                current_user = user_queryset.get_data(where_condition={'user_id': token_res.get('user')})
                # if current_user:
                #     set_to_redis(key, json.dumps(current_user, default=str))

            # if current_user:
            #     if current_user['is_superuser']:
            #         current_user['company_id'] = apikey
            #     else:
            #         if not apikey:
            #             return error_response(message=api_message["api_required"],
            #                                   error_code=401)
            #         if apikey != current_user['company_id']:
            #             return error_response(message=api_message["not_authorized"],
            #                                   error_code=401)
            #         current_user['company_id'] = apikey
            if not current_user:
                return error_response(message=api_message["invalid_token"], error_code=401)

            # check permission
            # if realm:
            #     if current_user['user_type'] == USER_TYPE_SUPER_USER:
            #         pass
            #     else:
            #         pass
            #         # TODO: ask naimbhai for changes
            #         #  check the permission if found any other user
            #         res = get_role_data(where_condition={'role_id': current_user['role_id']})
            #         print("request.method", request.method)
            #         if res:
            #             if res['permissions_module_list']:
            #                 module_action = PERMISSION_METHOD_DICT.get(request.method, None)
            #                 auth_data = get_module_action_data(
            #                     where_condition={'module_name': realm, 'module_action': module_action})
            #                 if auth_data:
            #                     if auth_data['id'] not in res['permissions_module_list']:
            #                         return error_response(message=api_message["not_authorized"],
            #                                               error_code=ERROR_CODE_NOT_PERMITTED)
            #                 else:
            #                     return error_response(message=api_message["not_authorized"],
            #                                           error_code=ERROR_CODE_NOT_PERMITTED)
            #             else:
            #                 return error_response(message=api_message["not_authorized"],
            #                                       error_code=ERROR_CODE_NOT_PERMITTED)
            #         else:
            #             return error_response(message=api_message["not_authorized"],
            #                                   error_code=ERROR_CODE_NOT_PERMITTED)
            #

            g.current_identity = current_user
            return fn(*args, **kwargs)

        # old Authentication
        # def decorator(*args, **kwargs):
        #     auth_header = None
        #     if 'Authorization' in request.headers:
        #         auth_header = request.headers['Authorization']
        #     if not auth_header:
        #         return error_response(message=api_message["token_required"], error_code=401)
        #
        #     auth_header = auth_header.split(" ")
        #
        #     if auth_header[0] != "Token":
        #         return error_response(message=api_message["invalid_token"], error_code=401)
        #     try:
        #         decoded = jwt.decode(auth_header[1], SECRET_KEY, algorithm="HS512")
        #         # decoded = jwt.decode("auth_header[1]", SECRET_KEY, algorithm="HS512")
        #     except Exception:
        #         return error_response(message=api_message["not_authorized"], error_code=401)
        #
        #     user_token = decoded.get("token")
        #     decoded.get("company_id")
        #
        #     in_redis = get_data("CURRENT_USER", user_token)
        #     # in_redis = None
        #     print('in_redis', in_redis)
        #     user = None
        #     if in_redis and in_redis != 0:
        #         user = json.loads(in_redis)
        #
        #         try:
        #             user.update({"user_id": user["_id"]})
        #             del user["_id"]
        #         except:
        #             pass
        #         # user = users.models.User(**user)
        #     else:
        #         # print("user_token-------->",user_token)
        #         try:
        #             token = user_queryset.get_token(where_condition=({"key": user_token}))
        #         except:
        #             token = None
        #         # print('token----',token)
        #         if token:
        #             user = user_queryset.get_data(where_condition={'user_id': token['user']})
        #             # if user:
        #             #     set_data("CURRENT_USER", user_token, user.to_json())
        #             # we are getting user detail from token.user and sending it to the authentication
        #             # user = json.loads(token.get("user"))
        #             # user.update({"user_id": user["_id"]})
        #             # user.update({"user_id": user["_id"]})
        #             # print('user-------->',user)
        #
        #             # try:
        #             #     set_data("CURRENT_USER", user_token, user.to_json())
        #             # except:
        #             #     pass
        #             # print('this is request data', user)
        #         else:
        #             user = None
        #
        #     if not user:
        #         return error_response(message=api_message["invalid_token"], error_code=401)
        #     # apikey = request.headers['apikey'] if 'apikey' in request.headers else None
        #     # token = None
        #     # checksum = None
        #
        #     # if 'Authorization' in request.headers:
        #     #     token = request.headers['Authorization']
        #     # if not token:
        #     #     return error_response(message=api_message["token_required"], error_code=401)
        #
        #     # print('token-->',token)
        #     # # if 'signature' in request.headers:
        #     # #     checksum = request.headers['signature']
        #     # # if not checksum:
        #     # #     return error_response(message=api_message["not_authorized"],
        #     # #                           error_code=401)
        #     # # print('checksum-->',checksum)
        #     # auth_header = token.split(' ')
        #     # try:
        #     #     pre_txt = auth_header[0]
        #     #     key = auth_header[1]
        #     # except Exception as e:
        #     #     print('e Error to decode token >>', e)
        #     #     return error_response(message=api_message["invalid_token"], error_code=401)
        #     # if pre_txt != 'Token':
        #     #     return error_response(message=api_message["invalid_token"], error_code=401)
        #
        #     # secret = bytes(SECRET_KEY, 'utf-8')
        #     # message = bytes(key, 'utf-8')
        #     # signature = hmac.new(secret, message, digestmod=hashlib.sha512)
        #     # print('signature-->',signature)
        #     # # if signature != checksum:
        #     #     # if given checksum of token is different from key checksum then error
        #     #     return error_response(message=api_message["not_authorized"], error_code=401)
        #
        #     # current_user = None
        #     # is_redis = get_from_redis(key)
        #     # if is_redis:
        #     #     # print('get token from redis', is_redis)
        #     #     current_user = json.loads(is_redis)
        #     # else:
        #     #     pass
        #     #     # todo : call internal and get data here
        #     #     # token_res = Token.objects.filter(key=key).first()
        #     #     # if token_res:
        #     #     #     current_user = mongo_base.get_data(User, where_query={'user_id': token_res['user'].id})
        #     #     #     if current_user:
        #     #     #         set_to_redis(key, json.dumps(current_user, default=str))
        #
        #     # if current_user:
        #     #     if current_user['user_type'] == USER_TYPE_SUPER_USER:
        #     #         current_user['company_id'] = apikey
        #     #     else:
        #     #         if not apikey:
        #     #             return error_response(message=api_message["api_required"],
        #     #                                   error_code=401)
        #     #         if not (apikey == current_user['company_id']):
        #     #             return error_response(message=api_message["not_authorized"],
        #     #                                   error_code=401)
        #     #         current_user['company_id'] = apikey
        #     # if not current_user:
        #     #     return error_response(message=api_message["invalid_token"], error_code=401)
        #
        #     # check permission
        #     # if realm:
        #     #     if current_user['user_type'] == USER_TYPE_SUPER_USER:
        #     #         pass
        #     #     else:
        #     #         pass
        #     #         # TODO: ask naimbhai for changes
        #     #         #  check the permission if found any other user
        #     #         res = get_role_data(where_condition={'role_id': current_user['role_id']})
        #     #         print("request.method", request.method)
        #     #         if res:
        #     #             if res['permissions_module_list']:
        #     #                 module_action = PERMISSION_METHOD_DICT.get(request.method, None)
        #     #                 auth_data = get_module_action_data(
        #     #                     where_condition={'module_name': realm, 'module_action': module_action})
        #     #                 if auth_data:
        #     #                     if auth_data['id'] not in res['permissions_module_list']:
        #     #                         return error_response(message=api_message["not_authorized"],
        #     #                                               error_code=ERROR_CODE_NOT_PERMITTED)
        #     #                 else:
        #     #                     return error_response(message=api_message["not_authorized"],
        #     #                                           error_code=ERROR_CODE_NOT_PERMITTED)
        #     #             else:
        #     #                 return error_response(message=api_message["not_authorized"],
        #     #                                       error_code=ERROR_CODE_NOT_PERMITTED)
        #     #         else:
        #     #             return error_response(message=api_message["not_authorized"],
        #     #                                   error_code=ERROR_CODE_NOT_PERMITTED)
        #     #
        #
        #     _request_ctx_stack.top.current_identity = user
        #     return fn(*args, **kwargs)

        return decorator

    return wrapper


def allow_any():
    """
    Allow any without any authentication (Open API)
    View decorator that requires a valid JWT token to be present in the request
    :param realm: an optional realm
    """

    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            g.current_identity = None
            return fn(*args, **kwargs)

        return decorator

    return wrapper


def get_api_key():
    """
    get api key from headers
    """
    apikey = request.headers['apikey'] if 'apikey' in request.headers else None
    return apikey


def get_authorisation_token():
    """
    get authorisation token from header
    """
    authorisation = request.headers['Authorization'] if 'Authorization' in request.headers else None
    return authorisation


# def get_company_id_from_token(default_company_id=False):
#     company_id = request.headers['apikey'] if 'apikey' in request.headers else None
#     if company_id:
#         company_obj = company_queryset.get_company_data(where_condition={"company_id": company_id})
#         if company_obj and company_obj.get("parent_id") and not default_company_id:
#             company_id = company_obj.get("parent_id")
#     else:
#         return error_response(message=api_message["api_required"], error_code=401)

#     return company_id


def tokenAuthentication():
    """
    View decorator that requires a valid JWT token to be present in the request
    :param realm: an optional realm
    """

    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):

            token = None
            checksum = None

            if 'Authorization' in request.headers:
                token = request.headers['Authorization']
            if not token:
                return error_response(message=api_message["token_required"], error_code=401)

            if 'signature' in request.headers:
                checksum = request.headers['signature']
            if not checksum:
                return error_response(message=api_message["not_authorized"],
                                      error_code=401)

            auth_header = token.split(' ')
            try:
                pre_txt = auth_header[0]
                key = auth_header[1]
            except Exception as e:
                print('e Error to decode token >>', e)
                return error_response(message=api_message["invalid_token"], error_code=401)
            if pre_txt != 'Token':
                return error_response(message=api_message["invalid_token"], error_code=401)

            secret = bytes(SECRET_KEY, 'utf-8')
            message = bytes(key, 'utf-8')
            signature = hmac.new(secret, message, digestmod=hashlib.sha256).hexdigest()

            if signature != checksum:
                # if given checksum of token is different from key checksum then error
                return error_response(message=api_message["not_authorized"], error_code=401)

            current_user = None
            # is_redis = get_data("CURRENT_USER", key)
            # print('is_redis--->',is_redis)
            # if is_redis:
            #     # print('get token from redis', is_redis)
            #     current_user = json.loads(is_redis)
            # else:
            token_res = user_queryset.get_token(where_condition={"key": key})
            if token_res:
                current_user = user_queryset.get_data(where_condition={'user_id': token_res.get('user')})
                # if current_user:
                #     set_to_redis(key, json.dumps(current_user, default=str))

            apikey = request.headers['apikey'] if 'apikey' in request.headers else None
            if apikey:
                current_user['company_id'] = apikey

            if not current_user:
                return error_response(message=api_message["invalid_token"], error_code=401)

            g.current_identity = current_user
            return fn(*args, **kwargs)

        return decorator

    return wrapper
