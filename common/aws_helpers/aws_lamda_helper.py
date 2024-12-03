# import json
# import os
# import boto3

# aws_region = os.environ.get("AWS_REGION", "")
# access_key = os.environ.get("ACCESS_KEY", "")
# secret_key = os.environ.get("AWS_ACCESS_SECRET_KEY", "")


# def invoke_aws_lambda(function_name, payload):
#     """
#     invoke aws lambda function using name and payload
#     """
#     payload = json.dumps(payload)
#     client = boto3.client('lambda',
#                           region_name=str(aws_region),
#                           aws_access_key_id=str(access_key),
#                           aws_secret_access_key=secret_key)

#     # request payload
#     response = client.invoke(
#         FunctionName=str(function_name),
#         InvocationType='RequestResponse',
#         Payload=payload
#     )
#     print('invoke_aws_lambda response', response)
#     response_data = None
#     if response.get('StatusCode', '') == 200:
#         response_data = json.loads(response['Payload'].read().decode())
#     return response_data
