from organdonationwebapp.models.SqlClient import SqlClient

class HospitalModel(SqlClient):
    def __init__(self):
        super(HospitalModel,self).__init__()
    
    def hospitalRegistration(self,hospital):
        try:
            self.cursor.callproc('hospitalregistration',[hospital.hospitalName,hospital.emailID,hospital.phone,hospital.address,hospital.province,hospital.city,hospital.password,hospital.data])
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


    def getHospitalName(self,hemail,logger):
        self.logger = logger
        try:
            self.logger.info(" getHospitalName logger intitlized")
            self.cursor.callproc('gethospitalname',[hemail])
            res = self.cursor.stored_results()
            for result in res:
                hname= result.fetchall()
                if(hname):
                    return hname[0]
                else:
                    return None
        except Exception as err:
            self.logger.error(err)
            return None


    def getHospitalList(self,logger):
        self.logger = logger
        try:
            self.logger.info("getHospitalList logger initilized")
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
            self.logger.error(err)
            return None


    def getHospitalID(self,donorHospitalName):
        try:
            self.cursor.callproc('getHospitalID',[donorHospitalName])
            res = self.cursor.stored_results()
            for result in res:
                hospital_email= result.fetchone()
                if(hospital_email):
                    return hospital_email
                else:
                    return None
        except Exception as err:
            return None


    def getHospitalDonorList(self,hname, logger):
        self.logger = logger
        try:
            self.logger.info("getHospitalDonorList logger initilized")
            self.cursor.callproc('gethospitaldonorlist',[hname])
            res = self.cursor.stored_results()
            for result in res:
                donorlist= result.fetchall()
                if(donorlist):
                    return donorlist
                else:
                    return None
        except Exception as err:
            self.logger.error(err)
            return None


    def getHospitalRecipientList(self,hname,logger):
        self.logger = logger
        try:
            self.logger.info("getHospitalRecipientList logger initilized")
            self.cursor.callproc('gethospitalreceiverlist',[hname])
            res = self.cursor.stored_results()
            for result in res:
                receiverlist= result.fetchall()
                if(receiverlist):
                    return receiverlist
                else:
                    return None
        except Exception as err:
            self.logger.error(err)
            return None


    def getHospitalRequestList(self,emailID, logger):
        self.logger = logger
        try:
            self.logger.info("getHospitalRequestList called for emailID" + self.emailID)
            self.cursor.callproc('requestlist', [emailID])
            res = self.cursor.stored_results()
            for result in res:
                requestlist= result.fetchall()
                if(requestlist):
                    self.logger.info("Values Fetched Successfully")
                    return requestlist
                else:
                    return None
        except Exception as err:
            self.logger.error(err)
            return None   


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
                # print(passwordRules)
                return passwordRules
        except Exception as err:
            return None