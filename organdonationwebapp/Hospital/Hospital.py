from flask import url_for
from organdonationwebapp import hc
# import bcrypt

class Hospital(object):
    def initialize(self,hospitalJson,certificateFile=None):
        self.hospitalName = hospitalJson['hospitalName'] if 'hospitalName' in hospitalJson else None
        self.emailID = hospitalJson['emailID'] if 'emailID' in hospitalJson else None
        self.phone = hospitalJson['phone'] if 'phone' in hospitalJson else None
        self.address = hospitalJson['address'] if 'address' in hospitalJson else None
        self.province = hospitalJson['province'] if 'province' in hospitalJson else None
        self.city = hospitalJson['city'] if 'city' in hospitalJson else None
        self.password = hospitalJson['password'] if 'password' in hospitalJson else None
        self.data = certificateFile


    def register(self):
        # self.encrypted_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        try:
            if(hc.hospitalRegistration(self)):
                url = url_for('Login')
                return True, url
            else:
                return False, "Registration Failed."
        except Exception as err:
            print(err)
        
            

    def login(self):
        result = hc.hospitalLoginAuthentication(self.emailID)
        if(result):
            try:
                if(self.password == result[0][6]):
                    url = url_for('hospitalHome', emailID=self.emailID)
                    return result, url
                else:
                    return False, "Authentication Failed. Please register if not a registered User"
            except Exception as err:
                print(err)
                

#Adding factory for complex operation of initialization of hospital and validating certificate
def build_Hospital(cls,hospitalJson,certificate = None):
    hosp = cls()
    hosp.initialize(hospitalJson,certificate)
    #validate certificate to add here
    return hosp