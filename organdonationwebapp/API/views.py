from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('PageNotFound.html'), 404