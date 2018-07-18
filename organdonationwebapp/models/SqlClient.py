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


    def getHospitalName(self,hemail):
        query = """SELECT  * FROM hospital where emailID=%s """
        self.cursor.execute(query,(hemail,))
        hname = self.cursor.fetchone()
        if(hname):
            return hname
        else:
            return None    

    
    def closeDBConnection(self):
        self.cursor.close()
        self.connection.close()