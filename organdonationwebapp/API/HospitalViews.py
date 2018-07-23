from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.Hospital.Hospital as ho
import organdonationwebapp.Hospital.HospitalHome as hho
import organdonationwebapp.Hospital.HospitalDonorList as hdl
import organdonationwebapp.Hospital.HospitalRecipientList as hrl
import organdonationwebapp.Hospital.HospitalRequestList as hprl
import organdonationwebapp.Hospital.ValidatePassword as val
import organdonationwebapp.Hospital.DBValidatePassword as DBval
import organdonationwebapp.API.Logger as log
import json
import binascii


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
    g.logger = log.MyLogger.__call__().get_logger()
    g.logger.debug("Acquired Singleton Logger")


@app.route('/hospitalregistration', methods=['GET','POST'])
def hospitalRegistration():
    if request.method == 'POST':
        hospital_data= json.dumps(request.form.to_dict())
        hospital_json = json.loads(hospital_data)
        data = request.files['certificate']
        bcertificate=data.read()
        certificate =binascii.hexlify(bcertificate)
        valPassword = DBval.DBValidatePassword(hospital_json['password'])
        password_value = valPassword.isValid()
        if(password_value):
            hospital = ho.construct_Hospital(ho.Hospital, hospital_json, certificate)
            if(hospital.registerHospital()):
                g.logger.info("Logged in successfully")
                return redirect(url_for('hospitalLogin'))
            else:
                g.logger.error("Error Inserting Data")
        else:
            return "Incorrect Password Value"
    return render_template('hospitalregistration.html')


@app.route('/', methods=['GET','POST'])
def hospitalLogin():
    if request.method == 'POST':
        hospital_data= json.dumps(request.form.to_dict())
        hospital_json = json.loads(hospital_data)
        if(hospital_json['submit']=='submit'):
            hospital = ho.construct_Hospital(ho.Hospital, hospital_json, None)
            session.pop('user', None)
            if(hospital.loginHospital()):
                session['user']= hospital_json['emailID']
                g.logger.info("Logged in")
                return redirect(url_for('hospitalHome', emailID=session['user']))
            else:   
                g.logger.error("User did not register")
                return "Please register"
        elif(hospital_json['submit']=='SignUp'):
            usertype = hospital_json['type']
            if(usertype =="Donor/Receiver"):
                return redirect(url_for('registerUser'))
            else:
                return redirect(url_for('hospitalRegistration'))
    return render_template('loginpage.html')


@app.route('/hospitalHome/<emailID>', methods=['GET','POST'])
def hospitalHome(emailID=None):
    if g.user:
        hemail=g.user
        hospitalhome = hho.HospitalHome(emailID)
        hospital_name = hospitalhome.getHospitalName()
        requestlist = hprl.HospitalRequestList(hemail)
        request_list = requestlist.getPendingRequestList()
        donorlist = hdl.HospitalDonorList(hospital_name[0])
        donor_list = donorlist.getDonorList()
        recipientlist = hrl.HospitalRecipientList(hospital_name[0])
        recipient_list = recipientlist.getRecipientList()
        if request.method == 'POST':
            data= json.dumps(request.form.to_dict())
            datajson = json.loads(data)
            if('requestID' in datajson):
                requestID = request.form['requestID']
                return redirect(url_for('donorHospitalRequestPage', requestID=requestID))
            if('submit' in datajson):
                if(request.form['submit']=='View Donor List'):
                    return redirect(url_for('donorList'))
                elif(request.form['submit']=='View Receiver List'):
                    return redirect(url_for('receiverList'))
        return render_template('hospitalHome.html',request = request_list,donor = donor_list, receiver = recipient_list)
    return redirect(url_for('hospitalLogin', emailID=emailID))