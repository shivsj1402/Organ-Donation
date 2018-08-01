from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.User.Recipient.RecipientListDetails as rlo
import organdonationwebapp.User.Recipient.ShowRecipientProfile as rpo
import organdonationwebapp.User.Donor.ShowRecommendedDonors as dpo
import organdonationwebapp.User.Recipient.ShowRecipientRequestStatus as sro
import organdonationwebapp.User.UpdateMedicalReports as rro
import organdonationwebapp.Hospital.HospitalHome as hho
import organdonationwebapp.Hospital.DonorHospitalID as dho
import organdonationwebapp.User.Recipient.NewDonationRequest as dro
import organdonationwebapp.User.OpenRequestDetails as rdo
import organdonationwebapp.User.Donor.Donor as do
import organdonationwebapp.User.Recipient.Recipient as ro
import organdonationwebapp.User.Donor.UpdateRequestStatus as uro
#import organdonationwebapp.User.Recipient.CheckRecommendedDonor as cdo
import json
import binascii


@app.route('/receiverList', methods=['GET', 'POST'])
def receiverList():
    print("g.user",(g.user))
    if g.user:
        hospitalhome = hho.HospitalHome(g.user)
        hospital_name = hospitalhome.getHospitalName()
        recipientlist = rlo.RecipientListDetails(hospital_name[0])
        rec_list_details = recipientlist.getRecipientsList(hospital_name[0])
        if(rec_list_details):
            if request.method == 'POST':
                recipientEmail = request.form['view']
                return redirect(url_for('receiverHospitalRequestPage',recipientEmail=recipientEmail))
            return render_template('receiverList.html', rlist=rec_list_details)
        return render_template('receiverList.html')
    return redirect(url_for('Login'))


@app.route('/receiverhospitalrequest/<recipientEmail>', methods=['GET','POST'])
def receiverHospitalRequestPage(recipientEmail=None):
    recipient_data = rpo.ShowRecipientProfile(recipientEmail)
    recipient_profile = recipient_data.getRecipientProfile()
    recipientEmail = recipient_profile[0][2] # Extracting recipient email from Recipient profile JSON
    recipient_organ_data = recipient_data.getRecipientOrgans()
    donor_organ_list = []
    only_organ_list = []
    for organ in recipient_organ_data:
        donor_list = dpo.ShowRecommendedDonors(organ[0])
        donor_organ_list.extend(donor_list.getrecommendedDonorList())
    # for item in donor_organ_list:
    #     only_organ_list.append(item[1])
    # print("only_organ_list",(only_organ_list))
    # checkDonor = cdo.CheckRecommendedDonor(recipientEmail, only_organ_list)
    # request_status_data = checkDonor.getRequestsStatus()
    requestStatus = sro.ShowRecipientRequestStatus(recipientEmail)
    request_status_data = requestStatus.getRequestsStatus()
    approved_requests = request_status_data["approved"]
    rejected_requests = request_status_data["rejected"]
    pending_requests = request_status_data["pending"]
    if(recipient_profile and recipient_organ_data):
        if request.method == 'POST':
            donor_data= json.dumps(request.form.to_dict())
            donor_json = json.loads(donor_data)
            if('upload' in donor_json):
                if('reports' in donor_json):
                    flash("Please insert a valid certificates")
                else:
                    data = request.files['reports']
                    breport=data.read()
                    report =binascii.hexlify(breport)
                    userType= "r"
                    recipientReport= umr.UpdateMedicalReports(recipientEmail, report, userType)
                    recipient_report_status = recipientReport.updateReports()
                    if(recipient_report_status):
                        flash("Updated Successfully")
                    else:
                        flash("Insertion Error!")
            if('create request' in donor_json):
                donor_json_values = donor_json['create request']
                donor_values_split = donor_json_values.split('_')
                donorEmail = donor_values_split[0]
                donatingOrgan = donor_values_split[1]
                donorHospitalName = donor_values_split[2]
                hospitalID = dho.DonorHospitalID(donorHospitalName)
                donorHospital = hospitalID.getDonorHospitalID()
                newRequest = dro.NewDonationRequest(donorEmail, recipientEmail, donatingOrgan, donorHospital[0])
                if (newRequest.createDonationRequest()):
                    print("Request data inserted successfully")
                    flash ("Request Sent Successfully!!")
                    return render_template('receiverProfile.html', recipient_data=recipient_profile, organ_data=recipient_organ_data, donor_organ_data=donor_organ_list, pending_requests=pending_requests, approved_requests=approved_requests, rejected_requests=rejected_requests)
                else:
                    print("Error creating request")
                    flash ("Error Sending Request!!")
            if('view request' in donor_json):
                requestID = request.form['view request']
                return redirect(url_for('recipientShowApprovedRequest', requestID=requestID))
        return render_template('receiverProfile.html', recipient_data=recipient_profile, organ_data=recipient_organ_data, donor_organ_data=donor_organ_list, pending_requests=pending_requests, approved_requests=approved_requests, rejected_requests=rejected_requests)


@app.route('/recipientapprovedrequest/<requestID>', methods=['GET','POST'])
def recipientShowApprovedRequest(requestID=None):
    donor_userdata = None
    recipient_userdata = None
    requestdata =rdo.OpenRequestDetails(requestID)
    request_userdata = requestdata.getOpenRequestData()
    donorEmail=request_userdata[0][0]
    recipientEmail=request_userdata[0][1]
    organ=request_userdata[0][2]
    requestState=request_userdata[0][3]
    if(donorEmail):
        donor = do.Donor(donorEmail)
        donor_userdata = donor.donorHospitalRequestPage()
    if(recipientEmail):
        recipient = ro.Recipient(recipientEmail)
        recipient_userdata = recipient.donorHospitalPageRecipientList()
    if(recipient_userdata and donor_userdata):
        if request.method == 'POST':
            request_data= json.dumps(request.form.to_dict())
            request_json = json.loads(request_data)
            if('submit' in request_json):
                updateRequestStatus = uro.UpdateRequestStatus(request.form['submit'], requestID)
                request_status = updateRequestStatus.setRequestsStatus()
                if(request_status):
                    flash("Request Status updated successfully")
                    return redirect(url_for('receiverHospitalRequestPage',recipientEmail=recipientEmail))
                else:
                    flash("Error updating request status. Please try again later!")
        return render_template('RecipientShowRequestStatus.html', recipientdata=recipient_userdata, donordata=donor_userdata, organ=organ, requestState=requestState)
    else:
        flash("No donor/reciever available for this Request!")
        return render_template('RecipientShowRequestStatus.html', recipientdata=recipient_userdata, donordata=donor_userdata, organ=organ)