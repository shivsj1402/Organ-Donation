# Get flask
from flask import Flask

# Create the app
app = Flask(__name__)
app.debug=True

from organdonationwebapp.models.sqlclient import SqlClient
sc = None
if not sc:
	sc = SqlClient()

app.secret_key = 'lfjsdlkfjdklsjfkl'
app.config['SESSION'] = True
import organdonationwebapp.views