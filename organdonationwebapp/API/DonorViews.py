from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.User.Donor.DonorListDetails as dlo
import organdonationwebapp.User.Donor.ShowDonorProfile as dop
import organdonationwebapp.Hospital.HospitalHome as hho
import organdonationwebapp.Hospital.HospitalDonorList as hdl
import organdonationwebapp.User.Donor.ShowDonorRequestStatus as rso
import json


@app.route('/donorList', methods=['GET','POST'])
def donorList():
    print("g.user",(g.user))
    if g.user:
        hospitalEmail = g.user
        hospitalhome = hho.HospitalHome(hospitalEmail)
        hospital_name = hospitalhome.getHospitalName()
        donorlist = dlo.DonorListDetails(hospital_name[0])
        don_list_details = donorlist.getDonorsList(hospital_name[0])
        if(don_list_details):
            if request.method == 'POST':
                data= json.dumps(request.form.to_dict())
                data_json = json.loads(data)
                if('view' in data_json):
                    donorEmail = request.form["view"]
                    return redirect(url_for('donorProfilePage', hospitalEmail=hospitalEmail, donorEmail=donorEmail))
            return render_template('donorList.html', dlist=don_list_details)
    return redirect(url_for('Login'))


@app.route('/donorprofile/<hospitalEmail>/<donorEmail>', methods=['GET','POST'])
def donorProfilePage(hospitalEmail=None,donorEmail=None):
    donorprofile = dop.ShowDonorProfile(donorEmail)
    donor_userdata = donorprofile.getDonorProfile()
    donor_organ_data = donorprofile.getDonorOrgans()
    requestStatus = rso.ShowDonorRequestStatus(hospitalEmail,donorEmail)
    request_status_data = requestStatus.getRequestsStatus()
    approved_requests = request_status_data["approved"]
    pending_requests = request_status_data["pending"]
    # requestlist = rso.ShowDonorRequestStatus(hospitalEmail,donorEmail)
    # pending_requests = requestlist.getPendingRequestList()
    if(donor_userdata and donor_organ_data):
        if request.method == 'POST':
            data= json.dumps(request.form.to_dict())
            datajson = json.loads(data)
            if('requestID' in datajson):
                requestID = request.form['requestID']
                return redirect(url_for('donorHospitalRequestPage', requestID=requestID))
        return render_template('donorprofile.html', hospitalEmail=hospitalEmail, donorEmail=donorEmail, pending_requests=pending_requests, approved_requests=approved_requests, donordata=donor_userdata, organ_data=donor_organ_data)