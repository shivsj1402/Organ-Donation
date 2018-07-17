from organdonationwebapp import duc

class DonorListDetails(object):
    def __init__(self,donorEmail):
        self.donorEmail = donorEmail

    def getDonorList(self):
        donor_list = duc.getDonorList()
        if(donor_list):
            return donor_list
        else:
            return None