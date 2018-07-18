from organdonationwebapp.models.SqlClient import SqlClient

class DonorModel(SqlClient):
    def __init__(self):
        super(DonorModel,self).__init__()


    def donorHospitalShowDonorProfile(self, donorEmail):
        query = """SELECT * FROM user WHERE emailID=%s AND donationType=%s"""
        try:
            self.cursor.execute(query,(donorEmail,"d"))
            userdata = self.cursor.fetchall()
            if(userdata):
                return userdata
            else:
                return None
        except Exception as err:
            return None


    def recommendedDonorList(self, organ):
        try:
            query = """SELECT emailID, organ FROM user WHERE organ=%s AND donationType=%s"""
            self.cursor.execute(query,(organ,"d"))
            organ_data = self.cursor.fetchall()
            if(organ_data):
                return organ_data
            else:
                return None
        except Exception as err:
            return None


    def getDonorList(self):
        query = """SELECT  * FROM user where donationType='d'"""
        self.cursor.execute(query)
        donorlist= self.cursor.fetchall()
        if(donorlist):
            return donorlist
        else:
            return None