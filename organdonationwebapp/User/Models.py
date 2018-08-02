from organdonationwebapp.models.SqlClient import SqlClient
import datetime

class UserModel(SqlClient):
    def __init__(self):
        super(UserModel,self).__init__()


    def userRegistration(self, user):
        requestdate =datetime.datetime.today().strftime('%Y-%m-%d')
        try:
            SqlClient.startDBConnection(self)
            print("userRegistration")
            for item in user.organ:
                self.cursor.callproc('userregistration',[user.first_name, user.last_name, user.phone_number, user.email, user.sex, user.dob, user.address, user.province, user.city, user.hospital, user.bloodgroup, user.usertype,requestdate,item])
                self.connection.commit()
            SqlClient.closeDBConnection(self)
            return True
        except Exception as err:
            print(err)
            SqlClient.closeDBConnection(self)
            return False


    def organRequest(self, requestID):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('organrequest',[requestID])
            res = self.cursor.stored_results()
            for result in res:
                requestdata= result.fetchall()
                if(requestdata):
                    SqlClient.closeDBConnection(self)
                    return requestdata
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            print(err)
            SqlClient.closeDBConnection(self)
            return None


    def getReports(self,emailID,userType):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('getuserreports',[emailID, userType])
            res = self.cursor.stored_results()
            for result in res:
                userreports= result.fetchall()
                if(userreports):
                    SqlClient.closeDBConnection(self)
                    return userreports
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            print(err)
            return False


    def updateReport(self,emailID,userType,report):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('updatereports',[emailID,userType,report])
            self.connection.commit()
            SqlClient.closeDBConnection(self)
            return True
        except Exception as err:
            print(err)
            SqlClient.closeDBConnection(self)
            return False