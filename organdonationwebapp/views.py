from flask import Flask, render_template, request, redirect, url_for
from organdonationwebapp import app, sc
import mysql.connector

# @app.route('/admin', methods=['GET'])
# def welcomeToAdminPortal():
#     return render_template('adminlogin.html')

@app.route('/hospital', methods=['GET'])
def takeToHospital():
    return render_template('hospitallogin.html')

@app.route('/helloworld', methods=['GET'])
def takeToHelloWorld():
    return "<p>hello world test</p>"

# @app.route('/login', methods=['GET'])
# def takeToAdmin():
#     return render_template('loginpage.html')

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