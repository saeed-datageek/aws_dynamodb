import os
import json
import boto3
from botocore.exceptions import NoCredentialsError
from django.core.management import execute_from_command_line
from django.conf import settings



# os.environ.setdefault("DJANGO_SETTINGS_MODULE",'settings')
# settings.configure()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('s.azad_device_table')

data = {
    "body":{
        "id":"d8",
        "deviceModel":"modelDomestic",
        "name":"deviceEight",
        "note":"eco",
        "serial":"A88111"
    }
}

import requests
def create_device(event, context):
    try:
        data = event['body']
        required_fields = ["id", "deviceModel", "name", "note", "serial"]

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
        response = table.put_item(Item=data)
        return {
            'statusCode': 201,
            'body': json.dumps({"message": "Item created successfully"})
        }

    except ValueError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({"error is ": str(e)})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error is ": str(e)})
        }


# For local testing
if __name__ == '__main__':
    execute_from_command_line(['manage.py', 'runserver'])
