from flask import url_for
from organdonationwebapp import hc
import base64


class Hospital(object):
    def initialize(self,hospitalJson,certificateFile=None):
        self.hospitalName = hospitalJson['hospitalName'] if 'hospitalName' in hospitalJson else None
        self.emailID = hospitalJson['emailID'] if 'emailID' in hospitalJson else None
        self.phone = hospitalJson['phone'] if 'phone' in hospitalJson else None
        self.address = hospitalJson['address'] if 'address' in hospitalJson else None
        self.province = hospitalJson['province'] if 'province' in hospitalJson else None
        self.city = hospitalJson['city'] if 'city' in hospitalJson else None
        passwrd = hospitalJson['password'] if 'password' in hospitalJson else None
        self.password = base64.b64encode(passwrd.encode())
        self.data = certificateFile

    
    def register(self):
        try:
            if(hc.hospitalRegistration(self)):
                url = url_for('Login')
                return True, url
            else:
                return False, "Registration Failed."
        except Exception as err:
            print(err)
        
            

    def login(self):
        result = hc.hospitalLoginAuthentication(self.emailID,self.password)
        if(result):
            url = url_for('hospitalHome', emailID=self.emailID)
            return result, url
        else:
            return False, "Authentication Failedr"
                


#Adding factory for complex operation of initialization of hospital and validating certificate
def build_Hospital(cls,hospitalJson,certificate = None):
    hosp = cls()
    hosp.initialize(hospitalJson,certificate)
    #validate certificate to add here
    return hosp
