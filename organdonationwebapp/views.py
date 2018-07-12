from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app, sc
from io import BytesIO
import mysql.connector
import logging

logging.basicConfig(filename='file.log',level=logging.DEBUG)

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/donorList', methods=['GET'])
def donorList():
    if g.user:
        if request.method == 'GET':
            dlist= sc.getDonorList()
            return render_template('donorList.html', dlist=dlist)
    return redirect(url_for('hospitalLogin'))

@app.route('/donorReceiverRequest', methods=['GET'])
def donorReceiverRequest():
    return render_template('donorReceiverRequest.html')

@app.route('/hospitalregistration', methods=['GET','POST'])
def hospitalRegistration():
    if request.method == 'POST':
        hospitalName = request.form['hospitalName']
        emailID = request.form['emailID']
        phone = request.form['phone']
        address = request.form['address']
        province = request.form['province']
        city = request.form['city']
        password = request.form['password']
        data = request.files['certificate']
        certificate=data.read()

        message = sc.hospitalRegistrattion(hospitalName,emailID,phone,address,province,city,password,certificate)
        if(message=="Done"):
            return redirect(url_for('hospitalLogin'))
        else:
            logging.warning("Error Inserting Data")  
    return render_template('hospitalregistration.html')

@app.route('/receiverList', methods=['GET'])
def receiverList():
    if g.user:
        if request.method == 'GET':
            rlist= sc.getReceiverList()
            return render_template('receiverList.html', rlist=rlist)
    return redirect(url_for('hospitalLogin'))

@app.route('/receiverProfile', methods=['GET'])
def receiverProfile():
    return render_template('receiverProfile.html')

@app.route('/requestFinal', methods=['GET'])
def requestFinal():
    return render_template('requestFinal.html')

@app.route('/signup', methods=['GET','POST'])
def registerUser():
    organ =[]
    hlist=sc.getHospitalList()
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        sex = request.form['sex']
        dob = request.form['dob']
        address = request.form['address']
        province = request.form['province']
        city = request.form['city']
        hospital = request.form['hname']
        bloodgroup = request.form['bloodgroup']
        usertype = request.form['usertype']
        organ = request.form.getlist('organ')
        for item in organ:
            message= sc.userRegistration(first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, item)
            if(message=="Done"):
                logging.info("User Registered")
            else:
                logging.warning("Error Inserting Data")
    return render_template('signup.html', hlist=hlist)

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
            logging.warning ('Authentication failed!!')
    return render_template('adminlogin.html')

@app.route('/adminhome/<username>', methods=['GET','POST'])
def adminHomepage(username=None, hospitalEmail=None):
    if request.method == 'POST':
        validate_hospital = request.form
        hospitalEmail = validate_hospital['validate']
        if(hospitalEmail != " "):
            hospitalEmail = sc.validateHospital(hospitalEmail)
    hospitallist = sc.getHospitalList()
    #print(hospitallist[6][7])
    #return send_file(BytesIO(hospitallist[6][7]), attachment_filename='certificate.pdf', as_attachment=True)
    if(hospitallist):
        return render_template('adminhome.html', list=hospitallist,username=username)
    return render_template('adminhome.html', username=username)

@app.route('/dummyrequest', methods=['GET', 'POST'])
def dummyRequest():
    if request.method == 'POST':
        requestdata = request.form
        # recipientID = recipientdata['recipientemail']
        requestID = requestdata['requestID']
        requestdata = sc.organRequest(requestID)
        print("View",(requestdata[0]))
        if(requestdata):
            return redirect(url_for('receiverHospitalRequestPage', donorEmail=requestdata[0],recipientEmail=requestdata[1],organ=requestdata[2]))
    return render_template('dummyrequests.html')

@app.route('/donorhospitalrequest/<donorEmail>/<recipientEmail>/<organ>', methods=['GET'])
def donorHospitalRequestPage(donorEmail=None, recipientEmail=None, organ=None):
    donor_userdata = None
    recipient_userdata = None
    print("Donor EMail:", (donorEmail))
    if(donorEmail):
        donor_userdata = sc.donorHospitalShowDonorProfile(donorEmail)
        print("AAAA:",(donor_userdata))
    if(recipientEmail):
        recipient_userdata = sc.donorHospitalShowReceiverProfile(recipientEmail)
        print(recipient_userdata)
    if(recipient_userdata and donor_userdata):
        return render_template('donorreceiverrequest.html', recipientdata=recipient_userdata, donordata=donor_userdata, organ=organ)

@app.route('/receiverhospitalrequest/<recipientEmail>', methods=['GET','POST'])
def receiverHospitalRequestPage(recipientEmail=None):
    if(recipientEmail != " "):
        userdata = sc.receiverHospitalShowProfile(recipientEmail)
        userdata_organ = sc.receiverHospitalShowOrgan(recipientEmail)
        donor_organ_data = []
        for organ in userdata_organ:
            donor_organ_data.extend(sc.recommendedDonorList(organ[0]))
        print (donor_organ_data)
        if(userdata and userdata_organ):
            return render_template('receiverprofile.html', recipientdata=userdata, organdata=userdata_organ, donororgandata=donor_organ_data)

@app.route('/donorprofile/<donorEmail>', methods=['GET'])
def donorProfilePage(donorEmail=None):
    donor_userdata = None
    print("Donor Email:", (donorEmail))
    if(donorEmail):
        donor_userdata = sc.donorHospitalShowDonorProfile(donorEmail)
        print("AAAA:",(donor_userdata))
    if(donor_userdata):
        return render_template('donorprofile.html', donordata=donor_userdata)

@app.route('/hospitalHome', methods=['GET','POST'])
def hospitalHome():
    if g.user:
        hemail=g.user
        hname=sc.getHospitalName(hemail)
        if request.method == 'POST':
            if(request.form['submit']=='View Donor List'):
                return redirect(url_for('donorList'))
            elif(request.form['submit']=='View Receiver List'):
                return redirect(url_for('receiverList'))
        res2 = sc.getHospitalDonorList(hname[0])
        res3 = sc.getHospitalReceiverList(hname[0])
        return render_template('hospitalHome.html',donor=res2, receiver=res3)
    return redirect(url_for('hospitalLogin'))

@app.route('/', methods=['GET','POST'])
def hospitalLogin():
    if request.method == 'POST':
        hospitaldata = request.form
        email =hospitaldata['hemail']
        password =hospitaldata['hpassword']
        # usertype = hospitaldata['type']
        session.pop('user', None)
        if(request.form['submit']=='submit'):
            res = sc.hospitalLoginAuthentication(email,password)
            if(res):
                session['user']= email
                logging.info("User " + session['user'] + " has logged in")
                return redirect(url_for('hospitalHome'))
            else:   
                logging.error("Invalid user")
                flash("Not an existing user. Please Register!!")
                return render_template('loginpage.html')
        elif(request.form['submit']=='SignUp'):
            if(usertype =="Donor/Receiver"):
                return redirect(url_for('registerUser'))
            else:
                return redirect(url_for('hospitalRegistration'))
    return render_template('loginpage.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('PageNotFound.html'), 404

@app.route('/log')
def log():
    with open("file.log", "r") as f:
        content = f.read()
    return render_template('log.html', content=content)