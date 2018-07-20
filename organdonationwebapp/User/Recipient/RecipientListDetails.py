from organdonationwebapp import ruc


class RecipientListDetails(object):
    def __init__(self,recipientEmail):
        self.recipientEmail = recipientEmail


    def getReceiverList(self, hname):
        self.hname = hname
        recipient_list = ruc.getRecepientList(self.hname)
        if(recipient_list):
            return recipient_list
        else:
            return None