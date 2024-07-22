# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
import jmespath

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('HelloWorldDatabase')

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    word = event['word']
# write name and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.scan()
    items = response['Items']
    query = "[?contains(ID, '{}')]".format(word)
    filtered_items = jmespath.search(query, items)
# return a properly formatted JSON object
    return filtered_items