from organdonationwebapp import ac

class DeleteHospital(object):
    def __init__(self,emailID, logger):
        self.hospitalEmail = emailID
        self.logger = logger
            
    def deleteHospital(self):
        try:
            self.logger.info("deleteHospital logger initiliazed")
            if(ac.deleteHospital(self.hospitalEmail, self.logger)):
                self.logger.info("Hospital " + self.emailID + " deleted Successfully." )
                return True
            else:
                self.logger.Error("Issue in deleting hospital")
                print("Error deleting hospital",(self.hospitalEmail))
                return False
        except Exception as err:
            self.logger.error(err)
            return False