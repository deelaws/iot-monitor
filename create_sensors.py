from mod_app.app import db, create_app
from mod_sensor.models import Sensor
from mod_sensor.sensor_types import SensorType

import uuid


app = create_app('development')

sensors_to_add = [  ('Room Fan Switch', SensorType.SWITCH),
                    ('Backyard Rain Sensor', SensorType.RAIN),
                    ('Outdoor Temperature Sensor', SensorType.TEMPERATURE),
                    ('Kitchen Smoke Sensor', SensorType.SMOKE)]

def create_sample_sensor():
    for s in sensors_to_add:
        # Generate a sensor-id
        new_guid = uuid.uuid4().hex
        new_sensor = Sensor(s[0], new_guid, s[1])
        print("Adding new sensor: \'%s\', id: \'%s\'" % (s[0], s[1]))
        db.session.add(new_sensor)

    db.session.commit()        

def refresh_db():
    with app.app_context():
        db.drop_all()
        #db.create_all()
        #create_sample_sensor()

if __name__ == "__main__":
    refresh_db()