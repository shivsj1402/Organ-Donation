from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.Admin.Admin as ao
import organdonationwebapp.Admin.ValidateHospital as vho
import organdonationwebapp.Admin.DeleteHospital as dho
import organdonationwebapp.Hospital.HospitalList as hlo
import organdonationwebapp.Admin.ViewCertificate as vc
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
            if('validate' in hospital_json):
                validate = vho.ValidateHospital(hospital_json)
                hospitalEmail = validate.updateValidateHospitalFlag()
                flash("Hospital validated")
                return render_template('adminhome.html', list=hospital_list,username=username)
            if('delete' in hospital_json):
                hospitalID = request.form['delete']
                deleteHospital = dho.DeleteHospital(hospitalID)
                delete_hospital_status = deleteHospital.deleteHospital()
                if(delete_hospital_status):
                    flash("deleted successfully")
                    return render_template('adminhome.html', list=hospital_list,username=username)
            if('certificate' in hospital_json):
                hospitalEmail = hospital_json['certificate'] if 'certificate' in hospital_json else None
                certificate = vc.ViewCertificate(hospitalEmail)
                hospitalcertificate = certificate.getHospitalCerti()
                if(hospitalcertificate):
                    print(hospitalcertificate[0][0])
                    return send_file(BytesIO(hospitalcertificate[0][0]), attachment_filename='certificate.pdf')
        return render_template('adminhome.html', list=hospital_list,username=username)
    return render_template('adminhome.html', username=username)