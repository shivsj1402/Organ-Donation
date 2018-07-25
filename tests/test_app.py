from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from flask import current_app
import unittest
import organdonationwebapp.API.Logger as log
import json
import organdonationwebapp.Hospital.Hospital as hc

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.logger = log.MyLogger.__call__().get_logger()
        self.json = json.loads('{"logintype": "Hospital", "emailID": "iwk@gmail.com", "password": "123456789", "submit": "submit", "type": "Donor or Receiver"}')
        
         
    def test_hospital_builder(self):
        obj = hc.build_Hospital(hc.Hospital, self.json,self.logger, None)
        self.assertIsNotNone(obj)

    def test_hospital_login_success(self):
        with current_app.app_context():
        	obj = hc.build_Hospital(hc.Hospital, self.json,self.logger, None)
        	result, url = obj.login()
        	self.assertTrue(result)

    def test_hospital_login_fail(self):
        obj = hc.build_Hospital(hc.Hospital, self.json,self.logger, None)
        obj.password = "Error"
        result, url = obj.login()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.result

	 #suite = unittest.TestLoader().loadTestsFromTestCase(hc.TestStringMethods)
	 #unittest.TextTestRunner(verbosity=2).run(suite)