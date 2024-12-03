import requests
import json


def post_request(url, data, headers=dict()):
    """
    Third party call
    """
    print('post request')
    print('post request url', url)
    print('post request data', data)
    print('post request headers', headers)
    result = None
    try:
        res = requests.post(url=url, json=json.dumps(data), headers=headers)
        result = res.json() if res.status_code == 200 else None
    except Exception as e:
        print("post_request", e)
    return result


def put_request(url, data, headers=dict()):
    """
    Third party call
    """
    print('put request')
    print('put request url', url)
    print('put request data', data)
    print('put request headers', headers)
    result = None
    try:
        res = requests.put(url=url, json=data, headers=headers)
        result = res.json() if res.status_code == 200 else None
        print('put request result', result.text)
    except Exception as e:
        print("put_request", e)

    return result
