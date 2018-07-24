from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.User.Recipient.RecipientListDetails as rlo
import organdonationwebapp.Hospital.HospitalHome as hho


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