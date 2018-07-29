from organdonationwebapp import ac

class ViewCertificate(object):
    def __init__(self,email):
        self.hospitalEmail = email
            

    def getHospitalCerti(self):
        Result = ac.getHospitalCertificate(self.hospitalEmail)
        if(Result):
            return Result
        else:
            return "No ertificate Found"