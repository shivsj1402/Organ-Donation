from organdonationwebapp import hc

class HospitalDonorList(object):
    def __init__(self,hospitalName):
        self.hospitalName = hospitalName

    def getDonorList(self):
        donor_list = hc.getHospitalDonorList(self.hospitalName)
        if(donor_list):
            return donor_list
        else:
            return None