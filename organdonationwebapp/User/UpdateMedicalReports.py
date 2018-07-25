from organdonationwebapp import uc

class UpdateMedicalReports(object):
    def __init__(self,emailID,reports,UserType):
        self.emailID = emailID
        self.reports = reports
        self.userType = UserType

    def updateReports(self):
        if(uc.updateReport(self.emailID, self.reports, self.userType)):
            return True
        else:
            return False