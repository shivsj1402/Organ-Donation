from organdonationwebapp import hc


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


    def registerHospital(self):
        # self.encrypted_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        if(hc.hospitalRegistration(self.hospitalName, self.emailID, self.phone, self.address, self.province, self.city, self.password, self.data)):
            return True
        else:
            return False
            

    def loginHospital(self):
        try:
            result = hc.hospitalLoginAuthentication(self.emailID,self.password)
            if(result):
                return result
            else:
                return None
        except Exception as err:
            print(err)
            return None


#Adding factory for complex operation of initialization of hospital and validating certificate
def construct_Hospital(cls,hospitalJson,certificate):
    hosp = cls()
    hosp.initialize(hospitalJson,certificate)
    #validate certificate to add here
    return hosp
