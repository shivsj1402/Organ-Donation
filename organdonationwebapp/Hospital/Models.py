from organdonationwebapp.models.SqlClient import SqlClient

class HospitalModel(SqlClient):
    def __init__(self):
        super(HospitalModel,self).__init__()
    
    
    def hospitalRegistration(self,hospitalName,emailID,phone,address,province,city,password,certificate):
        try:
            self.cursor.callproc('hospitalregistration',[hospitalName,emailID,phone,address,province,city,password,certificate])
            self.connection.commit()
            return True
        except Exception as err:
            print(err)
            return False


    def hospitalLoginAuthentication(self,hemail,hpass):
        try:
            self.cursor.callproc('hospitallogin',[hemail,hpass])
            res = self.cursor.stored_results()
            for result in res:
                hospitalauth= result.fetchall()
                if(hospitalauth):
                    return hospitalauth
                else:
                    return None
        except Exception as err:
            print(err)
            return None        


    def getHospitalName(self,hemail):
        try:
            self.cursor.callproc('gethospitalname',[hemail])
            res = self.cursor.stored_results()
            for result in res:
                hname= result.fetchall()
                if(hname):
                    return hname[0]
                else:
                    return None
        except Exception as err:
            return None


    def validateHospital(self, hospitalEmail):
        try:
            self.cursor.callproc('validatehospital',[hospitalEmail])
            self.connection.commit()
            return True
        except Exception as err:
            print(err)
            return False


    def getHospitalList(self):
        try:
            self.cursor.callproc('hospitallist')
            res = self.cursor.stored_results()
            for result in res:
                hospitallist= result.fetchall()
                for row in hospitallist:
                    hospitalEmail = row[0]
                    validateFlag = row[1]
                if(hospitallist):
                    return hospitallist
                else:
                    return None
        except Exception as err:
            return None

#################################
    def getHospitalID(self,donorHospitalName):
        try:
            query = """SELECT emailID FROM hospital WHERE hospitalName=%s"""
            self.cursor.execute(query,(donorHospitalName,))
            hospital_email = self.cursor.fetchone()
            if(hospital_email):
                return hospital_email
            else:
                return None
        except Exception as err:
            return None


    def getHospitalDonorList(self,hname):
        self.cursor.callproc('gethospitaldonorlist',[hname])
        res = self.cursor.stored_results()
        for result in res:
            donorlist= result.fetchall()
            return donorlist


    def getHospitalRecipientList(self,hname):
        self.cursor.callproc('gethospitalreceiverlist',[hname])
        res = self.cursor.stored_results()
        for result in res:
            receiverlist= result.fetchall()
            return receiverlist


    def getHospitalRequestList(self,emailID):
        self.cursor.callproc('requestlist', [emailID])
        res = self.cursor.stored_results()
        for result in res:
            requestlist= result.fetchall()
            return requestlist


    def hospitalexist(self, hemail):
        res = self.cursor.callproc('hospitalexist',[hemail,0])
        if(res[1]):
            return "Exist"
        else:
            return "NotExist"


    def getPassword(self):
        try:
            self.cursor.callproc('validatePassword')
            res = self.cursor.stored_results()
            for result in res:
                passwordRules= result.fetchall()
                print(passwordRules)
                return passwordRules
        except Exception as err:
            return None
