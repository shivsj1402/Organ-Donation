from organdonationwebapp.models.SqlClient import SqlClient

class AdminModel(SqlClient):
    def __init__(self):
        super(AdminModel,self).__init__()
    

    def adminLoginAuthentication(self,emailID,password):
        try:
            print("Successfully connected to Database")
            user1 = self.cursor.callproc('adminlogin',[emailID  ,password,0])
            if(user1[2]):
                return user1[2]
            else:
                return None
        except Exception as err:
            print(err)
            return None


    # def validateHospital(self, hospitalEmail):
    #     try:
    #         self.cursor.callproc('validatehospital',[hospitalEmail])
    #         self.connection.commit()
    #         return True
    #     except Exception as err:
    #         print(err)
    #         return False


    # def deleteHospital(self, hospitalEmail):
    #     try:
    #         self.cursor.callproc('deletehospital',[hospitalEmail])
    #         self.connection.commit()
    #         return True
    #     except Exception as err:
    #         print(err)
    #         return False