from mod_app.app import db, create_app

from mod_sensor.models import Sensor
from mod_sensor.sensor_types import SensorType
from mod_switch.models import IoTSwitch
from mod_switch.switch_types import SwitchType

import uuid


app = create_app('development')

sensors_to_add = [('Backyard Rain Sensor', SensorType.RAIN),
                  ('Outdoor Temperature Sensor', SensorType.TEMPERATURE),
                  ('Kitchen Smoke Sensor', SensorType.SMOKE)]


switches_to_add = [('Patio Lights', SwitchType.GenericSwitch),
                   ('Master Bedroom Lights', SwitchType.CeilingLight),
                   ('Study Desk Lamp', SwitchType.DeskLamp)]

def create_sample_sensors():
    for s in sensors_to_add:
        # Generate a sensor-id
        new_guid = uuid.uuid4().hex
        new_sensor = Sensor(s[0], new_guid, s[1])
        print("Adding new sensor: \'%s\', id: \'%s\'" % (s[0], s[1]))
        db.session.add(new_sensor)

    db.session.commit()

def create_sample_switches():
    for s in switches_to_add:
        new_guid = uuid.uuid4().hex
        new_switch = IoTSwitch(s[0], new_guid, s[1])
        print("Adding new switch: \'%s\', id: \'%s\'" % (s[0], s[1]))
        db.session.add(new_switch)
    
    db.session.commit()

def refresh_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_sample_sensors()
        create_sample_switches()
        

if __name__ == "__main__":
    refresh_db()
