3.AWS API Gateway Configuration:
Upon the creation of the DynamoDB table and Lambda functions, an AWS API Gateway,
named 's.azad-api-device,' is configured. This API Gateway is designed with two distinct actions: 'GET' and 'Post,' 
facilitating seamless communication with the associated Lambda functions.
4.Test Script Creation:
A Python file named 'test_api_working' is created for testing purposes. It contains four unit tests that can be executed using either python -m unittest test_api_working.py or python -m pytest.
