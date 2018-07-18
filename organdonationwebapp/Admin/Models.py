from organdonationwebapp.models.SqlClient import SqlClient

class AdminModel(SqlClient):
    def __init__(self):
        super(AdminModel,self).__init__()
    

    def adminLoginAuthentication(self,emailID,password):
        try:
            user1 = self.cursor.callproc('adminlogin',[emailID  ,password,0])
            if(user1[2]):
                return user1[2]
            else:
                return None
        except Exception as err:
            print(err)
            return None