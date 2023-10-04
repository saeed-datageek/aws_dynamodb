import boto3
import json

dynamodb = boto3.resource('dynamodb')


table = dynamodb.Table('s.azad_device_table')

id_param_output= {"queryStringParameters":{"id":"d1"}}
def get_data(event, context):
    try:

        id_param = event['queryStringParameters']['id']

        if not id_param:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'The "id" parameter is missing in the query string.'})
            }

        # get data from dynamodb table
        item = table.get_item(Key={'id': id_param})

        if 'Item' not in item:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': f'Item with ID {id_param} not found.'})
            }

        return {
            'statusCode': 200,
            'body': json.dumps(item['Item'])
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }