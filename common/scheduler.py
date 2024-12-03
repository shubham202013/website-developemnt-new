# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()
# SCHEDULER_SERVER = os.environ.get("SCHEDULER_SERVER", "")


# def start_scheduler(key=None, data=None, delay=None):
#     """
#     start scheduler using above params
#     :param key: string
#     :param data: json
#     :param delay: int
#     :return:
#     """
#     params = {
#         "key": key,
#         "data": data,
#         "delay": delay,
#     }
#     url = SCHEDULER_SERVER + "scheduler/start"
#     print("start_scheduler url", url)
#     print("start_scheduler params", params)
#     try:
#         res = requests.post(url, json=params)
#         print("start_scheduler res", res)
#     except Exception as e:
#         print("start_scheduler error", e)
#     return True


# def stop_scheduler(key=None):
#     """
#     stop scheduler by key
#     :param key: string
#     :return: Bool
#     """

#     params = {
#         "key": key,
#     }
#     try:
#         requests.post(SCHEDULER_SERVER + "scheduler/stop", json=params)
#     except Exception as e:
#         print("stop_scheduler error", e)
#     return True
