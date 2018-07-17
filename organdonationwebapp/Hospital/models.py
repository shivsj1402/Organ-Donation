from organdonationwebapp.models.SqlClient import SqlClient

class HospitalModel(SqlClient):
    def __init__(self):
        super(HospitalModel,self).__init__()
    
    def hospitalRegistration(self,hospitalName,emailID,phone,address,province,city,password,certificate):
        query = """INSERT INTO hospital(hospitalName,emailID,phone,address,province,city,password,certificate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        try:
            self.cursor.execute(query,(hospitalName,emailID,phone,address,province,city,password,certificate))
            self.connection.commit()
            return True
        except Exception as err:
            return False

    def hospitalLoginAuthentication(self,emailID,password):
        try:
            query = """SELECT  * FROM hospital where emailID=%s  AND password=%s"""
            self.cursor.execute(query,(emailID, password))
            result = self.cursor.fetchone()
            if(result):
                return result
            else:
                return None
        except Exception as err:
            return None


    def validateHospital(self, hospitalEmail):
        try:
            query = """UPDATE hospital SET validate = %s WHERE emailID=%s"""
            self.cursor.execute(query,(True, hospitalEmail))
            self.connection.commit()
            return True
        except Exception as err:
            return False


    def getHospitalList(self):
        try:
            query = """SELECT * FROM hospital"""
            self.cursor.execute(query)
            hospitallist = self.cursor.fetchall()
            for row in hospitallist:
                hospitalEmail = row[0]
                validateFlag = row[1]
            if(hospitallist):
                return hospitallist
            else:
                return None
        except Exception as err:
            return None