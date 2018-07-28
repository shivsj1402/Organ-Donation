from organdonationwebapp.models.SqlClient import SqlClient
import datetime

class UserModel(SqlClient):
    def __init__(self):
        super(UserModel,self).__init__()


    def userRegistration(self, user):
        requestdate =datetime.datetime.today().strftime('%Y-%m-%d')
        try:
            for item in user.organ:
                self.cursor.callproc('userregistration',[user.first_name, user.last_name, user.phone_number, user.email, user.sex, user.dob, user.address, user.province, user.city, user.hospital, user.bloodgroup, user.usertype,requestdate,item])
                self.connection.commit()
            return True
        except Exception as err:
            print(err)
            return False


    def organRequest(self, requestID):
        try:
            self.cursor.callproc('organrequest',[requestID])
            res = self.cursor.stored_results()
            for result in res:
                requestdata= result.fetchall()
                if(requestdata):
                    return requestdata
                else:
                    return None
        except Exception as err:
            print(err)
            return None

    def updateReport(self,emailID, report,userType):
        try:
            self.cursor.callproc('updatereports',[emailID, userType, report])
            self.connection.commit()
            return True
        except Exception as err:
            print(err)
            return False