from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

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
            print("Successfully connected to Database")
        except Exception as err:
            print("Error connecting to Database")
            exit(1)

    def adminLoginAuthentication(self,email,password):
        query = """SELECT emailID FROM admin WHERE emailID= %s AND password= %s"""
        self.cursor.execute(query,(email, password))
        user1 = self.cursor.fetchone()
        if not self.connection.is_connected():
            print("Database connection closed successfully - adminLoginAuthentication")
        else:
            print("Database connection is active - adminLoginAuthentication")
        if(user1):
            return user1[0]
        else:
            return None

    def getHospitalList(self):

        query = """SELECT * FROM hospital"""
        self.cursor.execute(query)
        hospitallist = self.cursor.fetchall()
        for row in hospitallist:
            hospitalEmail = row[0]
            validateFlag = row[1]
        if not self.connection.is_connected():
            print("Database connection closed successfully - getHospitalList")
        else:
            print("Database connection is active - getHospitalList")
        if(hospitallist):
            return hospitallist
        else:
            return None

    def validateHospital(self, hospitalEmail):
        query = """UPDATE hospital SET validate = %s WHERE emailID=%s"""
        self.cursor.execute(query,(True, hospitalEmail))
        self.connection.commit()

    def organRequest(self, requestID):
        print(requestID)
        query = """SELECT donorID, recipientID, organRequested FROM requestdata WHERE requestID=%s"""
        self.cursor.execute(query,(requestID,))
        requestdata = self.cursor.fetchone()
        print("Hello",(requestdata))
        if(requestdata):
            return requestdata
        else:
            return None

    def donorHospitalShowReceiverProfile(self, recipientEmail):
        query = """SELECT userFirstName, userLastName, emailID, dob, sex, organ FROM user WHERE emailID=%s AND donationType=%s"""
        self.cursor.execute(query,(recipientEmail,"r"))
        userdata = self.cursor.fetchall()
        if(userdata):
            return userdata
        else:
            return None

    def donorHospitalShowDonorProfile(self, donorEmail):
        query = """SELECT * FROM user WHERE emailID=%s AND donationType=%s"""
        self.cursor.execute(query,(donorEmail,"d"))
        userdata = self.cursor.fetchall()
        if(userdata):
            return userdata
        else:
            return None

    def receiverHospitalShowProfile(self, recipientEmail):
        query = """SELECT userFirstName, userLastName, emailID, dob, sex FROM user WHERE emailID=%s AND donationType=%s"""
        self.cursor.execute(query,(recipientEmail,"r"))
        userdata = self.cursor.fetchall()
        if(userdata):
            return userdata
        else:
            return None

    def receiverHospitalShowOrgan(self, recipientEmail):
        query = """SELECT organ FROM user WHERE emailID=%s AND donationType=%s"""
        self.cursor.execute(query,(recipientEmail,"r"))
        userdata_organ = self.cursor.fetchall()
        for row in userdata_organ:
            organ = row[0]
        if(userdata_organ):
            return userdata_organ
        else:
            return None

    def recommendedDonorList(self, organ):
        query = """SELECT emailID, organ FROM user WHERE organ=%s AND donationType=%s"""
        self.cursor.execute(query,(organ,"d"))
        organ_data = self.cursor.fetchall()
        if(organ_data):
            return organ_data
        else:
            return None
    
    def getHospitalDonorList(self,hname):
        query = """SELECT  * FROM user where donationType='d' AND hospital=%s"""
        self.cursor.execute(query,(hname,))
        donorlist= self.cursor.fetchall()
        return donorlist

    def getHospitalReceiverList(self,hname):
        query = """SELECT  * FROM user where donationType='r' AND hospital=%s"""
        self.cursor.execute(query,(hname,))
        receiverlist= self.cursor.fetchall()
        return receiverlist

    def hospitalLoginAuthentication(self,hemail,hpassword):
        query = """SELECT  * FROM hospital where emailID=%s  AND password=%s"""
        self.cursor.execute(query,(hemail, hpassword))
        result = self.cursor.fetchone()
        if(result):
            return result
        else:
            return None

    def getHospitalName(self,hemail):
        query = """SELECT  * FROM hospital where emailID=%s """
        self.cursor.execute(query,(hemail,))
        hname = self.cursor.fetchone()
        if(hname):
            return hname
        else:
            return None

    def getDonorList(self):
        query = """SELECT  * FROM user where donationType='d'"""
        self.cursor.execute(query)
        donorlist= self.cursor.fetchall()
        if(donorlist):
            return donorlist
        else:
            return None

    def getReceiverList(self):
        query = """SELECT  * FROM user where donationType='r'"""
        self.cursor.execute(query)
        receiverlist= self.cursor.fetchall()
        if(receiverlist):
            return receiverlist
        else:
            return None

    def hospitalRegistrattion(self,hospitalName,emailID,phone,address,province,city,password,certificate):
        query = """INSERT INTO hospital(hospitalName,emailID,phone,address,province,city,password,certificate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        self.cursor.execute(query,(hospitalName,emailID,phone,address,province,city,password,certificate))
        self.connection.commit()
        return "Done"
    
    def userRegistration(self,first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, organ):
        query = """INSERT INTO user(userFirstName,userLastName,phone,emailID,sex,dob,address,province,city,hospital,bloodGroup,donationType,organ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        self.cursor.execute(query,(first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, organ))
        self.connection.commit()
        return "Done"

    def closeDBConnection(self):
        self.cursor.close()
        self.connection.close()