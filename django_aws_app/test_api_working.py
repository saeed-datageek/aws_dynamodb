import requests
import boto3
import json
import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock, patch
url = "https://wccpepyaod.execute-api.eu-north-1.amazonaws.com/development/api/devices"

# data = {
#     "body":{
#     "id":"d3",
#     "deviceModel":"modelDomestic",
#     "name":"deviceThere",
#     "note":"eco",
#     "serial":"A32111"
# }
# }
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('s.azad_device_table')


# write unit test to post request, missing field failure, failure id  and get request

class TestApi(unittest.TestCase):

    def test_get_device_fail(self):

        params = {"id":"d5"}
        response = requests.get(url, params=params)

        print(response.json())
        expected_response = {'message': 'Item with ID d5 not found.'}
        assert response.status_code==404
        assert expected_response==response.json()

    def test_get_device_success(self):
        params = {"id":"d4"}
        response = requests.get(url, params=params)
        expected_response = {'deviceModel': 'modelHome', 'note': 'eco', 'id': 'd4', 'name': 'device4', 'serial': 'A42441'}
        print(response.json())
        assert response.status_code==200
        assert expected_response==response.json()

    def test_create_device_missing_field(self):
        data = {'body': {'id': 'd6', 'deviceModel': 'modelDomestic','note':"affordable model"}}
        response = requests.post(url, json=data)
        expected_response = {'statusCode': 400, 'body': '{"error is ": "Missing required fields: name, serial"}'}

        print(response.json())
        assert expected_response==response.json()


    ##mocking_creatig_device in dynamodb table
    @patch('requests.post')
    def test_create_device_success_mock(self, mock_post):
        data = {"body":{ "id":"d7", "deviceModel":"modelIndustry", "name":"deviceseven","note":"eco", "serial":"A77111"}}

        expected_response = {'statusCode': 201, 'body': '{"message": "Item created successfully"}'}
        mock_response = MagicMock()
        mock_response.json.return_value = expected_response
        mock_response.status_code = 201


        mock_post.return_value = mock_response

        response = requests.post(url, json=data)
        result_json, result_status_code = response.json(),response.status_code

        # Assert
        self.assertEqual(result_status_code, 201)
        assert expected_response==response.json()
        mock_post.assert_called_once_with(url, json=data)
        print(response.json())


    # Comment to avoid adding new data

    # def test_create_device_success_real(self):
    #     data = {"body":{ "id":"d8","deviceModel":"ModelEight", "name":"deviceEight","note":"eco", "serial":"A88111"}}
    #     response = requests.post(url, json=data)
    #     expected_response = {'statusCode': 201, 'body': '{"message": "Item created successfully"}'}
    #     assert expected_response == response.json()





if __name__ == '__main__':
    unittest.main()