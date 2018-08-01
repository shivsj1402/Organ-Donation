from organdonationwebapp import hc

class HospitalHome(object):
    def __init__(self,emailID):
        self.hospitalEmail = emailID
            

    def getHospitalName(self):
        try:
            hospital_name = hc.getHospitalName(self.hospitalEmail)
           
            if(hospital_name):
                return (hospital_name[0])
            else:
                return None
        except Exception as err:
            print(err)
            return None