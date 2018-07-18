from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app, sc
import organdonationwebapp.Admin.Admin as ao
import organdonationwebapp.Hospital.Hospital as ho
import organdonationwebapp.Hospital.ValidateHospital as vho
import organdonationwebapp.Hospital.HospitalList as hlo
import organdonationwebapp.Hospital.HospitalHome as hho
import organdonationwebapp.Hospital.HospitalDonorList as hdl
import organdonationwebapp.Hospital.HospitalRecipientList as hrl
import organdonationwebapp.User.User as us
import organdonationwebapp.User.Donor.Donor as do
import organdonationwebapp.User.Donor.DonorProfile as dop
import organdonationwebapp.User.Donor.DonorListDetails as dlo
import organdonationwebapp.User.Recipient.Recipient as ro
import organdonationwebapp.User.Recipient.RecipientListDetails as rlo
import organdonationwebapp.User.Recipient.ShowRecipientProfile as rpo
import organdonationwebapp.User.Donor.ShowRecommendedDonors as dpo
from io import BytesIO
import mysql.connector
import json

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/donorReceiverRequest', methods=['GET'])
def donorReceiverRequest():
    return render_template('donorReceiverRequest.html')


@app.route('/hospitalregistration', methods=['GET','POST'])
def hospitalRegistration():
    if request.method == 'POST':
        hospital_data= json.dumps(request.form.to_dict())
        hospital_json = json.loads(hospital_data)
        data = request.files['certificate']
        certificate=data.read()
        hospital = ho.Hospital(hospital_json, certificate)
        if(hospital.registerHospital()):
            return redirect(url_for('hospitalLogin'))
        else:
            print("Error Inserting Data")  
    return render_template('hospitalregistration.html')


@app.route('/', methods=['GET','POST'])
def hospitalLogin():
    if request.method == 'POST':
        hospital_data= json.dumps(request.form.to_dict())
        hospital_json = json.loads(hospital_data)
        if(hospital_json['submit']=='submit'):
            hospital = ho.Hospital(hospital_json)
            session.pop('user', None)
            if(hospital.loginHospital()):
                print("12344",(hospital.loginHospital()))
                session['user']= hospital_json['emailID']
                return redirect(url_for('hospitalHome', emailID=session['user']))
            else:   
                return "Please register"
        elif(hospital_json['submit']=='SignUp'):
            usertype = hospital_json['type']
            if(usertype =="Donor/Receiver"):
                return redirect(url_for('registerUser'))
            else:
                return redirect(url_for('hospitalRegistration'))
    return render_template('loginPage.html')


@app.route('/hospitalHome/<emailID>', methods=['GET','POST'])
def hospitalHome(emailID=None):
    if g.user:
        hemail=g.user
        print(hemail)
        hospitalhome = hho.HospitalHome(emailID)
        hospital_name = hospitalhome.getHospitalName()
        print("1234",hospital_name)
        if request.method == 'POST':
            if(request.form['submit']=='View Donor List'):
                return redirect(url_for('donorList'))
            elif(request.form['submit']=='View Receiver List'):
                return redirect(url_for('receiverList'))
        donorlist = hdl.HospitalDonorList(hospital_name[0])
        donor_list = donorlist.getDonorList()
        recipientlist = hrl.HospitalRecipientList(hospital_name[0])
        recipient_list = recipientlist.getRecipientList()
        return render_template('hospitalHome.html',donor=donor_list, receiver=recipient_list)
    return redirect(url_for('hospitalLogin', emailID=emailID))


@app.route('/adminlogin', methods=['GET','POST'])
def adminLoginPage():
    if request.method == 'POST':
        user = None
        admin_data = json.dumps(request.form.to_dict())
        admin_json = json.loads(admin_data)
        if(admin_json['submit']=='submit'):
            admin = ao.Admin(admin_json)
            session.pop('user', None)
            if(admin.loginAdmin()):
                session['user']= admin_json['emailID']
                print(session['user'])
                user = session['user']
                return redirect(url_for('adminHomepage', username=user))
            else:
                return 'Authentication failed!!'
    return render_template('adminlogin.html')


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
        user_dict = request.form.to_dict()
        organ = request.form.getlist('organ')
        user_dict['organ'] = organ
        user_data= json.dumps(user_dict)
        user_json = json.loads(user_data)
        user = us.User(user_json)
        if user.registerUser():
            return "<h2> Registered Successfully </h2>"
        else:
            return "<h2> Registration failed </h2>"
    return render_template('signup.html', hlist=hlist)


@app.route('/hospitaldonor', methods=['GET'])
def hospitalDonorPage():
    return render_template('DonorReceiverRequest.html')


@app.route('/adminhome/<username>', methods=['GET','POST'])
def adminHomepage(username=None, hospitalEmail=None):
    if request.method == 'POST':
        validate_hospital = json.dumps(request.form.to_dict())
        hospital_json = json.loads(validate_hospital)
        if(hospital_json != " "):
            validate = vho.ValidateHospital(hospital_json)
            hospitalEmail = validate.updateValidateHospitalFlag()
    hospitalList = hlo.HospitalList()
    hospital_list = hospitalList.getGlobalHospitalList()
    #print(hospitallist[6][7])
    #return send_file(BytesIO(hospitallist[6][7]), attachment_filename='certificate.pdf', as_attachment=True)
    if(hospital_list):
        return render_template('adminhome.html', list=hospital_list,username=username)
    return render_template('adminhome.html', username=username)


@app.route('/dummyrequest', methods=['GET', 'POST'])
def dummyRequest():
    if request.method == 'POST':
        requestdata = request.form
        requestID = requestdata['requestID']
        requestdata = sc.organRequest(requestID)
        if(requestdata):
            return redirect(url_for('receiverHospitalRequestPage', donorEmail=requestdata[0],recipientEmail=requestdata[1],organ=requestdata[2]))
    return render_template('dummyrequests.html')


@app.route('/donorhospitalrequest/<donorEmail>/<recipientEmail>/<organ>', methods=['GET'])
def donorHospitalRequestPage(donorEmail=None, recipientEmail=None, organ=None):
    donor_userdata = None
    recipient_userdata = None
    if(donorEmail):
        donor = do.Donor(donorEmail)
        donor_userdata = donor.donorHospitalRequestPage()
    if(recipientEmail):
        recipient = ro.Recipient(recipientEmail)
        recipient_userdata = recipient.donorHospitalPageRecipientList()
    if(recipient_userdata and donor_userdata):
        return render_template('donorreceiverrequest.html', recipientdata=recipient_userdata, donordata=donor_userdata, organ=organ)


@app.route('/receiverList', methods=['GET'])
def receiverList():
    if g.user:
        recipientList = rlo.RecipientListDetails(g.user)
        rec_list_details = recipientList.getRecipientList()
        if(rec_list_details):
            return render_template('receiverList.html', rlist=rec_list_details)
    return redirect(url_for('hospitalLogin'))


@app.route('/donorList', methods=['GET'])
def donorList():
    if g.user:
        donorList = dlo.DonorListDetails(g.user)
        don_list_details = donorList.getDonorList()
        if(don_list_details):
            return render_template('donorList.html', dlist=don_list_details)
    return redirect(url_for('hospitalLogin'))


@app.route('/receiverhospitalrequest/<recipientEmail>', methods=['GET','POST'])
def receiverHospitalRequestPage(recipientEmail=None):
    if(recipientEmail != " "):
        recipient_data = rpo.ShowRecipientProfile(recipientEmail)
        recipient_profile = recipient_data.getRecipientProfile()
        recipient_organ_data = recipient_data.getRecipientOrgans()
        donor_organ_data = []
        for organ in recipient_organ_data:
            donor_data = dpo.ShowRecommendedDonors(organ[0])
            donor_organ_data.extend(donor_data.getrecommendedDonorList())
        print (donor_organ_data)
        if(recipient_profile and recipient_organ_data):
            return render_template('receiverprofile.html', recipientdata=recipient_profile, organdata=recipient_organ_data, donororgandata=donor_organ_data)


@app.route('/donorprofile/<donorEmail>', methods=['GET'])
def donorProfilePage(donorEmail=None):
    donor_userdata = None
    if(donorEmail):
        donorprofile = dop.DonorProfile(donorEmail)
        donor_userdata = donorprofile.getDonorProfile()
        print("donor_userdata",(donor_userdata))
    if(donor_userdata):
        return render_template('donorprofile.html', donordata=donor_userdata)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('PageNotFound.html'), 404