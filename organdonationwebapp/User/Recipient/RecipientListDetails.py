from organdonationwebapp import ruc,sc

class RecipientListDetails(object):
    def __init__(self,recipientEmail):
        self.recipientEmail = recipientEmail

    def getRecipientsList(self, hname):
        self.hname = hname
        recipient_list = ruc.getRecepientList(self.hname)
        if(recipient_list):
            return recipient_list
        else:
            return None