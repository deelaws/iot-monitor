import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


'''
Beta-api url: https://taunoq5we0.execute-api.us-west-2.amazonaws.com/beta/data?sensor_id=d7a21cbc-93d7-47da-ac3a-1b4b3d2cd7e4
'''

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def read_sensor_data(params):
    dynamodb = boto3.resource("dynamodb", region_name='us-west-2')

    table = dynamodb.Table('Sensors')

    # 1 == temperature sensor  
    # TODO: FIXME: get this from the events dictionary
    sensor_type = 1
    sensor_id   = params["sensor_id"]

    try:
        response = table.get_item(
            Key={
                'sensor_id': sensor_id
            }
        )
    except ClientError as e:
        logger.error(e.response['Error']['Message'])
    else:
        item = response['Item']
        logger.info("Get Sensor data  succeeded")
        return json.dumps(item, indent=4, cls=DecimalEncoder)


def lambda_handler(event, context):
    query_params = event["queryStringParameters"]
    return {"statusCode": 200, "headers": {}, "body": read_sensor_data(query_params)}
    
