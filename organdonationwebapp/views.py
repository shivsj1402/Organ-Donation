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
    return "<p>hello world</p>"