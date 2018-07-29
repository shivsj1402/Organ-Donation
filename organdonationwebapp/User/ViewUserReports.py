from organdonationwebapp import uc

class ViewUserReports(object):
    def __init__(self,emailID,UserType):
        self.emailID = emailID
        self.userType = UserType

    def viewReports(self):
        result = uc.getReports(self.emailID, self.userType)
        if(result):
            return result
        else:
            return None