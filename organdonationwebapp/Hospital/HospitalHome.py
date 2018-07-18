from organdonationwebapp import hc

class HospitalHome(object):
    def __init__(self,emailID):
        self.hospitalEmail = emailID
            

    def getHospitalName(self):
        hospital_name = hc.getHospitalName(self.hospitalEmail)
        if(hospital_name):
            return hospital_name
        else:
            return None