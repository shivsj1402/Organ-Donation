from organdonationwebapp import ac

class ValidateHospital(object):
    def __init__(self,hospitalJson, logger):
        self.hospitalEmail = hospitalJson['validate'] if 'validate' in hospitalJson else None
        self.logger = logger
            

    def updateValidateHospitalFlag(self):
        if(ac.validateHospital(self.hospitalEmail, self.logger)):
            return True
        else:
            return False