from organdonationwebapp import uc

class UpdateMedicalReports(object):
    def __init__(self,emailID,UserType,reports):
        self.emailID = emailID
        self.reports = reports
        self.userType = UserType

    def updateReports(self):
        if(uc.updateReport(self.emailID, self.userType, self.reports)):
            return True
        else:
            return False