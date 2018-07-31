from organdonationwebapp import duc


class UpdateRequestStatus(object):
    def __init__(self,request, requestID):
        self.request = request
        self.requestID = requestID


    def setRequestsStatus(self):
        try:
            requeststate = 0
            if(self.request == "Accept"):
                requeststate = 1
            else:
                requeststate = 2
            if(duc.setRequestsStatus(self.requestID, requeststate)):
                return True
            else:
                return False
        except Exception as err:
            return None