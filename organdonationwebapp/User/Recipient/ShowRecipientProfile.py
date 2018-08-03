from organdonationwebapp import ruc

class ShowRecipientProfile(object):
    def __init__(self,recipientEmail, logger):
        self.recipientEmail = recipientEmail
        self.logger = logger

    def getRecipientProfile(self):
        try:
            recipient_data = ruc.receiverHospitalShowProfile(self.recipientEmail)
            if(recipient_data):
                return recipient_data
            else:
                return None
        except Exception as err:
            return err

    def getRecipientOrgans(self):
        try:
            recipient_organ_data = ruc.receiverHospitalShowOrgan(self.recipientEmail, self.logger)
            if(recipient_organ_data):
                return recipient_organ_data
            else:
                return None
        except Exception as err:
            return err