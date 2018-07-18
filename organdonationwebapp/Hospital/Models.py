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

    def hospitalLoginAuthentication(self,hemail):
        try:
            self.cursor.callproc('hospitallogin',[hemail])
            res = self.cursor.stored_results()
            for result in res:
                hospitalauth= result.fetchall()
                hospitalpassword=hospitalauth[0][6]
                #print(result)
                if(hospitalauth):
                    return hospitalauth
                else:
                    return None
        except Exception as err:
            return None        

    def getHospitalName(self,hemail):
        try:
            query = """SELECT  * FROM hospital where emailID=%s """
            self.cursor.execute(query,(hemail,))
            hname = self.cursor.fetchone()
            if(hname):
                return hname
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


    def getHospitalDonorList(self,hname):
        query = """SELECT  * FROM user where donationType='d' AND hospital=%s"""
        self.cursor.execute(query,(hname,))
        donorlist= self.cursor.fetchall()
        return donorlist


    def getHospitalRecipientList(self,hname):
        query = """SELECT  * FROM user where donationType='r' AND hospital=%s"""
        self.cursor.execute(query,(hname,))
        receiverlist= self.cursor.fetchall()
        return receiverlist