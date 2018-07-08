# Get flask
from flask import Flask

# Create the app
app = Flask(__name__)
app.debug=True
app.secret_key = 'lfjsdlkfjdklsjfkl'
app.config['SESSION'] = True

import organdonationwebapp.views