from organdonationwebapp.models.sqlclient import SqlClient

class AdminModel(SqlClient):
    def __init__(self):
        super(AdminModel,self).__init__()
    

    def adminLoginAuthentication(self,emailID,password):
        query = """SELECT  * FROM admin where emailID=%s  AND password=%s"""
        try:
            self.cursor.execute(query,(emailID, password))
            result = self.cursor.fetchone()
            if(result):
                return result
            else:
                return None
        except Exception as err:
            return None