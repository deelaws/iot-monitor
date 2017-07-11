
from flask_sqlalchemy import SQLAlchemy
from mod_app.app import db

# Define a base model for other database tables to inherit

'''
User's ip-address used for logging and monitoring.
'''
def remote_addr():
    return request.remote_addr


class Base(db.Model):

    __abstract__ = True

    '''
    Lets the models that inherit define their own primary key
    '''
    id = db.Column(db.Integer, primary_key=True)

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

'''
Base model for all IoT devices.
It has all the common properties/attributes shared by all IoT devices
'''
class IoTDevice(Base):
    __abstract__ = True

    device_name = db.Column(db.String(30), nullable=False)

    '''
    Device ID is a 32 byte unique GUID.
    '''
    device_id   = db.Column(db.String(32),  unique=True, nullable=False)

    '''
    By default, every iot-device is de-activated for now.
    '''
    active = db.Column(db.Boolean, default=False)

    '''
    Device is either indoor or outdoor.
    '''
    indoor = db.Column(db.Boolean, default=True)

    # TODO: perhaps more location specific data? Geo-co-ordinates

'''
Base model for all type of IoT device data to be stored.

'''
class BaseIotData(db.Model):
    __abstract__ = True
    date_recorded = db.Column(db.DateTime, default=db.func.current_timestamp())

    remote_ip = db.Column(db.String(24), default=remote_addr)
