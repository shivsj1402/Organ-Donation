<<<<<<< HEAD
'''
from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from flask import current_app
=======
from flask import Flask
from flask import app
>>>>>>> 3a14e22dab98c817f23ba4b3169320b72427abd5
import unittest
import organdonationwebapp.API.Logger as log
import json
import organdonationwebapp.Hospital.Hospital as hc
import organdonationwebapp.Admin.Admin as adm

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.logger = log.MyLogger.__call__().get_logger()
        self.hospitaljson = json.loads('{"logintype": "Hospital", "emailID": "iwk@gmail.com", "password": "123456789", "submit": "submit", "type": "Donor or Receiver"}')
        self.adminJson = json.loads('{"logintype": "Admin", "emailID": "shivsj1402@gmail.com", "password": "123456", "submit": "submit", "type": "Donor or Receiver"}')
        
         
    def test_hospital_builder(self):
        obj = hc.build_Hospital(hc.Hospital, self.hospitaljson,self.logger, None)
        self.assertIsNotNone(obj)

    def test_hospital_login_success(self):
        # with app.AppContext:
        	obj = hc.build_Hospital(hc.Hospital, self.hospitaljson,self.logger, None)
        	result, url = obj.login()
        	self.assertTrue(result)

    def test_hospital_login_fail(self):
        obj = hc.build_Hospital(hc.Hospital, self.hospitaljson,self.logger, None)
        obj.password = "Error"
        result, url = obj.login()
        self.assertFalse(result)

    def test_admin_builder(self):
        obj = adm.build_Admin(adm.Admin, self.adminJson, self.logger)
        self.assertIsNotNone(obj)

    def test_admin_login_success(self):
        	obj = adm.build_Admin(adm.Admin, self.adminJson, self.logger)
        	result, url = obj.login()
        	self.assertTrue(result)

    def test_admin_login_fail(self):
        obj = adm.build_Admin(adm.Admin, self.adminJson, self.logger)
        obj.password = "Error"
        result, url = obj.login()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.result

	 #suite = unittest.TestLoader().loadTestsFromTestCase(hc.TestStringMethods)
	 #unittest.TextTestRunner(verbosity=2).run(suite)
     '''
