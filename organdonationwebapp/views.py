from flask import Flask, render_template, request, redirect, session, url_for, g
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
    if g.user:
        if request.method == 'GET':
            sqlcnx = mysql.connector.connect(user='CSCI5308_16_DEVINT_USER',password='CSCI5308_16_DEVINT_16175',host='db-5308.cs.dal.ca',database='CSCI5308_16_DEVINT')
            cursor2 = sqlcnx.cursor()
            query2 = """SELECT  * FROM user where donationType='d'"""
            cursor2.execute(query2)
            res2 = cursor2.fetchall()
            cursor3 = sqlcnx.cursor()
            query3 = """SELECT  * FROM user where donationType='r'"""
            cursor3.execute(query3)
            res3 = cursor3.fetchall()
        return render_template('hospitalHome.html',donor=res2, receiver=res3)
    return redirect(url_for('hospitalLogin'))

@app.route('/loginPage', methods=['GET','POST'])
def hospitalLogin():
    if request.method == 'POST':
        hospitaldata = request.form
        email =hospitaldata['hemail']
        password =hospitaldata['hpassword']
        session.pop('user', None)
        sqlcnx = mysql.connector.connect(user='CSCI5308_16_DEVINT_USER',password='CSCI5308_16_DEVINT_16175',host='db-5308.cs.dal.ca',database='CSCI5308_16_DEVINT')
        cursor1 = sqlcnx.cursor()
        query = """SELECT  * FROM hospital where emailID=%s  AND password=%s"""
        cursor1.execute(query,(email, password))
        res = cursor1.fetchone()
        if(res):
            session['user']= email
            return redirect(url_for('hospitalHome'))
        else:   
            return "Please register"
    return render_template('loginPage.html')

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/hospitalRegestration', methods=['GET'])
def hospitalRegestration():
    return render_template('hospitalRegestration.html')

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