"""
lambda deploy
"""

from __future__ import print_function
import boto3

WATCH = [{'bucket'  : 'ask-ava',
          'key'     : 'ask-ava.zip',
          'function': 'ask-ava'
         }]

def lambda_handler(event, context):
    """ lambda handler """
    status = None
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']

    client = boto3.client('lambda')

    for item in WATCH:
        if bucket in item['bucket'] and key in item['key']:
            response = client.update_function_code(
                FunctionName=item['function'],
                S3Bucket=item['bucket'],
                S3Key=item['key']
            )
            status = True
    return status
