from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.User.Donor.DonorListDetails as dlo
import organdonationwebapp.User.Donor.DonorProfile as dop
import organdonationwebapp.Hospital.HospitalHome as hho
import organdonationwebapp.Hospital.HospitalDonorList as hdl


@app.route('/donorList', methods=['GET'])
def donorList():
    if g.user:
        hospitalhome = hho.HospitalHome(g.user)
        hospital_name = hospitalhome.getHospitalName()
        donorlist = dlo.DonorListDetails(hospital_name[0])
        don_list_details = donorlist.getDonorsList(hospital_name[0])
        if(don_list_details):
            return render_template('donorList.html', dlist=don_list_details)
    return redirect(url_for('Login'))


@app.route('/donorprofile/<donorEmail>', methods=['GET'])
def donorProfilePage(donorEmail=None):
    donor_userdata = None
    if(donorEmail):
        donorprofile = dop.DonorProfile(donorEmail)
        donor_userdata = donorprofile.getDonorProfile()
        print("donor_userdata",(donor_userdata))
    if(donor_userdata):
        return render_template('donorprofile.html', donordata=donor_userdata)