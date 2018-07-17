from organdonationwebapp.models.sqlclient import SqlClient

class RecipientModel(SqlClient):
    def __init__(self):
        super(RecipientModel,self).__init__()


    def donorHospitalShowReceiverProfile(self, recipientEmail):
        query = """SELECT userFirstName, userLastName, emailID, dob, sex, organ FROM user WHERE emailID=%s AND donationType=%s"""
        try:
            self.cursor.execute(query,(recipientEmail,"r"))
            userdata = self.cursor.fetchall()
            if(userdata):
                return userdata
            else:
                return None
        except Exception as err:
            return None


    def getReceiverList(self):
        query = """SELECT  * FROM user where donationType='r'"""
        try:
            self.cursor.execute(query)
            receiverlist= self.cursor.fetchall()
            if(receiverlist):
                return receiverlist
            else:
                return None
        except Exception as err:
            return None


    def receiverHospitalShowProfile(self, recipientEmail):
        try: 
            query = """SELECT userFirstName, userLastName, emailID, dob, sex FROM user WHERE emailID=%s AND donationType=%s"""
            self.cursor.execute(query,(recipientEmail,"r"))
            userdata = self.cursor.fetchall()
            if(userdata):
                return userdata
            else:
                return None
        except Exception as err:
            return None


    def receiverHospitalShowOrgan(self, recipientEmail):
        try:
            query = """SELECT organ FROM user WHERE emailID=%s AND donationType=%s"""
            self.cursor.execute(query,(recipientEmail,"r"))
            userdata_organ = self.cursor.fetchall()
            for row in userdata_organ:
                organ = row[0]
            if(userdata_organ):
                return userdata_organ
            else:
                return None
        except Exception as err:
            return None