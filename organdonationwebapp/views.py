from flask import Flask, render_template, request, redirect
import mysql.connector
from organdonationwebapp import app

@app.route('/helloworld', methods=['GET'])
def takeToHelloWorld():
    return "<p>hello world</p>"

@app.route('/adminLogin', methods=['GET'])
def adminPortalLogin():
    return render_template('adminLogin.html')

@app.route('/adminHome', methods=['GET'])
def adminPortalHome():
    return render_template('adminHome.html')

@app.route('/donorList', methods=['GET'])
def donorList():
    return render_template('donorList.html')

@app.route('/donorReceiverRequest', methods=['GET'])
def donorReceiverRequest():
    return render_template('donorReceiverRequest.html')

@app.route('/hospitalHome', methods=['GET'])
def hospitalHome():
    return render_template('hospitalHome.html')

@app.route('/hospitalLogin', methods=['GET','POST'])
def hospitalLogin():
    if request.method == 'POST':
        hospitaldata = request.form
        email =hospitaldata['hemail']
        password =hospitaldata['hpassword']

        sqlcnx = mysql.connector.connect(user='CSCI5308_16_DEVINT_USER',password='CSCI5308_16_DEVINT_16175',host='db-5308.cs.dal.ca',database='CSCI5308_16_DEVINT')
        cursor1 = sqlcnx.cursor()
        query = """SELECT  * FROM hospital where emailID=%s  AND password=%s"""
        cursor1.execute(query,(email, password))
        res = cursor1.fetchone()
        cursor2 = sqlcnx.cursor()
        query2 = """SELECT  * FROM user where donationType='d'"""
        cursor2.execute(query2)
        res2 = cursor2.fetchall()
        cursor3 = sqlcnx.cursor()
        query3 = """SELECT  * FROM user where donationType='r'"""
        cursor3.execute(query3)
        res3 = cursor3.fetchall()

        if(res):
            return render_template('hospitalHome.html',result=res, donor=res2, receiver=res3)
        else:   
            return "Please register"
    return render_template('hospitalLogin.html')

# @app.route('/retrival')
# def retrival():
#     sqlcnx = mysql.connector.connect(user='CSCI5308_16_DEVINT_USER',password='CSCI5308_16_DEVINT_16175',host='db-5308.cs.dal.ca',database='CSCI5308_16_DEVINT')
#     cursor1 = sqlcnx.cursor()
#     query = """SELECT  * FROM hospital"""
#     result = cursor1.execute(query)
#     hospitaldata = cursor1.fetchall()
#     return render_template('retrival.html',hospitaldata=hospitaldata )

@app.route('/hospitalRegestration', methods=['GET'])
def hospitalRegestration():
    return render_template('hospitalRegestration.html')

@app.route('/loginPage', methods=['GET'])
def loginPage():
    return render_template('loginPage.html')

@app.route('/receiverList', methods=['GET'])
def receiverList():
    return render_template('receiverList.html')

@app.route('/receiverProfile', methods=['GET'])
def receiverProfile():
    return render_template('receiverProfile.html')

@app.route('/requestFinal', methods=['GET'])
def requestFinal():
    return render_template('requestFinal.html')

@app.route('/signUp', methods=['GET'])
def signUp():
    return render_template('signUp.html')