from organdonationwebapp import hc

class HospitalRequestList(object):
    def __init__(self,emailID, logger):
        self.hospitalEmail = emailID
        self.logger = logger

    def getPendingRequestList(self):
        request_list = hc.getHospitalRequestList(self.hospitalEmail, self.logger)
        if(request_list):
            return request_list