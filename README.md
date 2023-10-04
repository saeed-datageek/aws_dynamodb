Steps to Create a Simple RESTful API:
1. DynamoDB Table Creation:
To initiate the creation of a basic RESTful API, the first step involves creating a DynamoDB table 
named 's.azad_device_table.' DynamoDB, being a non-relational database with a key-value structure, requires 
the initial definition of a primary key (partition key). Additional keys can be added later, and the table can be created manually 
in the AWS console or with the Boto3 SDK in Python. I created it in python named create_dynomodb.py.
2. Lambda Functions Setup:
Following the creation of DynamoDB, two Lambda functions are established. The first, 'sazad-lambda-get-device,' is dedicated to handling GET requests.
The second, 's_azad_lambda_device,' is designed for response requests. The Python codes for these functions are available in 'put_device_data.py' and 
'get_device_data.py.' Due to their dependencies, these functions are bundled with the required libraries in a zipped format.
While considering the implementation of Zappa for real-world projects, I currently lack the necessary permissions to make changes in IAM.
AWS API Gateway Configuration:
Upon the creation of the DynamoDB table and Lambda functions, an AWS API Gateway,
named 's.azad-api-device,' is configured. This API Gateway is designed with two distinct actions: 'GET' and 'Post,' 
facilitating seamless communication with the associated Lambda functions.


