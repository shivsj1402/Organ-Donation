from organdonationwebapp import uc

class OpenRequestDetails(object):
    def __init__(self,requestID):
        self.requestID = requestID

    def getOpenRequestData(self):
        request_userdata = uc.organRequest(self.requestID)
        if(request_userdata):
            return request_userdata
        else:
            return None