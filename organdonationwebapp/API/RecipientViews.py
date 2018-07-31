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
import json
import binascii


@app.route('/receiverList', methods=['GET', 'POST'])
def receiverList():
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
    return redirect(url_for('Login'))


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
    requestStatus = sro.ShowRecipientRequestStatus(recipientEmail)
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