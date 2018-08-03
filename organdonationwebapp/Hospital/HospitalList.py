from organdonationwebapp import hc

class HospitalList(object):
    def __init__(self,logger):
        self.logger = logger

    def getGlobalHospitalList(self):
        try:
            self.logger.info("getGlobalHospitalList logger initialized")
            hospital_list = hc.getHospitalList(self.logger)
            if(hospital_list):
                return hospital_list
            else:
                return None
        except Exception as err:
            self.logger.error(err)
            return err        