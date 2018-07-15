from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app, sc
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, RadioField, widgets, SelectMultipleField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Email, Length, Regexp, EqualTo
from io import BytesIO
import mysql.connector
import logging
import binascii

logging.basicConfig(filename='file.log',level=logging.DEBUG)

class hospitalLoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),(Email( message="Please enter in valid email format"))])
    password = PasswordField('password', validators=[InputRequired(message="password is required")])

class adminLoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),(Email( message="Please enter in valid email format"))])
    password = PasswordField('password', validators=[InputRequired(message="password is required")])

class hospitalSignupForm(FlaskForm):
    hospitalname = StringField('hospitalname',validators=[InputRequired(), Regexp('^[a-zA-Z ]*$',message="Please input only characters"),(Length(min=5, max= 20, message="Should be between 5 to 20 Characters."))])
    hospitalemail= StringField('hospitalemail', validators=[InputRequired(), (Email(message="Enter Email in a vaid format"))])
    phonenumber= StringField('phonenumber', validators=[InputRequired(), Regexp('^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',message="Please input only characters")])
    address = StringField('address', validators=[InputRequired(),Regexp('^\\d+ [a-zA-Z ]+$', message="Enter Address in valid format")])
    province= SelectField('province',choices=[('NS','NS'), ('ON', 'ON'), ('AB', 'AB'), ('NB', 'NB')])
    city= SelectField('city',choices=[('Halifax', 'Halifax'), ('Tornoto', 'Toronto'), ('Vancouver', 'Vancouver'), ('Fedrection', 'Fedrection')])
    password = PasswordField('password', validators=[InputRequired(),(Length(min=8, message="shoule be atlease 8 characters"))])
    cpassword= PasswordField('cpassword', validators=[InputRequired(), EqualTo('password', message="Shoule be same as password"), Length(min=8, message="shoule be atlease 8 characters")])

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class userSignup(FlaskForm):
    userfirstname= StringField('userfirstname',validators=[InputRequired(), Regexp('^[a-zA-Z ]*$',message="Please input only characters"),(Length(min=5, max= 20, message="Should be between 5 to 20 Characters."))])
    userlastname = StringField('userlastname', validators=[InputRequired(), Regexp('^([a-zA-Z]+[\-]?[a-zA-Z]+[ ]?)+$',message="Please input only characters"),(Length(min=5, max= 20, message="Should be between 5 to 20 Characters."))])
    phonenumber= StringField('phonenumber', validators=[InputRequired(), Regexp('^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',message="Please input only characters")])
    useremail= StringField('useremail', validators=[InputRequired(), (Email(message="Enter Email in a vaid format"))])
    sex= SelectField('sex',choices=[('M', 'Male'), ('F', 'Female')])
    dob = DateField('dob', format='%Y-%m-%d', validators=[InputRequired()])
    address = StringField('address',validators=[InputRequired(),Regexp('^\\d+ [a-zA-Z ]+$', message="Enter Address in valid format")])
    province= SelectField('province',choices=[('NS','NS'), ('ON', 'ON'), ('AB', 'AB'), ('NB', 'NB')])
    city= SelectField('city',choices=[('Halifax', 'Halifax'), ('Tornoto', 'Toronto'), ('Vancouver', 'Vancouver'), ('Fedrection', 'Fedrection')])
    bloodgroup= SelectField('bloodgroup',choices=[('A+','A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')])
    
    usertype =RadioField('usertype', choices=[('d','Donor'),('r','Receiver')])
    string_of_files = ['liver\r\nheart\r\neyes\r\nlidney\r\n']
    list_of_files = string_of_files[0].split()
    files = [(x, x) for x in list_of_files]
    organ = MultiCheckboxField('Label', choices=files, validators=[InputRequired()])



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
    form = hospitalSignupForm()
    if form.validate_on_submit():
        hospitalName = form.hospitalname.data
        emailID = form.hospitalemail.data
        phone = form.phonenumber.data
        address = form.address.data
        province = form.province.data
        city = form.city.data
        password = form.password.data
        data = request.files['certificate']
        mes =sc.hospitalexist(emailID)
        print(mes)
        if(mes== "NotExist"):
            # if(data):
            certificate=data.read()
            bcertificate =binascii.hexlify(certificate)
            message = sc.hospitalRegistrattion(hospitalName,emailID,phone,address,province,city,password,bcertificate)
            if(message=="Done"):
                flash("Registered Sucessfully")
                return redirect(url_for('hospitalLogin'))
            else:
                logging.warning("Error Inserting Data")  
                return render_template('hospitalregistration.html', form = form)
            # else:
            #     flash("please provide a valid certificate")
            #     return render_template('hospitalregistration.html', form = form)
        else:
            flash("email already exists")
            return render_template('hospitalregistration.html', form = form)
    return render_template('hospitalregistration.html', form = form)

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
    hlist=sc.getHospitalList()
    organ =[]
    form = userSignup()
    if form.validate_on_submit():
        first_name = form.userfirstname.data
        last_name = form.userlastname.data
        phone_number = form.phonenumber.data
        email = form.useremail.data
        sex = form.sex.data
        dob = form.dob.data
        address = form.address.data
        province = form.province.data
        city = form.city.data
        bloodgroup = form.bloodgroup.data
        usertype = form.usertype.data
        organ = form.organ.data
        hospital = request.form['hname']
        for item in organ:
            message= sc.userRegistration(first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, item)
            if(message=="Done"):
                logging.info("User Registered")
                flash("User registered")
                redirect(url_for('hospitalLogin'))
            else:
                logging.warning("Error Inserting Data")
                flash('error occoured!')
                return render_template('signup.html', form=form, hlist=hlist)  
        return render_template('signup.html', form = form, hlist=hlist,)       
    print("validation issue")
    return render_template('signup.html',form = form ,hlist=hlist)

@app.route('/hospitaldonor', methods=['GET'])
def hospitalDonorPage():
    return render_template('DonorReceiverRequest.html')

@app.route('/adminlogin', methods=['GET','POST'])
def adminLoginPage():
    form = adminLoginForm()
    if form.validate_on_submit():
        email =form.username.data
        password =form.password.data
        user = sc.adminLoginAuthentication(email, password)
        if(user):
            return redirect(url_for('adminHomepage', username=user))
        else:
            logging.warning ('Authentication failed!!')
            flash("Please Enter Correct Details!!")
            return render_template('adminlogin.html', form= form)
    return render_template('adminlogin.html', form= form)

@app.route('/adminhome/<username>', methods=['GET','POST'])
def adminHomepage(username=None, hospitalEmail=None):
    if request.method == 'POST':
        validate_hospital = request.form
        hospitalEmail = validate_hospital['validate']
        if(hospitalEmail != " "):
            hospitalEmail = sc.validateHospital(hospitalEmail)
    hospitallist = sc.getHospitalList()
    # print(hospitallist[1][7])
    # return send_file(BytesIO(hospitallist[1][7]), attachment_filename='certificate.pdf', as_attachment=True)
    if(hospitallist):
        return render_template('adminhome.html', list=hospitallist,username=username)
    return render_template('adminhome.html', username=username)

@app.route('/dummyrequest', methods=['GET', 'POST'])
def dummyRequest():
    if request.method == 'POST':
        requestdata = request.form
        # recipientID = recipientdata['recipientemail']
        requestID= requestdata['requestID']
        requestdata = sc.organRequest(requestID[0])
        print("View",(requestdata[0]))
        if(requestdata):
            return redirect(url_for('receiverHospitalRequestPage', donorEmail=requestdata[0][0],recipientEmail=requestdata[0][1],organ=requestdata[0][2]))
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
    form = hospitalLoginForm()
    if form.validate_on_submit():
        email =form.username.data
        password =form.password.data
        session.pop('user', None)
        res = sc.hospitalLoginAuthentication(email,password)
        if(res):
            session['user']= email
            logging.info("User " + session['user'] + " has logged in")
            return redirect(url_for('hospitalHome'))
        else:   
            logging.error("Invalid user")
            flash("Not an existing user. Please Register!!")
            return render_template('loginpage.html', form= form)
    return render_template('loginpage.html', form= form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('PageNotFound.html'), 404

@app.route('/log')
def log():
    with open("file.log", "r") as f:
        content = f.read()
    return render_template('log.html', content=content)