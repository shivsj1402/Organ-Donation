from organdonationwebapp import duc


class Donor(object):
    def __init__(self,donorEmail):
        self.donorEmail = donorEmail

    def donorHospitalRequestPage(self):
        try:
            donor_data = duc.donorHospitalShowDonorProfile(self.donorEmail)
            if(donor_data):
                return donor_data
            else:
                return None
        except Exception as err:
            return err