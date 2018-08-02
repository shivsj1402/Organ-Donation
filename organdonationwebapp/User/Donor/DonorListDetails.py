from organdonationwebapp import duc

class DonorListDetails(object):
    def __init__(self,Email):
        self.Email = Email


    def getDonorsList(self, hname):
        try:
            self.hname = hname
            donor_list = duc.getDonorList(self.hname)
            if(donor_list):
                return donor_list
            else:
                return None
        except Exception as err:
            return err