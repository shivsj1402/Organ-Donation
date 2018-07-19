from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.Admin.Admin as ao
import organdonationwebapp.Admin.ValidateHospital as vho
import organdonationwebapp.Hospital.HospitalList as hlo
import json


@app.route('/adminlogin', methods=['GET','POST'])
def adminLoginPage():
    if request.method == 'POST':
        user = None
        admin_data = json.dumps(request.form.to_dict())
        admin_json = json.loads(admin_data)
        if(admin_json['submit']=='submit'):
            admin = ao.Admin(admin_json)
            session.pop('user', None)
            if(admin.loginAdmin()):
                session['user']= admin_json['emailID']
                user = session['user']
                return redirect(url_for('adminHomepage', username=user))
            else:
                return 'Authentication failed!!'
    return render_template('adminlogin.html')


@app.route('/adminhome/<username>', methods=['GET','POST'])
def adminHomepage(username=None, hospitalEmail=None):
    if request.method == 'POST':
        validate_hospital = json.dumps(request.form.to_dict())
        hospital_json = json.loads(validate_hospital)
        if(hospital_json != " "):
            validate = vho.ValidateHospital(hospital_json)
            hospitalEmail = validate.updateValidateHospitalFlag()
    hospitalList = hlo.HospitalList()
    hospital_list = hospitalList.getGlobalHospitalList()
    #print(hospitallist[6][7])
    #return send_file(BytesIO(hospitallist[6][7]), attachment_filename='certificate.pdf', as_attachment=True)
    if(hospital_list):
        return render_template('adminhome.html', list=hospital_list,username=username)
    return render_template('adminhome.html', username=username)