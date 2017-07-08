from flask import Blueprint, request

from mod_app.app import db

from mod_sensor.models import Sensor,TemperatureSensorData
from mod_sensor.sensor_types import SensorType
from mod_sensor.exceptions import InvalidInput

mod_sensor = Blueprint('sensor', __name__, url_prefix='/sensor')


'''
print(request.__dict__)
print(request.headers)
print(request.data)
print(request.get_json())
'''

@mod_sensor.route('/create', methods=['GET', 'POST'])
def create_sensor():
    # TODO: 
    return "TODO: create new sensor"

@mod_sensor.route('/data/upload', methods=['POST'])
def sensor_upload_data():
    print('Received request to upload data...')
    ret = ()

    # TODO: verify common data shared by all sensor types
    #       that is needed to upload data.

    # Get Sensor Type!
    r_json = request.get_json()

    stype = SensorType.get_type_from_string(r_json["sensor_type"])
    
    if stype == SensorType.TEMPERATURE:
        ret = TemperatureSensorData.add_data(r_json)
    else:
        print("temperature not supported")

    print(stype.value)

    if not ret[0]:
        raise InvalidInput(ret[1])
    
    return ret[1], 200

@mod_sensor.route('/data/download', methods=['GET'])
def sensor_download_data():
    return "TODO: download sensor data"

@mod_sensor.route('/status', methods=['GET'])
def check_sensor_status():
    return "TODO: Get sensor status"