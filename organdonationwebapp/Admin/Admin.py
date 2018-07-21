from flask import url_for
from organdonationwebapp import ac

class Admin(object):
    def initialize(self,adminJson):
        self.emailID = adminJson['emailID'] if 'emailID' in adminJson else None
        self.password = adminJson['password'] if 'password' in adminJson else None

    def register(self):
        return NotImplementedError

    def login(self):
        if(ac.adminLoginAuthentication(self.emailID, self.password)):
            url = url_for('adminHomepage', username=self.emailID)
            return True, url
        else:
            return False, "Authentication Failed. Please register if not a registered User"

def build_Admin(cls,adminJson):
    admin = cls()
    admin.initialize(adminJson)
    #validate certificate to add here
    return admin