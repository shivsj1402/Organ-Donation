from organdonationwebapp import duc

class ShowRecommendedDonors(object):
    def __init__(self,donororgan,logger):
        self.donororgan = donororgan
        self.logger = logger

    def getrecommendedDonorList(self):
        matching_donors = duc.recommendedDonorList(self.donororgan, self.logger)
        if(matching_donors):
            return matching_donors
        else:
            return None