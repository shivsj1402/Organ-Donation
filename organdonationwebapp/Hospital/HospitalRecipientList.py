from organdonationwebapp import hc

class HospitalRecipientList(object):
    def __init__(self,hospitalName):
        self.hospitalName = hospitalName

    def getRecipientList(self):
        recipient_list = hc.getHospitalRecipientList(self.hospitalName)
        if(recipient_list):
            return recipient_list
        else:
            return None