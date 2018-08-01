from organdonationwebapp import ruc


class Recipient(object):
    def __init__(self,recipientEmail,logger):
        self.recipientEmail = recipientEmail
        self.logger = logger

    def donorHospitalPageRecipientList(self):
        recipient_data = ruc.donorHospitalShowReceiverProfile(self.recipientEmail,self.logger)
        if(recipient_data):
            return recipient_data
        else:
            return None