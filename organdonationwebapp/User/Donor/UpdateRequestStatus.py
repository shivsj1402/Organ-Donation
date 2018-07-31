from organdonationwebapp import duc


class UpdateRequestStatus(object):
    def __init__(self,request, requestID):
        self.request = request
        self.requestID = requestID


    def setRequestsStatus(self):
        try:
            requeststate = 0        # 0 for any new pending requests
            if(self.request == "AcceptDonor"):
                requeststate = 1    # 1 for requests accepted by Donors but pending at recipient's end for approval
            elif(self.request == "DeclineDonor"):
                requeststate = 2    # 2 for requests rejected by Donors
            elif(self.request == "AcceptRecipient"):
                requeststate = 3    # 3 for requests accepted by both Donor and Recipient
            elif(self.request == "DeclineRecipient"):
                requeststate = 4    # 4 for requests rejected by Donors
            if(duc.setRequestsStatus(self.requestID, requeststate)):
                return True
            else:
                return False
        except Exception as err:
            return None