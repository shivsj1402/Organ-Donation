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
            return 
        except Exception as err:
            print("Error in connecting to Database")
            exit(1)

    def adminLoginAuthentication(self,email,password):
        query = """SELECT emailID FROM admin WHERE emailID= %s AND password= %s"""
        self.cursor.execute(query,(email, password))
        user1 = self.cursor.fetchone()
        if(user1):
            return user1[0]
        else:
            return None

    def getHospitalList(self):
        query = """SELECT emailID FROM hospital"""
        self.cursor.execute(query)
        hospitallist = self.cursor.fetchall()
        if(hospitallist):
            return hospitallist
        else:
            return None
    
    def getHospitalDonorList(self):
        query = """SELECT  * FROM user where donationType='d'"""
        self.cursor.execute(query)
        donorlist= self.cursor.fetchall()
        if(donorlist):
            return donorlist
        else:
            return None

    def getHospitalReceiverList(self):
        query = """SELECT  * FROM user where donationType='r'"""
        self.cursor.execute(query)
        receiverlist= self.cursor.fetchall()
        if(receiverlist):
            return receiverlist
        else:
            return None

    def hospitalLoginAuthentication(self,hemail,hpassword):
        query = """SELECT  * FROM hospital where emailID=%s  AND password=%s"""
        self.cursor.execute(query,(hemail, hpassword))
        result = self.cursor.fetchone()
        if(result):
            return result
        else:
            return None
