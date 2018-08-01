from organdonationwebapp.models.SqlClient import SqlClient

class RecipientModel(SqlClient):
    def __init__(self):
        super(RecipientModel,self).__init__()


    def donorHospitalShowReceiverProfile(self, recipientEmail):
        try:
            SqlClient.startDBConnection(self)
            print("donorHospitalShowReceiverProfile")
            self.cursor.callproc('donorhospitalshowreceiverprofile',[recipientEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata= result.fetchall()
                if(userdata):
                    SqlClient.closeDBConnection(self)
                    print("userdata",(userdata))
                    return userdata
                else:
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None


    def getRecepientList(self, hname):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('gethospitalreceiverlist',[hname])
            res = self.cursor.stored_results()
            for result in res:
                recipientlist= result.fetchall()
            SqlClient.closeDBConnection(self)
            return recipientlist
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None


    def receiverHospitalShowProfile(self, recipientEmail):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('receiverhospitalshowprofile',[recipientEmail])
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


    def receiverHospitalShowOrgan(self, recipientEmail):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('receiverhospitalshoworgan',[recipientEmail])
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


    def createRequest(self, donorEmail, recipientEmail, donatingOrgan, donorHospital):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('createrequest',[donorEmail,recipientEmail,donatingOrgan,donorHospital,0])
            self.connection.commit()
            SqlClient.closeDBConnection(self)
            return True
        except Exception as err:
            SqlClient.closeDBConnection(self)
            print(err)
            return False


    def getOpenRequestsStatus(self, recipientEmail):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('recipientOpenRequestStatus',[recipientEmail])
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