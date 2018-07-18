from organdonationwebapp.models.SqlClient import SqlClient

class HospitalModel(SqlClient):
    def __init__(self):
        super(HospitalModel,self).__init__()
    
    def hospitalRegistration(self,hospitalName,emailID,phone,address,province,city,password,certificate):
        try:
            # print("Cert",(certificate))
            self.cursor.callproc('hospitalregistration',[hospitalName,emailID,phone,address,province,city,password,certificate])
            self.connection.commit()
            return True
        except Exception as err:
            print(err)
            return False

    def hospitalLoginAuthentication(self,hemail):
        try:
            self.cursor.callproc('hospitallogin',[hemail])
            res = self.cursor.stored_results()
            for result in res:
                hospitalauth= result.fetchall()
                if(hospitalauth):
                    return hospitalauth
                else:
                    return None
        except Exception as err:
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