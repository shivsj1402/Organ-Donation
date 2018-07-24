from organdonationwebapp import duc

class DonorListDetails(object):
    def __init__(self,Email):
        self.Email = Email


    def getDonorsList(self, hname):
        self.hname = hname
        donor_list = duc.getDonorList(self.hname)
        if(donor_list):
            return donor_list
        else:
            return None