from flask_sqlalchemy import SQLAlchemy
from flask import url_for

from mod_app.app import db
from mod_app.models import Base, IoTDevice, BaseIotData
from mod_switch.switch_types import SwitchType

class IoTSwitch(IoTDevice):
    __tablename__ = 'iot_switch'

    switch_type = db.Column(db.Enum(SwitchType), nullable=False)

    def __init__(self, name, id, stype):
        self.device_name = name
        self.device_id = id
        self.switch_type = stype
    
    @staticmethod
    def get_switch(id):
        return IoTSwitch.query.filter_by(device_id=id).first()


class IoTSwitchData(BaseIotData):
    __tablename__ = 'switch_data'

    id = db.Column(db.Integer, primary_key=True)

    state_change = db.Column(db.Boolean, default=None)

    sensor_id = db.Column(db.Integer, db.ForeignKey('iot_switch.id'))
    sensor = db.relationship('IoTSwitch', backref="data")

    @staticmethod
    def add_change_to_db(req_json):
        pass