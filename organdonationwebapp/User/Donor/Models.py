from organdonationwebapp.models.SqlClient import SqlClient

class DonorModel(SqlClient):
    def __init__(self):
        super(DonorModel,self).__init__()


    def donorHospitalShowDonorProfile(self, donorEmail):
        try:
            self.cursor.callproc('donorhospitalshowdonorprofile',[donorEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata= result.fetchall()
                if(userdata):
                    return userdata
                else:
                    return None
        except Exception as err:
            return None


    def recommendedDonorList(self, organ):
        try:
            self.cursor.callproc('recommendeddonorlist',[organ])
            res = self.cursor.stored_results()
            for result in res:
                organ_data= result.fetchall()
                if(organ_data):
                    return organ_data
                else:
                    return None
        except Exception as err:
            return None


    def getDonorList(self, hname):
        self.cursor.callproc('gethospitaldonorlist',[hname])
        res = self.cursor.stored_results()
        for result in res:
            donorlist= result.fetchall()
            return donorlist
