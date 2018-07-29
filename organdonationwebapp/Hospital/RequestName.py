from organdonationwebapp import hc

class RequestName(object):
    def __init__(self,emailID,hospitalName):
        self.hospitalEmail = emailID
        self.hospitalName = hospitalName

    def getRequestListName(self):
        request_list = hc.getRequestName(self.hospitalEmail, self.hospitalName)
        if(request_list):
            return request_list
        else:
            return None    