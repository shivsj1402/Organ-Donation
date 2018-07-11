from flask import Flask, render_template, request, redirect, session, url_for, g, send_file
from organdonationwebapp import app, sc
from io import BytesIO
import mysql.connector

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/donorList', methods=['GET'])
def donorList():
    if g.user:
        if request.method == 'GET':
            dlist= sc.getDonorList()
            return render_template('donorList.html', dlist=dlist)
    return redirect(url_for('hospitalLogin'))

@app.route('/donorReceiverRequest', methods=['GET'])
def donorReceiverRequest():
    return render_template('donorReceiverRequest.html')

@app.route('/hospitalregistration', methods=['GET','POST'])
def hospitalRegistration():
    if request.method == 'POST':
        hospitalName = request.form['hospitalName']
        emailID = request.form['emailID']
        phone = request.form['phone']
        address = request.form['address']
        province = request.form['province']
        city = request.form['city']
        password = request.form['password']
        data = request.files['certificate']
        certificate=data.read()

        message = sc.hospitalRegistrattion(hospitalName,emailID,phone,address,province,city,password,certificate)
        if(message=="Done"):
            return redirect(url_for('hospitalLogin'))
        else:
            print("Error Inserting Data")  
    return render_template('hospitalregistration.html')

# @app.route('/download')
# def download():
#     hemail1="hospital1@gmail.com"
#     file_data=sc.getHospitalName(hemail1)
#     return print(file_data)

@app.route('/receiverList', methods=['GET'])
def receiverList():
    if g.user:
        if request.method == 'GET':
            rlist= sc.getReceiverList()
            return render_template('receiverList.html', rlist=rlist)
    return redirect(url_for('hospitalLogin'))

@app.route('/receiverProfile', methods=['GET'])
def receiverProfile():
    return render_template('receiverProfile.html')

@app.route('/requestFinal', methods=['GET'])
def requestFinal():
    return render_template('requestFinal.html')

@app.route('/signup', methods=['GET','POST'])
def registerUser():
    organ =[]
    hlist=sc.getHospitalList()
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        sex = request.form['sex']
        dob = request.form['dob']
        address = request.form['address']
        province = request.form['province']
        city = request.form['city']
        hospital = request.form['hname']
        bloodgroup = request.form['bloodgroup']
        usertype = request.form['usertype']
        organ = request.form.getlist('organ')
        for item in organ:
            message= sc.userRegistration(first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, item)
            if(message=="Done"):
                print("User Registered")
            else:
                print("Error Inserting Data")
    return render_template('signup.html', hlist=hlist)

@app.route('/hospitaldonor', methods=['GET'])
def hospitalDonorPage():
    return render_template('DonorReceiverRequest.html')

@app.route('/adminlogin', methods=['GET','POST'])
def adminLoginPage():
    if request.method == 'POST':
        hospitaldata = request.form
        email =hospitaldata['emailID']
        password =hospitaldata['password']
        user = sc.adminLoginAuthentication(email, password)
        if(user):
            return redirect(url_for('adminHomepage', username=user))
        else:
            return 'Authentication failed!!'
    return render_template('adminlogin.html')

@app.route('/adminhome/<username>', methods=['GET','POST'])
def adminHomepage(username=None):
    hospitallist = sc.getHospitalList()
    #print(hospitallist[6][7])
    #return send_file(BytesIO(hospitallist[6][7]), attachment_filename='certificate.pdf', as_attachment=True)
    if(hospitallist):
        return render_template('adminhome.html', list=hospitallist,username=username)
    return render_template('adminhome.html', username=username)

@app.route('/hospitalHome', methods=['GET','POST'])
def hospitalHome():
    if g.user:
        hemail=g.user
        print(hemail)
        hname=sc.getHospitalName(hemail)
        print(hname)
        if request.method == 'POST':
            if(request.form['submit']=='View Donor List'):
                return redirect(url_for('donorList'))
            elif(request.form['submit']=='View Receiver List'):
                return redirect(url_for('receiverList'))
        res2 = sc.getHospitalDonorList(hname[0])
        res3 = sc.getHospitalReceiverList(hname[0])
        return render_template('hospitalHome.html',donor=res2, receiver=res3)
    return redirect(url_for('hospitalLogin'))

@app.route('/loginPage', methods=['GET','POST'])
def hospitalLogin():
    if request.method == 'POST':
        hospitaldata = request.form
        email =hospitaldata['hemail']
        password =hospitaldata['hpassword']
        usertype = hospitaldata['type']
        session.pop('user', None)
        if(request.form['submit']=='submit'):
            res = sc.hospitalLoginAuthentication(email,password)
            if(res):
                session['user']= email
                return redirect(url_for('hospitalHome'))
            else:   
                return "Please register"
        elif(request.form['submit']=='SignUp'):
            if(usertype =="Donor/Receiver"):
                return redirect(url_for('registerUser'))
            else:
                return redirect(url_for('hospitalRegistration'))
    return render_template('loginPage.html')