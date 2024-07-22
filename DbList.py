# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('HelloWorldDatabase')

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    # DB からデータをとってきて変数に入れる
    response = table.scan()
    count = response['Count']
    items = response['Items']
    return count, items