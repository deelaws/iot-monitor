import boto3
import json
import decimal
import datetime
import random

from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

def get_utc_ticks_from_epoch():
    dt = datetime.datetime.now()
    return unix_time_millis(dt)

def put_temperate_sensor_data(params):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table('Sensors')

    # 1 == temperature sensor
    sensor_type = 1 
    sensor_id   = params["sensor_id"]
    temper = params["temperature"]

    response = table.put_item(
    Item={
            'sensor_type': sensor_type,
            'sensor_id': sensor_id,
            'data': {
                'unit': "C",
                'temp': temper,
                # For now just store the current utc time tick
                # Later on, get it from the device.
                'utc-time': decimal.Decimal(get_utc_ticks_from_epoch())
            }
        }
    )

def lambda_handler(event, context):
    query_params = event["queryStringParameters"]
    put_temperate_sensor_data(query_params)
    return {"headers": {}, "statusCode": 200, "body": "Sensor data successfully stored"}
