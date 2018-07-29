from organdonationwebapp import duc


class ShowDonorRequestStatus(object):
    def __init__(self,hospitalEmail,donorEmail):
        self.hospitalEmail = hospitalEmail
        self.donorEmail = donorEmail


    def getRequestsStatus(self):
        try:
            request_status_data = duc.getOpenRequestsStatus(self.hospitalEmail,self.donorEmail)
            request_data = {"approved": [], "pending": []}
            if(request_status_data):
                for item in request_status_data:
                    if(item[5] == 1):
                        request_data["approved"].append(item)
                    elif(item[5] == 0 or item[5] == ""):
                        request_data["pending"].append(item)
            return request_data
        except Exception as err:
            return None