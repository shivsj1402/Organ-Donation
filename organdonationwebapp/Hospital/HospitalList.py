from organdonationwebapp import hc

class HospitalList(object):

    def getGlobalHospitalList(self):
        hospital_list = hc.getHospitalList()
        if(hospital_list):
            return hospital_list
        else:
            return None