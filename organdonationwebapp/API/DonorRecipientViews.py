from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.User.User as us
import organdonationwebapp.Hospital.HospitalList as hlo
import organdonationwebapp.User.Donor.Donor as do
import organdonationwebapp.User.Recipient.Recipient as ro
import organdonationwebapp.User.Donor.ShowRecommendedDonors as dpo
import organdonationwebapp.User.Recipient.ShowRecipientProfile as rpo
import json


@app.route('/signup', methods=['GET','POST'])
def registerUser():
    organ =[]
    hospitalList = hlo.HospitalList()
    hospital_list = hospitalList.getGlobalHospitalList()
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
    return render_template('signup.html', hlist=hospital_list)


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



@app.route('/receiverhospitalrequest/<recipientEmail>', methods=['GET','POST'])
def receiverHospitalRequestPage(recipientEmail=None):
    print("RecEmail:",(recipientEmail))
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