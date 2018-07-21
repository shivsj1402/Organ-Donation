import organdonationwebapp.Hospital.Hospital as ho
import organdonationwebapp.Admin.Admin as ao
import organdonationwebapp.User.User as us

class UserTypeFactory(object):
    def __init__(self,Json,certificate= None, usertype= None):
        self.certificate = certificate
        self.usertype = usertype
        self.json = Json

    def createObject(self):
        if(self.usertype == "Hospital"):
            return ho.build_Hospital(ho.Hospital, self.json, self.certificate)
        elif(self.usertype == "Donor or Receiver"):
            return us.build_User(us.User,self.json)
        elif(self.usertype == "Admin"):
            return ao.build_Admin(ao.Admin,self.json)
        else:
            return None