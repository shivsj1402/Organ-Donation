from organdonationwebapp import duc, sc

class DonorListDetails(object):
    def __init__(self,Email):
        self.Email = Email

    def getDonorList(self, hname):
        self.hname = hname
        donor_list = duc.getDonorList(self.hname)
        if(donor_list):
            return donor_list
        else:
            return None