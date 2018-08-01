from organdonationwebapp.models.SqlClient import SqlClient

class DonorModel(SqlClient):
    def __init__(self):
        super(DonorModel,self).__init__()


    def donorHospitalShowDonorProfile(self, donorEmail):
        try:
            SqlClient.startDBConnection(self)
            print("donorHospitalShowDonorProfile")
            self.cursor.callproc('donorhospitalshowdonorprofile',[donorEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata= result.fetchall()
                if(userdata):
                    SqlClient.closeDBConnection(self)
                    return userdata
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None


    def showDonorOrgan(self, donorEmail):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('donorshoworgan',[donorEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata_organ= result.fetchall()
                for row in userdata_organ:
                    organ = row[0]
                if(userdata_organ):
                    SqlClient.closeDBConnection(self)
                    return userdata_organ
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None


    def recommendedDonorList(self, organ, logger):
        self.logger = logger
        try:
            SqlClient.startDBConnection(self)
            self.logger.info("recommendedDonorList logger initilized")
            self.cursor.callproc('recommendeddonorlist',[organ])
            res = self.cursor.stored_results()
            for result in res:
                organ_data= result.fetchall()
                if(organ_data):
                    SqlClient.closeDBConnection(self)
                    return organ_data
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            self.logger.error(err)
            return None


    def getDonorList(self, hname):
        SqlClient.startDBConnection(self)
        self.cursor.callproc('gethospitaldonorlist',[hname])
        res = self.cursor.stored_results()
        for result in res:
            donorlist= result.fetchall()
            SqlClient.closeDBConnection(self)
            return donorlist


    def setRequestsStatus(self, requestID, requeststate):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('updaterequeststate',[requestID,requeststate])
            self.connection.commit()
            SqlClient.closeDBConnection(self)
            return True
        except Exception as err:
            print(err)
            SqlClient.closeDBConnection(self)
            return False


    def getOpenRequestsStatus(self, hospitalEmail, donorEmail):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('donorOpenRequestStatus',[hospitalEmail,donorEmail])
            res = self.cursor.stored_results()
            for result in res:
                requeststatusdata= result.fetchall()
                if(requeststatusdata):
                    SqlClient.closeDBConnection(self)
                    return requeststatusdata
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None