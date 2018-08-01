from organdonationwebapp.models.SqlClient import SqlClient

class RecipientModel(SqlClient):
    def __init__(self):
        super(RecipientModel,self).__init__()


    def donorHospitalShowReceiverProfile(self, recipientEmail, logger):
        self.logger = logger
        try:
            self.logger.info("donorHospitalShowReceiverProfile logger initilized")
            self.cursor.callproc('donorhospitalshowreceiverprofile',[recipientEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata= result.fetchall()
                if(userdata):
                    # print("userdata",(userdata))
                    return userdata
                else:
                    return None
        except Exception as err:
            self.logger.error(err)
            return None


    def getRecepientList(self, hname):
        try:
            self.cursor.callproc('gethospitalreceiverlist',[hname])
            res = self.cursor.stored_results()
            for result in res:
                recipientlist= result.fetchall()
                return recipientlist
        except Exception as err:
            return None


    def receiverHospitalShowProfile(self, recipientEmail):
        try: 
            self.cursor.callproc('receiverhospitalshowprofile',[recipientEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata= result.fetchall()
                if(userdata):
                    return userdata
                else:
                    return None
        except Exception as err:
            return None


    def receiverHospitalShowOrgan(self, recipientEmail, logger):
        self.logger = logger
        try:
            self.logger.info("receiverHospitalShowOrgan logger initilized")
            self.cursor.callproc('receiverhospitalshoworgan',[recipientEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata_organ= result.fetchall()
                for row in userdata_organ:
                    organ = row[0]
                if(userdata_organ):
                    return userdata_organ
                else:
                    return None
        except Exception as err:
            self.logger.error(err)
            return None


    def createRequest(self, donorEmail, recipientEmail, donatingOrgan, donorHospital):
        try:
            self.cursor.callproc('createrequest',[donorEmail,recipientEmail,donatingOrgan,donorHospital,0])
            self.connection.commit()
            return True
        except Exception as err:
            print(err)
            return False


    def getOpenRequestsStatus(self, recipientEmail):
        try:
            self.cursor.callproc('recipientOpenRequestStatus',[recipientEmail])
            res = self.cursor.stored_results()
            for result in res:
                requeststatusdata= result.fetchall()
                if(requeststatusdata):
                    return requeststatusdata
                else:
                    return None
        except Exception as err:
            return None