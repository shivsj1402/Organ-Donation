# Get flask
from flask import Flask

# Create the app
app = Flask(__name__)
app.debug=True


from organdonationwebapp.models.sqlclient import SqlClient
sc = None
if not sc:
    sc = SqlClient()


from organdonationwebapp.Admin.models import AdminModel
ac = None
if not ac:
    ac = AdminModel()


from organdonationwebapp.Hospital.models import HospitalModel
hc = None
if not hc:
    hc = HospitalModel()


from organdonationwebapp.User.models import UserModel
uc = None
if not uc:
    uc = UserModel()


from organdonationwebapp.User.Donor.models import DonorModel
duc = None
if not duc:
    duc = DonorModel()


from organdonationwebapp.User.Recipient.models import RecipientModel
ruc = None
if not ruc:
    ruc = RecipientModel()


app.secret_key = 'lfjsdlkfjdklsjfkl'
app.config['SESSION'] = True
import organdonationwebapp.API.views
# import organdonationwebapp.Hospital.hospital as ho