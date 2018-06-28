# Get flask
from flask import Flask

# Create the app
app = Flask(__name__)
app.debug=True

import organdonationwebapp.views