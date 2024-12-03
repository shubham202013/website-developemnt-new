import os
# from common.notification.init_gateway import _send_email, _send_email_common
# from v1.module_config.gmail_config.helper import get_email_config
from flask import render_template
from common.notification.init_gateway import _send_email_common
from v1.users import queryset as user_queryset
# def send_notification_sqs(data):
#     """this is for temp. """
#     pass


# def init_forgot_password(to_email_list, forgot_code):
#     frontend_url = os.environ.get('FRONTEND_URL')
#     verify_email_link = "{0}/reset-password/{1}".format(frontend_url, forgot_code)
#     email_conf = dict()
#     email_conf['host'] = os.environ.get('DEFAULT_EMAIL_HOST')
#     email_conf['username'] = os.environ.get('DEFAULT_EMAIL_HOST_USER')
#     email_conf['password'] = os.environ.get("DEFAULT_EMAIL_HOST_PASSWORD")
#     email_conf['port'] = os.environ.get('DEFAULT_EMAIL_PORT')
#     email_conf['from_email'] = os.environ.get('DEFAULT_FROM_EMAIL')

#     subject = "Forget Password"
#     message = "Hi, To reset password go through the link {0}".format(verify_email_link)
#     _send_email(to_email_list=to_email_list, subject=subject, message=message,
#                 email_conf=email_conf)


def init_forgot_password_v1(to_email_list, forgot_code, company_id):
    frontend_url = os.environ.get('FRONTEND_URL')
    verify_email_link = "{0}/reset-password/{1}".format(frontend_url, forgot_code)
    email_conf = dict()
    email_conf['host'] = os.environ.get('DEFAULT_EMAIL_HOST')
    email_conf['username'] = os.environ.get('DEFAULT_EMAIL_HOST_USER')
    email_conf['password'] = os.environ.get("DEFAULT_EMAIL_HOST_PASSWORD")
    email_conf['port'] = os.environ.get('DEFAULT_EMAIL_PORT')
    email_conf['from_email'] = os.environ.get('DEFAULT_FROM_EMAIL')
    full_name = None
    last_name = None

    user_obj = user_queryset.get_data(where_condition={'email': to_email_list[0]})
    if user_obj:
        full_name = user_obj.get('full_name')
    subject = "Forgot Password"
    # message = "Hi, To reset password go through the link {0}".format(verify_email_link)
    email_message = render_template("forgot-password.html",
                                    full_name=full_name ,
                                    verify_email_link=verify_email_link
                                    )
    # _send_email(to_email_list=to_email_list, subject=subject, message=message,
    #             email_conf=email_conf)
    _send_email_common(to_email_list=to_email_list, subject=subject, message=email_message,
                       email_conf=email_conf)
