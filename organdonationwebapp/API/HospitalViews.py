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
import organdonationwebapp.API.Authenticator as auth
import organdonationwebapp.API.Register as res
import json
import binascii


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
    g.logger = log.MyLogger.__call__().get_logger()
    g.logger.debug("Acquired Singleton Logger")


@app.route('/hospitalregistration/<usertype>', methods=['GET','POST'])
def hospitalRegistration(usertype = None):
    if request.method == 'POST':
        hospital_data= json.dumps(request.form.to_dict())
        registerJson = json.loads(hospital_data)
        data = request.files['certificate']
        bcertificate=data.read()
        certificate =binascii.hexlify(bcertificate)
        valPassword = DBval.DBValidatePassword(registerJson['password'])
        password_value = valPassword.isValid()
        if(password_value):
            registerObject = res.Register(registerJson, certificate, usertype)
            valid, url = registerObject.registerEntity()
            if(valid):
                g.logger.info("Registered Successfully")
                flash("Registered Successfully")
                return redirect(url_for('Login'))
            else:
                g.logger.error("Error Inserting Data") 
                flash("Registration error") 
        else:
            g.logger.error("Incorrect Password Value")
            flash("Incorrect Password Value") 
    return render_template('hospitalregistration.html')


@app.route('/', methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        login_data= json.dumps(request.form.to_dict())
        login_json = json.loads(login_data)
        if(login_json['submit']=='submit'):
            authenticatorObject = auth.Authenticator(login_json)
            session.pop('user', None)
            valid, url = authenticatorObject.validateLogin()
            if(valid):
                session['user']= login_json['emailID']
                g.logger.info("Logged in")
                flash("Logged in")
                return redirect(url)
            else:   
                g.logger.error("User did not register")
                flash("Please register")
        elif(login_json['submit']=='SignUp'):
            usertype = login_json['type']
            if(usertype =="Donor or Receiver"):
                return redirect(url_for('registerUser', usertype = usertype))
            else:
                return redirect(url_for('hospitalRegistration',usertype = usertype))
    return render_template('loginpage.html')


@app.route('/hospitalHome/<emailID>', methods=['GET','POST'])
def hospitalHome(emailID=None):
    if g.user:
        hemail=g.user
        # print(hemail)
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


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   flash("User logged out Successfully")
   return redirect(url_for('Login'))