from flask import Flask, render_template, request, redirect, session, url_for, g
from organdonationwebapp import app, sc
import mysql.connector

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/donorList', methods=['GET'])
def donorList():
    return render_template('donorList.html')

@app.route('/donorReceiverRequest', methods=['GET'])
def donorReceiverRequest():
    return render_template('donorReceiverRequest.html')

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

@app.route('/signup', methods=['GET'])
def registerHospital():
    return render_template('signup.html')

@app.route('/hospitaldonor', methods=['GET'])
def hospitalDonorPage():
    return render_template('DonorReceiverRequest.html')

@app.route('/adminlogin', methods=['GET','POST'])
def adminLoginPage():
    if request.method == 'POST':
        hospitaldata = request.form
        email =hospitaldata['emailID']
        password =hospitaldata['password']
        user = sc.adminLoginAuthentication(email, password)
        if(user):
            return redirect(url_for('adminHomepage', username=user))
        else:
            return 'Authentication failed!!'
    return render_template('adminlogin.html')

@app.route('/adminhome/<username>', methods=['GET','POST'])
def adminHomepage(username=None):
    hospitallist = sc.getHospitalList()
    if(hospitallist):
        return render_template('adminhome.html', list=hospitallist,username=username)
    return render_template('adminhome.html', username=username)

@app.route('/hospitalHome', methods=['GET'])
def hospitalHome():
    if g.user:
        if request.method == 'GET':
            res2 = sc.getHospitalDonorList()
            res3 = sc.getHospitalReceiverList()
        return render_template('hospitalHome.html',donor=res2, receiver=res3)
    return redirect(url_for('hospitalLogin'))

@app.route('/loginPage', methods=['GET','POST'])
def hospitalLogin():
    if request.method == 'POST':
        hospitaldata = request.form
        email =hospitaldata['hemail']
        password =hospitaldata['hpassword']
        session.pop('user', None)
        res = sc.hospitalLoginAuthentication(email,password)
        if(res):
            session['user']= email
            return redirect(url_for('hospitalHome'))
        else:   
            return "Please register"
    return render_template('loginPage.html')