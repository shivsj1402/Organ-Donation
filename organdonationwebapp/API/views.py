from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app, sc
from io import BytesIO
import mysql.connector
import json


@app.route('/donorReceiverRequest', methods=['GET'])
def donorReceiverRequest():
    return render_template('donorReceiverRequest.html')


@app.route('/receiverProfile', methods=['GET'])
def receiverProfile():
    return render_template('receiverProfile.html')


@app.route('/requestFinal', methods=['GET'])
def requestFinal():
    return render_template('requestFinal.html')


@app.route('/hospitaldonor', methods=['GET'])
def hospitalDonorPage():
    return render_template('DonorReceiverRequest.html')


@app.route('/dummyrequest', methods=['GET', 'POST'])
def dummyRequest():
    if request.method == 'POST':
        requestdata = request.form
        requestID = requestdata['requestID']
        requestdata = sc.organRequest(requestID)
        if(requestdata):
            return redirect(url_for('donorHospitalRequestPage', donorEmail=requestdata[0][0],recipientEmail=requestdata[0][1],organ=requestdata[0][2]))
    return render_template('dummyrequests.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('PageNotFound.html'), 404