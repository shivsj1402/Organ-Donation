from organdonationwebapp import duc


class ShowDonorProfile(object):
    def __init__(self,donorEmail):
        self.donorEmail = donorEmail


    def getDonorProfile(self):
        try:
            donor_data = duc.donorHospitalShowDonorProfile(self.donorEmail)
            if(donor_data):
                return donor_data
            else:
                return None
        except Exception as err:
            return err


    def getDonorOrgans(self):
        try:
            donor_organ_data = duc.showDonorOrgan(self.donorEmail)
            if(donor_organ_data):
                return donor_organ_data
            else:
                return None
        except Exception as err:
            return err