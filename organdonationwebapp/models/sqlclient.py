from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import logging
logging.basicConfig(filename='file.log',level=logging.DEBUG)

class SqlClient(object):
    def __init__(self):
        self.host = "db-5308.cs.dal.ca"
        self.port = 3306
        self.user = "CSCI5308_16_DEVINT_USER"
        self.password = "CSCI5308_16_DEVINT_16175"
        self.connect_timeout = 30
        self.dbname = "CSCI5308_16_DEVINT"
        try:
            self.connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.dbname)
            self.cursor = self.connection.cursor()
            logging.info("Successfully connected to Database")
        except Exception as err:
            logging.error("Error connecting to Database")
            exit(1)

    def hospitalLoginAuthentication(self,hemail,hpass):
        result = self.cursor.callproc('hospitallogin',[hemail,hpass,0])
        #print(result)
        if(result[2]):
            return result
        else:
            return None
    
    def hospitalexist(self, hemail):
        res = self.cursor.callproc('hospitalexist',[hemail,0])
        if(res[1]):
            return "Exist"
        else:
            return "NotExist"
    def adminLoginAuthentication(self,email,password):
        user1 = self.cursor.callproc('adminlogin',[email,password,0])
        #print(user1)
        if not self.connection.is_connected():
            logging.info("Database connection closed successfully - adminLoginAuthentication")
        else:
            logging.info("Database connection is active - adminLoginAuthentication")
        if(user1[2]):
            return user1[2]
        else:
            return None

    def getHospitalList(self):

        self.cursor.callproc('hospitallist')
        res = self.cursor.stored_results()
        for result in res:
            hospitallist= result.fetchall()
            for row in hospitallist:
                hospitalEmail = row[0]
                validateFlag = row[1]
            if(hospitallist):
                # print(hospitallist)
                return hospitallist
            else:
                return None
        if not self.connection.is_connected():
             print("Database connection closed successfully - getHospitalList")
        else:
             print("Database connection is active - getHospitalList")

    def validateHospital(self, hospitalname):
        self.cursor.callproc('validatehospital',[hospitalname])
        self.connection.commit()

    def organRequest(self, requestID):
        # print(requestID)
        self.cursor.callproc('organrequest',[requestID])
        res = self.cursor.stored_results()
        for result in res:
            requestdata= result.fetchall()
            print(requestdata)
            if(requestdata):
                return requestdata
            else:
                return None

    
    def donorHospitalShowReceiverProfile(self, recipientEmail):
            
            self.cursor.callproc('donorhospitalshowreceiverprofile',[recipientEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata= result.fetchall()
                if(userdata):
                    return userdata
                else:
                    return None

    def donorHospitalShowDonorProfile(self, donorEmail):
        self.cursor.callproc('donorhospitalshowdonorprofile',[donorEmail])
        res = self.cursor.stored_results()
        for result in res:
            userdata= result.fetchall()
            if(userdata):
                return userdata
            else:
                return None


    def receiverHospitalShowProfile(self, recipientEmail):
        self.cursor.callproc('receiverhospitalshowprofile',[recipientEmail])
        res = self.cursor.stored_results()
        for result in res:
            userdata= result.fetchall()
            if(userdata):
                return userdata
            else:
                return None


    def receiverHospitalShowOrgan(self, recipientEmail):
        self.cursor.callproc('receiverhospitalshoworgan',[recipientEmail])
        res = self.cursor.stored_results()
        for result in res:
            userdata_organ= result.fetchall()
            for row in userdata_organ:
                organ = row[0]
            if(userdata_organ):
                return userdata_organ
            else:
                return None

    def recommendedDonorList(self, organ):
        self.cursor.callproc('recommendeddonorlist',[organ])
        res = self.cursor.stored_results()
        for result in res:
            organ_data= result.fetchall()
            if(organ_data):
                return organ_data
            else:
                return None
    
    def getHospitalDonorList(self,hname):
        self.cursor.callproc('gethospitaldonorlist',[hname])
        res = self.cursor.stored_results()
        for result in res:
            donorlist= result.fetchall()
            return donorlist

    def getHospitalReceiverList(self,hname):
        self.cursor.callproc('gethospitalreceiverlist',[hname])
        res = self.cursor.stored_results()
        for result in res:
            receiverlist= result.fetchall()
            return receiverlist


    def getHospitalName(self,hemail):
        self.cursor.callproc('gethospitalname',[hemail])
        res = self.cursor.stored_results()
        for result in res:
            hname= result.fetchall()
            # print(hname)
            if(hname):
                return hname[0]
            else:
                return None

    def getDonorList(self):
        self.cursor.callproc('getreceiverlist')
        res = self.cursor.stored_results()
        for result in res:
            donorlist= result.fetchall()
            if(donorlist):
                return donorlist
            else:
                return None

    def getReceiverList(self):
        self.cursor.callproc('getreceiverlist')
        res = self.cursor.stored_results()
        for result in res:
            receiverlist= result.fetchall()
            print(receiverlist)
            if(receiverlist):
                return receiverlist
            else:
                return None

    def hospitalRegistrattion(self,hospitalName,emailID,phone,address,province,city,password,certificate):
        self.cursor.callproc('hospitalregistration',[hospitalName,emailID,phone,address,province,city,password,certificate])
        self.connection.commit()
        return "Done"
    
    def userRegistration(self,first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, organ):
        self.cursor.callproc('userregistration',[first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, organ])
        self.connection.commit()
        return "Done"

    def closeDBConnection(self):
        self.cursor.close()
        self.connection.close()