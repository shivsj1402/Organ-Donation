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
        query = """SELECT emailID, validate FROM hospital"""
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


    def donorHospitalShowProfile(self, recipientEmail):
        #print ("SQL",(recipientEmail))
        query = """SELECT userFirstName, userLastName, emailID, dob, sex, organ FROM user WHERE emailID=%s"""
        self.cursor.execute(query,(recipientEmail,))
        userdata = self.cursor.fetchall()
        for row in userdata:
            firstname = row[0]
            lastname = row[1]
            email = row[2]
            date_of_birth = row[3]
            sex = row[4]
            organ = row[5]
        if(userdata):
            return userdata
        else:
            return None


    def closeDBConnection(self):
        self.cursor.close()
        self.connection.close()