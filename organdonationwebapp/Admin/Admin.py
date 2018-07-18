from organdonationwebapp import ac

class Admin(object):
    def __init__(self,adminJson):
        self.emailID = adminJson['emailID'] if 'emailID' in adminJson else None
        self.password = adminJson['password'] if 'password' in adminJson else None


    def loginAdmin(self):
        if(ac.adminLoginAuthentication(self.emailID, self.password)):
            return True
        else:
            return False