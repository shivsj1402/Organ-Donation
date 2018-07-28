from organdonationwebapp import ac

class DeleteHospital(object):
    def __init__(self,emailID):
        self.hospitalEmail = emailID
            

    def deleteHospital(self):
        try:
            if(ac.deleteHospital(self.hospitalEmail)):
                print("Hospital",(self.hospitalEmail),"deleted successfully")
                return True
            else:
                print("Error deleting hospital",(self.hospitalEmail))
                return False
        except Exception as err:
            print(err)
            return False