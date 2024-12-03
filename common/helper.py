from common.choices import COUNTRY_LIST
from common.constants import SEND_CLIENT_CHANGE_PASSWORD_MAIL_NOTIFICATION
# from common.utils import send_to_consumer
from v1.users import queryset as user_queryset
# from v1.role_with_permission import queryset as role_queryset
import random


def generate_otp():
    """
    Generate otp
    """
    return random.randint(100000, 999999)


def send_otp(company_id, dial_code, mobile_no, otp):
    """
    Send OTP
    TODO : Remaining
    """
    print('company_id, dial_code, mobile_no, otp', [company_id, dial_code, mobile_no, otp])
    return 0


# def get_role_using_role_type(company_id, is_superuser=False):
#     role_obj = role_queryset.get_all_role_data(where_query={"company_id": company_id})
#     return_dict = dict()
#     for obj in role_obj:
#         if not return_dict.get(obj.get("module"), None):
#             return_dict[obj.get("module")] = dict()
#         return_dict[obj.get("module")][obj.get("action")] = True if is_superuser else obj.get("permission")
#     # print(return_dict)
#     return return_dict


def get_country_object(pk):
    obj = [obj for obj in COUNTRY_LIST if obj.get("code") == pk]
    return obj[0] if obj else None


# def send_change_password_mail_notification(user_id, email, first_name, last_name, company_id):
#     data = {
#         "user_id": user_id,
#         "email": email,
#         "first_name": first_name,
#         "last_name": last_name,
#         'company_id': company_id
#     }
#     send_to_consumer(SEND_CLIENT_CHANGE_PASSWORD_MAIL_NOTIFICATION,
#                      data)

#     return True
