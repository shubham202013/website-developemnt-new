import os

from common.constants import USER_TYPE_EMPLOYEE, CURRENT_USER, USER_TYPE_COMPANY_ADMIN
# from common.rediscomponant.redisware import set_data
# from v1.company import queryset as company_querset, schema as company_schema
# from v1.company.helper import get_company_data_response
# from v1.employee import queryset as employee_queryset
# from v1.role_with_permission.queryset import get_role_wise_permissions
from v1.users.schema import GetUserSchema
from v1.users import queryset as user_queryset

SECRET_KEY = os.environ.get('SECRET_KEY')


def get_user_detail(user_object):

    user_id = str(user_object["user_id"])
    result = {
        "id": user_id,
        "full_name": user_object["full_name"],
        "email": user_object["email"],
        "dial_code": user_object["dial_code"],
        "phone_number": user_object["phone_number"],
        "is_superuser": user_object["is_superuser"],
        "referral_code": user_object["referral_code"],
        "invite_referral_code": user_object.get("invite_referral_code"),
        
        "image": user_object["image"],
        # "is_first_login": user_object.get("is_first_login"),
        "user_id": user_id,
    }
    return result


def get_login_user_dict(user_object, token, selected_company_id=None):
    token_dict = {"token": token, 'user_id': user_object.get("user_id"),
                  'is_superuser': user_object.get("is_superuser"),
                  } 

    user_detail =  user_queryset.get_user_object(where_query={'email': user_object.get("email")})


    try:
        user_object = GetUserSchema().dump(user_object)
        # set_data(CURRENT_USER, token, user_object)
    except Exception as e:
        print('get_login_user_dict error-->', e)

    token_info = {"token": token, "type": "Token"}

    result = dict()
    result["user"] = get_user_detail(user_object)
    result['user']['timezone'] = user_detail.get("timezone")
    result['user']['date_format'] = user_detail.get("date_format")
    result["token"] = token_info

    return result
