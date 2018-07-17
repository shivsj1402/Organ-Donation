from organdonationwebapp import duc

class ShowRecommendedDonors(object):
    def __init__(self,donororgan):
        self.donororgan = donororgan

    def getrecommendedDonorList(self):
        matching_donors = duc.recommendedDonorList(self.donororgan)
        if(matching_donors):
            return matching_donors
        else:
            return None