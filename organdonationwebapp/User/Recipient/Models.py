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


    def getRecepientList(self, hname):
        self.cursor.callproc('gethospitalreceiverlist',[hname])
        res = self.cursor.stored_results()
        for result in res:
            recipientlist= result.fetchall()
            return recipientlist


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