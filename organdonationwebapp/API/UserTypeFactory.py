import organdonationwebapp.Hospital.Hospital as ho
import organdonationwebapp.Admin.Admin as ao
import organdonationwebapp.User.User as us

class UserTypeFactory(object):
    def __init__(self,Json):
        self.logintype = Json['logintype'] if 'logintype' in Json else None
        self.json = Json

    def createObject(self):
        if(self.logintype == "hospital"):
            return ho.build_Hospital(ho.Hospital, self.json, None)
        elif(self.logintype == "admin"):
            return ao.build_Admin(ao.Admin,self.json)
        elif(self.logintype == "donor" or self.logintype == "receiver"):
            return us.build_User(us.User,self.json)
        else:
            return None