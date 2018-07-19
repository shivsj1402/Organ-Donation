from organdonationwebapp import hc

class ValidateHospital(object):
    def __init__(self,hospitalJson):
        self.hospitalEmail = hospitalJson['validate'] if 'validate' in hospitalJson else None
            

    def updateValidateHospitalFlag(self):
        if(hc.validateHospital(self.hospitalEmail)):
            return True
        else:
            return False