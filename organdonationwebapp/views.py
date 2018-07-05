from flask import Flask, render_template
from organdonationwebapp import app


@app.route('/admin', methods=['GET'])
def welcomeToAdminPortal():
    return render_template('adminlogin.html')

@app.route('/hospital', methods=['GET'])
def takeToHospital():
    return render_template('hospitallogin.html')

@app.route('/helloworld', methods=['GET'])
def takeToHelloWorld():
    return "<p>hello world test</p>"

@app.route('/login', methods=['GET'])
def takeToAdmin():
    return render_template('loginpage.html')

@app.route('/signup', methods=['GET'])
def registerHospital():
    return render_template('signup.html')