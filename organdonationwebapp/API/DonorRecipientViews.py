from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app, sc
import organdonationwebapp.User.User as us
import organdonationwebapp.User.OpenRequestDetails as rdo
import organdonationwebapp.Hospital.HospitalList as hlo
import organdonationwebapp.Hospital.DonorHospitalID as dho
import organdonationwebapp.User.Donor.Donor as do
import organdonationwebapp.User.Recipient.Recipient as ro
import organdonationwebapp.User.Donor.ShowRecommendedDonors as dpo
import organdonationwebapp.User.Recipient.ShowRecipientProfile as rpo
import organdonationwebapp.User.Recipient.ShowRequestsStatus as sro
import organdonationwebapp.User.Donor.UpdateRequestStatus as uro
import organdonationwebapp.User.Recipient.NewDonationRequest as dro
import organdonationwebapp.API.Register as res
import organdonationwebapp.User.UpdateMedicalReports as rro
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
    print(requestID)
    print(request_userdata)
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
        return "No donor/reciever available for this Request. Please go back to previous page!"




@app.route('/receiverhospitalrequest/<recipientEmail>', methods=['GET','POST'])
def receiverHospitalRequestPage(recipientEmail=None):
    recipient_data = rpo.ShowRecipientProfile(recipientEmail)
    recipient_profile = recipient_data.getRecipientProfile()
    recipientEmail = recipient_profile[0][2] #Extracting recipient email from Recipient profile JSON
    recipient_organ_data = recipient_data.getRecipientOrgans()
    donor_organ_list = []
    for organ in recipient_organ_data:
        donor_list = dpo.ShowRecommendedDonors(organ[0])
        donor_organ_list.extend(donor_list.getrecommendedDonorList())
    requestStatus = sro.ShowRequestsStatus(recipientEmail)
    request_status_data = requestStatus.getRequestsStatus()
    approved_requests = request_status_data["approved"]
    rejected_requests = request_status_data["rejected"]
    pending_requests = request_status_data["pending"]
    if(recipient_profile and recipient_organ_data):
        if request.method == 'POST':
            donor_data= json.dumps(request.form.to_dict())
            donor_json = json.loads(donor_data)
            if(request.form['submit']=='submit'):
                if(donor_json['reports']==""):
                    flash("please enter a valid certificate")
                else:
                    data = request.files['reports']
                    breport=data.read()
                    report =binascii.hexlify(breport)
                    userType= "r"
                    recipientReport= rro.UpdateMedicalReports(recipientEmail, report, userType)
                    recipient_report_status = recipientReport.updateReports()
                    if(recipient_report_status):
                        flash("Updated Successfully")
                    else:
                        flash("Insertion Error!") 
            else:
                donor_json_values = donor_json["submit"]
                donor_values_split = donor_json_values.split('_')
                donorEmail = donor_values_split[0]
                donatingOrgan = donor_values_split[1]
                donorHospitalName = donor_values_split[2]
                hospitalID = dho.DonorHospitalID(donorHospitalName)
                donorHospital = hospitalID.getDonorHospitalID()
                if('submit' in donor_json):
                    newRequest = dro.NewDonationRequest(donorEmail, recipientEmail, donatingOrgan, donorHospital[0])
                    if (newRequest.createDonationRequest()):
                        print("Inserted successfully")
                        flash ("Request Sent")
                    else:
                        print("Error creating request")
                        flash ("Request Sending Error!")
        return render_template('receiverProfile.html', recipient_data=recipient_profile, organ_data=recipient_organ_data, donor_organ_data=donor_organ_list, pending_requests=pending_requests, approved_requests=approved_requests, rejected_requests=rejected_requests)