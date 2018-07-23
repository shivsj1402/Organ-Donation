from organdonationwebapp import ruc


class NewDonationRequest(object):
    def __init__(self, donorEmail, recipientEmail, donatingOrgan, donorHospital):
        self.donorEmail = donorEmail
        self.recipientEmail = recipientEmail
        self.donatingOrgan = donatingOrgan
        self.donorHospital = donorHospital


    def createDonationRequest(self):
        try:
            #hospitalRegistration
            if(ruc.createRequest(self.donorEmail, self.recipientEmail, self.donatingOrgan, self.donorHospital)):
                return True
            else:
                return False
        except Exception as err:
            return False