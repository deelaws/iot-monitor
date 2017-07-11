import unittest
import json
from ctypes import cdll

from mod_app.app import create_app, db
from flask import url_for
from mod_switch.models import IoTSwitch
from mod_switch.switch_types import SwitchType

"""
Data upload tests

Run command:
python -m unittest tests\switch\switch_onoff_tests.py
"""
class SwitchOnOffTests(unittest.TestCase):

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

    def get_lightbulb_switch(self):
        return Sensor.query.filter_by(switch_type=SwitchType.CeilingLight).first()

    def switch_state_change_success(self):
        print("Running Test: ", self._testMethodName)

        test_sensor = self.get_lightbulb_switch()
