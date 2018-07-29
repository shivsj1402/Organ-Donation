from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app, sc
import organdonationwebapp.User.User as us
import organdonationwebapp.User.OpenRequestDetails as rdo
import organdonationwebapp.Hospital.HospitalList as hlo
import organdonationwebapp.User.Donor.Donor as do
import organdonationwebapp.User.Recipient.Recipient as ro
import organdonationwebapp.User.Donor.UpdateRequestStatus as uro
import organdonationwebapp.API.Register as res
import json
import binascii


@app.route('/signup/<usertype>', methods=['GET','POST'])
def registerUser(usertype = None):
    organ =[]
    hospitalList = hlo.HospitalList()
    hospital_list = hospitalList.getGlobalHospitalList()
    if request.method == 'POST':
        user_dict = request.form.to_dict()
        organ = request.form.getlist('organ')
        user_dict['organ'] = organ
        user_data= json.dumps(user_dict)
        registerJson = json.loads(user_data)
        registerObject = res.Register(registerJson, None, usertype)
        valid, url = registerObject.registerEntity()
        if(valid):
            if(g.user):
                flash ("Registered Successfully")
                return redirect(url_for('hospitalHome', emailID = g.user))
            else:
                flash ("Registered Successfully")
                return redirect(url_for('Login'))
        else:
            flash("Registration error")
            return "<h2> Registration failed </h2>"
    return render_template('signup.html', hlist=hospital_list)


@app.route('/donorhospitalrequest/<requestID>', methods=['GET','POST'])
def donorHospitalRequestPage(requestID=None):
    donor_userdata = None
    recipient_userdata = None
    requestdata =rdo.OpenRequestDetails(requestID)
    request_userdata = requestdata.getOpenRequestData()
    donorEmail=request_userdata[0][0]
    recipientEmail=request_userdata[0][1]
    organ=request_userdata[0][2]
    if(donorEmail):
        donor = do.Donor(donorEmail)
        donor_userdata = donor.donorHospitalRequestPage()
    if(recipientEmail):
        recipient = ro.Recipient(recipientEmail)
        recipient_userdata = recipient.donorHospitalPageRecipientList()
    if(recipient_userdata and donor_userdata):
        if request.method == 'POST':
            request1= json.dumps(request.form.to_dict())
            request_json = json.loads(request1)
            if('submit' in request_json):
                updateRequestStatus = uro.UpdateRequestStatus(request.form['submit'], requestID)
                request_status = updateRequestStatus.setRequestsStatus()
                if(request_status):
                    flash("Request Status updated successfully")
                else:
                    flash("Error updating request status. Please try again later!")
        return render_template('donorreceiverrequest.html', recipientdata=recipient_userdata, donordata=donor_userdata, organ=organ)
    else:
        flash("No donor/reciever available for this Request!")
        return render_template('donorreceiverrequest.html', recipientdata=recipient_userdata, donordata=donor_userdata, organ=organ)
