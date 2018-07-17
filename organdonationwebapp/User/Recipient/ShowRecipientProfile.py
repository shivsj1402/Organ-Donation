from organdonationwebapp import ruc

class ShowRecipientProfile(object):
    def __init__(self,recipientEmail):
        self.recipientEmail = recipientEmail

    def getRecipientProfile(self):
        recipient_data = ruc.receiverHospitalShowProfile(self.recipientEmail)
        if(recipient_data):
            return recipient_data
        else:
            return None

    def getRecipientOrgans(self):
        recipient_organ_data = ruc.receiverHospitalShowOrgan(self.recipientEmail)
        if(recipient_organ_data):
            return recipient_organ_data
        else:
            return None