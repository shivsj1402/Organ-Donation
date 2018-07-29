from organdonationwebapp import ac

class ValidateHospital(object):
    def __init__(self,hospitalJson):
        self.hospitalEmail = hospitalJson['validate'] if 'validate' in hospitalJson else None
            

    def updateValidateHospitalFlag(self):
        if(ac.validateHospital(self.hospitalEmail)):
            return True
        else:
            return False