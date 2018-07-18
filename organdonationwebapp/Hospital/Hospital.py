from organdonationwebapp import hc
import bcrypt

class Hospital(object):
    def __init__(self,hospitalJson,certificateFile=None):
        self.hospitalName = hospitalJson['hospitalName'] if 'hospitalName' in hospitalJson else None
        self.emailID = hospitalJson['emailID'] if 'emailID' in hospitalJson else None
        self.phone = hospitalJson['phone'] if 'phone' in hospitalJson else None
        self.address = hospitalJson['address'] if 'address' in hospitalJson else None
        self.province = hospitalJson['province'] if 'province' in hospitalJson else None
        self.city = hospitalJson['city'] if 'city' in hospitalJson else None
        self.password = hospitalJson['password'] if 'password' in hospitalJson else None
        self.data = certificateFile


    def registerHospital(self):
        self.encrypted_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        if(hc.hospitalRegistration(self.hospitalName, self.emailID, self.phone, self.address, self.province, self.city, self.encrypted_password, self.data)):
            return True
        else:
            return False
            

    def loginHospital(self):
        result = hc.hospitalLoginAuthentication(self.emailID)
        if(result):
            if(bcrypt.checkpw(self.password.encode('utf-8'), result[0][6].encode('utf-8'))):
                return result
            else:
                return None