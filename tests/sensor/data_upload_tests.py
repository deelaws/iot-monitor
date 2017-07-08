import unittest
import json
from ctypes import cdll

from mod_app.app import create_app, db
from flask import url_for
from mod_sensor.models import Sensor
from mod_sensor.sensor_types import SensorType

"""
Data upload tests

Run command:
python -m unittest tests\sensor\data_upload_tests.py
"""
class SensorDataUploadTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup Class method ")

    @classmethod
    def tearDownClass(cls):
        print("TearDown Class method")

    def setUp(self):
        self.app = create_app('development')
        # To allow assertions and errorrs to be propagated up.
        self.app.testing = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)
        self._ctx = self.app.test_request_context()
        self._ctx.push()

    def tearDown(self):
        pass

    def get_temperature_sensor(self):
        return Sensor.query.filter_by(sensor_type=SensorType.TEMPERATURE).first()

    def test_temperate_data_upload_success(self):
        print("Running Test: ", self._testMethodName)

        test_sensor = self.get_temperature_sensor()

        print(test_sensor.device_name)

        to_upload = dict(
            device_id=test_sensor.device_id,
            sensor_type=test_sensor.sensor_type.value,
            temperature=35,
            unit="C")
        
        # NOTE: Have to use json.dumps() to convert dict to a string that contains double quotes
        #       request.get_json() will not be able to get JSON request data otherwise with single
        #       quotes

        response = self.client.post(url_for('sensor.sensor_upload_data'), data=json.dumps(to_upload),
            headers={'Content-Type': 'application/json'})

        print("Http Response %s: " % response.data)
        print("Http Response Code %s:" % response.status_code)
        self.assertEqual(response.data, b"Upload Success")
        self.assertEqual(response.status_code, 200)

    def test_temperate_data_upload_failure(self):
        print("Running Test: ", self._testMethodName)

        test_sensor = self.get_temperature_sensor()

        print(test_sensor.device_name)

        to_upload = dict(
            device_id=test_sensor.device_id,
            sensor_type=test_sensor.sensor_type.value,
            temperature=35,
            unit="G")
        
        # NOTE: Have to use json.dumps() to convert dict to a string that contains double quotes
        #       request.get_json() will not be able to get JSON request data otherwise with single
        #       quotes

        response = self.client.post(url_for('sensor.sensor_upload_data'), data=json.dumps(to_upload),
            headers={'Content-Type': 'application/json'})

        print("Http Response %s: " % response.data)
        print("Http Response Code %s:" % response.status_code)

        self.assertEqual(True, "Incorrect temperature unit" in str(response.data))
        self.assertEqual(response.status_code, 400)
