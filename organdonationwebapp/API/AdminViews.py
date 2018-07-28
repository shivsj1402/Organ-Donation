from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.Admin.Admin as ao
import organdonationwebapp.Admin.ValidateHospital as vho
import organdonationwebapp.Admin.DeleteHospital as dho
import organdonationwebapp.Hospital.HospitalList as hlo
import json
from io import BytesIO


@app.route('/adminhome/<username>', methods=['GET','POST'])
def adminHomepage(username=None, hospitalEmail=None):
    hospitalList = hlo.HospitalList()
    hospital_list = hospitalList.getGlobalHospitalList()
    if(hospital_list):
        if request.method == 'POST':
            validate_hospital = json.dumps(request.form.to_dict())
            hospital_json = json.loads(validate_hospital)
            print("hospital_json",hospital_json)
            if('viewcertificate' in hospital_json):
                validate = vho.ValidateHospital(hospital_json)
                hospitalEmail = validate.updateValidateHospitalFlag()
            if('delete' in hospital_json):
                hospitalID = request.form['delete']
                deleteHospital = dho.DeleteHospital(hospitalID)
                delete_hospital_status = deleteHospital.deleteHospital()
                if(delete_hospital_status):
                    return render_template('adminhome.html', list=hospital_list,username=username)
        return render_template('adminhome.html', list=hospital_list,username=username)
    return render_template('adminhome.html', username=username)


# @app.route('/adminhome/<username>', methods=['GET','POST'])
# def adminHomepage(username=None, hospitalEmail=None):
#     if request.method == 'POST':
#         validate_hospital = json.dumps(request.form.to_dict())
#         hospital_json = json.loads(validate_hospital)
#         if(hospital_json != " "):
#             validate = vho.ValidateHospital(hospital_json)
#             hospitalEmail = validate.updateValidateHospitalFlag()
#     hospitalList = hlo.HospitalList()
#     hospital_list = hospitalList.getGlobalHospitalList()
#     # print(hospital_list)
#     # return send_file(BytesIO(hospital_list[5][7]), attachment_filename='certificate.pdf', as_attachment=True)
#     if(hospital_list):
#         return render_template('adminhome.html', list=hospital_list,username=username)
#     return render_template('adminhome.html', username=username)