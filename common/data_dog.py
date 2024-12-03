# import json
# import logging

# from datadog_api_client import ApiClient, Configuration
# from datadog_api_client.v2.api.logs_api import LogsApi
# from datadog_api_client.v2.model.content_encoding import ContentEncoding
# from datadog_api_client.v2.model.http_log import HTTPLog
# from datadog_api_client.v2.model.http_log_item import HTTPLogItem
# from datetime import datetime
# import os
# from urllib.parse import urlparse

# DATA_DOG_API_KEY = os.environ.get('DATA_DOG_API_KEY')


# def data_dog_body(request, _response, time_diff):
#     """
#         Insert log in Data-Dog
#     """
#     payload = request.form or request.get_json()
#     try:
#         header_json = dict(request.headers)
#     except Exception as e:
#         print("data_dog_body header json error -->", e)
#         header_json = {}

#     o = urlparse(request.base_url)

#     status = "INFO"
#     _response = json.loads(_response[0])
#     if not _response.get("success"):
#         status = "Error"
#     api_url = request.url
#     if "healthcheck" in api_url:
#         print("healthcheck")
#         return True
#     # print('response code', _response.get("code"))
#     try:
#         if int(_response.get("code")) != 500:
#             level = "INFO"
#         else:
#             level = "ERROR"
#     except Exception as e:
#         print("data_dog_body response code error -->", e)
#         level = "INFO"
#     param_dict = dict(request.args)
#     error_message = _response.get("error")
#     body = HTTPLog(
#         [
#             HTTPLogItem(
#                 function_name=request.endpoint,
#                 ddsource="Python",
#                 ddtags="env:pms,version:1.0.0,docker:base",
#                 hostname=o.hostname,
#                 source=request.headers.get('User-Agent'),
#                 url=request.url,
#                 service="PMS-User",
#                 message="",
#                 method=request.method,
#                 level=level,
#                 payload=json.dumps(payload, sort_keys=True, indent=4),
#                 header=json.dumps(header_json, sort_keys=True, indent=4),
#                 response=json.dumps(_response, sort_keys=True, indent=4),
#                 parameter=json.dumps(param_dict, sort_keys=True, indent=4),
#                 status=str(status),
#                 status_code=str(_response.get("code")),
#                 error_message=str(error_message),
#                 response_message=str(_response.get("message")),
#                 error_code=str(_response.get("error_code")),
#                 date=str(datetime.now()),
#                 duration=f"{(round(time_diff, 2))} ms",
#             ),
#         ]
#     )
#     configuration = Configuration()
#     configuration.api_key["apiKeyAuth"] = DATA_DOG_API_KEY

#     api_mode = os.environ.get("MODE", "LOCAL")
#     # print('datadog------------>',body)
#     if api_mode == "LIVE":
#         with ApiClient(configuration) as api_client:
#             api_instance = LogsApi(api_client)
#             api_instance.submit_log(content_encoding=ContentEncoding.DEFLATE, body=body)
#         return True
