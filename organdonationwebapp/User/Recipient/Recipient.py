from organdonationwebapp import ruc


class Recipient(object):
    def __init__(self,recipientEmail):
        self.recipientEmail = recipientEmail

    def donorHospitalPageRecipientList(self):
        recipient_data = ruc.donorHospitalShowReceiverProfile(self.recipientEmail)
        if(recipient_data):
            return recipient_data
        else:
            return None