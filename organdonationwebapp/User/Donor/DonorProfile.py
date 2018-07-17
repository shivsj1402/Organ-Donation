from organdonationwebapp import duc


class DonorProfile(object):
    def __init__(self,donorEmail):
        self.donorEmail = donorEmail


    def getDonorProfile(self):
        donor_data = duc.donorHospitalShowDonorProfile(self.donorEmail)
        if(donor_data):
            return donor_data
        else:
            return None