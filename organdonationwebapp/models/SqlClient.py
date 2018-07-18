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
            logging.info("Error connecting to Database")
            exit(1)


    def organRequest(self, requestID):
        print(requestID)
        self.cursor.callproc('organrequest',[requestID])
        res = self.cursor.stored_results()
        for result in res:
            requestdata= result.fetchall()
            print("Hello",(requestdata))
            if(requestdata):
                return requestdata
            else:
                return None
    
    def closeDBConnection(self):
        self.cursor.close()
        self.connection.close()