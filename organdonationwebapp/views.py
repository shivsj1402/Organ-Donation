from flask import Flask, render_template, request, redirect, url_for, flash
from organdonationwebapp import app, sc

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

@app.route('/hospitalLogin', methods=['GET'])
def hospitalLogin():
    return render_template('hospitalLogin.html')

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
def adminHomepage(username=None, hospitalEmail=None):
    if request.method == 'POST':
        validate_hospital = request.form
        hospitalEmail = validate_hospital['validate']
        if(hospitalEmail != " "):
            hospitalEmail = sc.validateHospital(hospitalEmail)
    hospitallist = sc.getHospitalList()
    if(hospitallist):
        return render_template('adminhome.html', list=hospitallist,username=username)
    return render_template('adminhome.html', username=username)


@app.route('/dummyrequest', methods=['GET', 'POST'])
def dummyRequest():
    if request.method == 'POST':
        recipientdata = request.form
        recipientEmail = recipientdata['recipientemail']
        if(recipientEmail):
            return redirect(url_for('donorHospitalRequestPage', recipientEmail=recipientEmail))
    return render_template('dummyrequests.html')


@app.route('/donorhospitalrequest/<recipientEmail>', methods=['GET','POST'])
def donorHospitalRequestPage(recipientEmail=None):
    #print ("Views",(recipientEmail))
    if(recipientEmail != " "):
        userdata = sc.donorHospitalShowProfile(recipientEmail)
        if(userdata):
            return render_template('donorreceiverrequest.html', recipientdata=userdata)