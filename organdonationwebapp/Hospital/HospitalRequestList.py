from organdonationwebapp import hc

class HospitalRequestList(object):
    def __init__(self,emailID):
        self.hospitalEmail = emailID

    def getPendingRequestList(self):
        request_list = hc.getHospitalRequestList(self.hospitalEmail)
        if(request_list):
            return request_list