from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.User.Recipient.RecipientListDetails as rlo


@app.route('/receiverList', methods=['GET'])
def receiverList():
    if g.user:
        recipientList = rlo.RecipientListDetails(g.user)
        rec_list_details = recipientList.getRecipientList()
        if(rec_list_details):
            return render_template('receiverList.html', rlist=rec_list_details)
    return redirect(url_for('hospitalLogin'))