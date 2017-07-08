from flask_sqlalchemy import SQLAlchemy
from flask import url_for

from mod_app.app import db
from mod_app.models import Base, IoTDevice, BaseIotData

from mod_sensor.sensor_types import SensorType
from mod_sensor.data_parsers import *

class Sensor(IoTDevice):
    __tablename__ = 'iot_sensor'

    sensor_type = db.Column(db.Enum(SensorType), nullable=False)

    def __init__(self, name, id, stype):
        self.device_name = name
        self.device_id = id
        self.sensor_type = stype

    @staticmethod
    def get_sensor(id):
        return Sensor.query.filter_by(device_id=id).first()

'''
Stores the data for all sensors. 

NOTE:
This will be split into seperate tables for each specific Sensor.
A generic SensorData will be there for custom Sensors.
'''
class TemperatureSensorData(BaseIotData):
    __tablename__ = 'temperature_data'
    id = db.Column(db.Integer, primary_key=True)

    '''
    All temperature value is stored in ceclius units
    '''
    temperature = db.Column(db.Float, nullable=False)

    #Each data entry is associated with a sensor.
    sensor_id = db.Column(db.Integer, db.ForeignKey('iot_sensor.id'))
    sensor = db.relationship('Sensor', backref="temperatue_data")

    def __init__(self, temp):
        self.temperature = temp

    @staticmethod
    def add_data(req_json):
        temp = req_json['temperature']
        unit = req_json['unit'] 
        if unit != 'C' and unit != 'F':
            return (False, "Incorrect temperature unit")
        else:
            if (unit == "F"):
                # TODO: convert units to ceclius since all
               #      temperature data is stored in celcius
                unit = unit
              
            sensor = Sensor.get_sensor(req_json["device_id"])
            sensor_data = TemperatureSensorData(temp)
            sensor.temperatue_data.append(sensor_data)
            
            db.session.add(sensor)
            db.session.commit()

            return (True, "Upload Success")

'''

'''
class RainSensorData(BaseIotData):
    __tablename__ = 'rain_data'

    id = db.Column(db.Integer, primary_key=True)

    rain_data = db.Column(db.Float, nullable=False)

    #Each data entry is associated with a sensor.
    sensor_id = db.Column(db.Integer, db.ForeignKey('iot_sensor.id'))
    sensor = db.relationship('Sensor', backref="rain_data")


