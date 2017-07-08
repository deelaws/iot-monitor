from flask_sqlalchemy import SQLAlchemy
from flask import url_for

from mod_app.app import db
from mod_app.models import Base, IoTDevice, BaseIotData



class IoTSwitch(IoTDevice):
    __tablename__ = 'iot_switch'
