
import organdonationwebapp.API.UserTypeFactory as factory

class Authenticator(object):
    def __init__(self,loginJson):
        self.usertype = loginJson['logintype'] if 'logintype' in loginJson else None
        self.email = loginJson['emailID'] if 'emailID' in loginJson else None
        self.password = loginJson['password'] if 'password' in loginJson else None
        self.json = loginJson

    def validateLogin(self):
        objectFactory = factory.UserTypeFactory(self.json,None, self.usertype)
        inst = objectFactory.createObject()
        valid, url = inst.login()
        return valid, url