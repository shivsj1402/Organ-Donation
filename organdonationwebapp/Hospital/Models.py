from organdonationwebapp.models.SqlClient import SqlClient


class HospitalModel(SqlClient):
    def __init__(self):
        super(HospitalModel,self).__init__()
    
    def hospitalRegistration(self,hospital):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('hospitalregistration',[hospital.hospitalName,hospital.emailID,hospital.phone,hospital.address,hospital.province,hospital.city,hospital.password,hospital.data])
            self.connection.commit()
            SqlClient.closeDBConnection(self)
            return True
        except Exception as err:
            SqlClient.closeDBConnection(self)
            print(err)
            return False


    def hospitalLoginAuthentication(self,hemail,hpass):
        try:
            SqlClient.startDBConnection(self)
            print("hospitalLoginAuthentication")
            self.cursor.callproc('hospitallogin',[hemail,hpass])
            res = self.cursor.stored_results()
            for result in res:
                hospitalauth= result.fetchall()
                if(hospitalauth):
                    SqlClient.closeDBConnection(self)
                    print("hospitalLoginAuthentication Close")
                    return hospitalauth
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            print(err)
            SqlClient.closeDBConnection(self)
            return None        


    def getHospitalName(self,hemail):
        try:
            SqlClient.startDBConnection(self)
            print("getHospitalName")
            self.cursor.callproc('gethospitalname',[hemail])
            res = self.cursor.stored_results()
            for result in res:
                hname= result.fetchall()
                if(hname):
                    SqlClient.closeDBConnection(self)
                    return hname[0]
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None


    def getHospitalList(self):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('hospitallist')
            res = self.cursor.stored_results()
            for result in res:
                hospitallist= result.fetchall()
                for row in hospitallist:
                    hospitalEmail = row[0]
                    validateFlag = row[1]
                if(hospitallist):
                    SqlClient.closeDBConnection(self)
                    return hospitallist
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None


    def getHospitalID(self,donorHospitalName):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('getHospitalID',[donorHospitalName])
            res = self.cursor.stored_results()
            for result in res:
                hospital_email= result.fetchone()
                if(hospital_email):
                    SqlClient.closeDBConnection(self)
                    return hospital_email
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None


    def getHospitalDonorList(self,hname):
        SqlClient.startDBConnection(self)
        print("getHospitalDonorList")
        self.cursor.callproc('gethospitaldonorlist',[hname])
        res = self.cursor.stored_results()
        for result in res:
            donorlist= result.fetchall()
        SqlClient.closeDBConnection(self)
        return donorlist


    def getHospitalRecipientList(self,hname):
        SqlClient.startDBConnection(self)
        print("getHospitalRecipientList")
        self.cursor.callproc('gethospitalreceiverlist',[hname])
        res = self.cursor.stored_results()
        for result in res:
            receiverlist= result.fetchall()
        SqlClient.closeDBConnection(self)
        return receiverlist


    def getHospitalRequestList(self,emailID):
        SqlClient.startDBConnection(self)
        print("getHospitalRequestList")
        self.cursor.callproc('requestlist', [emailID])
        res = self.cursor.stored_results()
        for result in res:
            requestlist= result.fetchall()
        SqlClient.closeDBConnection(self)
        return requestlist


    def hospitalexist(self, hemail):
        SqlClient.startDBConnection(self)
        res = self.cursor.callproc('hospitalexist',[hemail,0])
        if(res[1]):
            SqlClient.closeDBConnection(self)
            return "Exist"
        else:
            SqlClient.closeDBConnection(self)
            return "NotExist"


    def getPassword(self):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('validatePassword')
            res = self.cursor.stored_results()
            for result in res:
                passwordRules= result.fetchall()
                print(passwordRules)
            SqlClient.closeDBConnection(self)
            return passwordRules
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None