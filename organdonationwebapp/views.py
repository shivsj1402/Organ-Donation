from flask import Flask, render_template
from organdonationwebapp import app

@app.route('/helloworld', methods=['GET'])
def takeToHelloWorld():
    return "<p>hello world whats up? hello</p>"

@app.route('/adminLogin', methods=['GET'])
def adminPortalLogin():
    return render_template('adminLogin.html')

@app.route('/adminHome', methods=['GET'])
def adminPortalHome():
    return render_template('adminHome.html')

@app.route('/donorList', methods=['GET'])
def donorList():
    return render_template('donorList.html')

@app.route('/donorReceiverRequest', methods=['GET'])
def donorReceiverRequest():
    return render_template('donorReceiverRequest.html')

@app.route('/hospitalHome', methods=['GET'])
def hospitalHome():
    return render_template('hospitalHome.html')

@app.route('/hospitalLogin', methods=['GET'])
def hospitalLogin():
    return render_template('hospitalLogin.html')

@app.route('/hospitalRegestration', methods=['GET'])
def hospitalRegestration():
    return render_template('hospitalRegestration.html')

@app.route('/loginPage', methods=['GET'])
def loginPage():
    return render_template('loginPage.html')

@app.route('/receiverList', methods=['GET'])
def receiverList():
    return render_template('receiverList.html')

@app.route('/receiverProfile', methods=['GET'])
def receiverProfile():
    return render_template('receiverProfile.html')

@app.route('/requestFinal', methods=['GET'])
def requestFinal():
    return render_template('requestFinal.html')

@app.route('/signUp', methods=['GET'])
def signUp():
    return render_template('signUp.html')