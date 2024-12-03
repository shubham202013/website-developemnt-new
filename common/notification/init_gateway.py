# import io
# import json
# import mimetypes
import os
from email import encoders
# from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# from flask import current_app

# import requests
import smtplib
from email.mime.text import MIMEText

# from flask import request

# THIRD_PARTY_GATEWAY_BASE_URL = os.environ.get("THIRD_PARTY_GATEWAY_BASE_URL", "")


# def _msg_91_sms(to_number, content, conf_data):
#     """
#         This function is currently empty because the SMS functionality using the MSG91 service
#         is not yet implemented. Further development is required to integrate the SMS sending logic.
#     """
#     pass


# def _send_email(to_email_list, subject, message, email_conf):
#     """
#     send email base function
#     """
#     if email_conf:
#         import base64

#         message_bytes = message.encode('ascii')
#         message = base64.b64encode(message_bytes)
#         message = message.decode('ascii')

#         mail_host = email_conf.get('host', '')
#         mail_username = email_conf.get('username', '')
#         mail_password = email_conf.get('password', '')
#         mail_port = email_conf.get('port', 0)
#         from_email = email_conf.get('from_email', '')
#         url = f"{THIRD_PARTY_GATEWAY_BASE_URL}/email/send"

#         body_data = {
#             "subject": subject,
#             "content": message,
#             "to_email": ",".join(to_email_list),
#             "mail_host": mail_host,
#             "mail_username": mail_username,
#             "mail_password": mail_password,
#             "mail_port": int(mail_port),
#             "from_email": from_email,
#         }
#         post_request(url, body_data)
#     return True


def _send_email_common(to_email_list, subject, message, email_conf, attachments=None):
    """
    send email base function
    """
    print("email_conf", email_conf)
    f_host = email_conf.get('host')
    f_port = email_conf.get('port')
    f_user = email_conf.get('username')
    f_passwd = email_conf.get('password')

    smtpserver = smtplib.SMTP(f_host, f_port)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    print("f_user", f_user)
    print("f_passwd", f_passwd)
    smtpserver.login(f_user, f_passwd)  # from email credential
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = email_conf.get('from_email')
    msg['To'] = ','.join(to_email_list)

    body_text = MIMEText(message, 'html')
    msg.attach(body_text)

    # add attachments if any
    if attachments:
        print('attachments------->', attachments)
        with open(attachments, "rb") as attachment:
            # Add file as application/octet-stream
            # Email clients can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(attachments)}",
        )

        # Add attachment to message and convert message to string
        msg.attach(part)
        os.remove(attachments)

    for t in to_email_list:
        smtpserver.sendmail(f_user, t, msg.as_string())  # you just need to add
        # this in for loop in
        # your code.
    smtpserver.close()
    print('Mail is sent successfully!!')
    return True


# def _send_push(device_id, device_type, server_key, body):
#     """
#     send push notification to device
#     """
#     url = f"{THIRD_PARTY_GATEWAY_BASE_URL}/push/send"
#     body_data = {
#         "device_id": device_id,
#         "body": json.dumps(body),
#         "serverKey": server_key,
#         "device_type": device_type
#     }
#     print('\n\n\n')
#     print('_send_push >>>>>')
#     print('url', url)
#     print('body_data', body_data)
#     print('\n\n\n')
#     post_request(url, body_data)
#     return True


# def post_request(url, body):
#     """
#     common post request
#     """
#     print('external post_request url', url)
#     print('external post_request body', body)
#     result = None
#     try:
#         headers = {
#             'Content-Type': 'application/json'
#         }
#         result = requests.post(url=url, json=body, headers=headers)
#     except Exception as e:
#         print("post_request", e)
#     return result
