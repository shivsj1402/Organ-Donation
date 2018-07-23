from organdonationwebapp.models.SqlClient import SqlClient

class RecipientModel(SqlClient):
    def __init__(self):
        super(RecipientModel,self).__init__()


    def donorHospitalShowReceiverProfile(self, recipientEmail):
        try:
            self.cursor.callproc('donorhospitalshowreceiverprofile',[recipientEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata= result.fetchall()
                if(userdata):
                    return userdata
                else:
                    return None
        except Exception as err:
            return None


    def getReceiverList(self, hname):
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


    def receiverHospitalShowOrgan(self, recipientEmail):
        try:
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
            return None

##################################
    def createRequest(self, donorEmail, recipientEmail, donatingOrgan, donorHospital):
        try:
            query = """INSERT INTO requestdata(donorID,recipientID,organRequested,hospitalID, requestState) VALUES (%s,%s,%s,%s,%s)"""
            self.cursor.execute(query,(donorEmail,recipientEmail,donatingOrgan,donorHospital,0))
            self.connection.commit()
            return True
        except Exception as err:
            print(err)
            return False

##################################
    def getOpenRequestsStatus(self, recipientEmail):
        try:
            query = """SELECT * FROM requestdata WHERE recipientID=%s"""
            self.cursor.execute(query,(recipientEmail,))
            requeststatusdata = self.cursor.fetchall()
            if(requeststatusdata):
                return requeststatusdata
            else:
                return None
        except Exception as err:
            return None