from organdonationwebapp import ruc

class RecipientListDetails(object):
    def __init__(self,recipientEmail):
        self.recipientEmail = recipientEmail

    def getRecipientList(self):
        recipient_list = ruc.getReceiverList()
        if(recipient_list):
            return recipient_list
        else:
            return None