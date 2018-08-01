from organdonationwebapp.models.SqlClient import SqlClient

class AdminModel(SqlClient):
    def __init__(self):
        super(AdminModel,self).__init__()
    

    def adminLoginAuthentication(self,emailID,password):
        try:
            SqlClient.startDBConnection(self)
            user1 = self.cursor.callproc('adminlogin',[emailID  ,password,0])
            if(user1[2]):
                SqlClient.closeDBConnection(self)
                return user1[2]
            else:
                SqlClient.closeDBConnection(self)
                return None
        except Exception as err:
            print(err)
            SqlClient.closeDBConnection(self)
            return None


    def validateHospital(self, hospitalEmail, logger):
        self.logger = logger
        try:
            SqlClient.startDBConnection(self)
            self.logger.info("validateHospital logger initilized")
            self.cursor.callproc('validatehospital',[hospitalEmail])
            self.connection.commit()
            SqlClient.closeDBConnection(self)
            return True
        except Exception as err:
            self.logger.error(err)
            SqlClient.closeDBConnection(self)
            return False


    def deleteHospital(self, hospitalEmail, logger):
        self.logger = logger
        try:
            SqlClient.startDBConnection(self)
            self.logger.info("deleteHospital logger initilized")
            self.cursor.callproc('deletehospital',[hospitalEmail])
            self.connection.commit()
            SqlClient.closeDBConnection(self)
            return True
        except Exception as err:
            SqlClient.closeDBConnection(self)
            self.logger.error(err)
            return False

    def getHospitalCertificate(self, hospitalEmail):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('gethospitalcertificate',[hospitalEmail])
            res = self.cursor.stored_results()
            for result in res:
                hospitalcertificate= result.fetchall()
                if(hospitalcertificate):
                    SqlClient.closeDBConnection(self)
                    return hospitalcertificate
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            print(err)
            SqlClient.closeDBConnection(self)
            return False