from organdonationwebapp import duc
from organdonationwebapp import app

from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature

app.config.from_pyfile('../config.cfg')

mail = Mail(app)

class UpdateRequestStatus(object):
    def __init__(self,request, requestID, userEmail):
        self.request = request
        self.requestID = requestID
        self.userEmail = userEmail


    def setRequestsStatus(self):
        try:
            requeststate = 0        # 0 for any new pending requests
            if(self.request == "AcceptDonor"):
                requeststate = 1    # 1 for requests accepted by Donors but pending at recipient's end for approval
            elif(self.request == "DeclineDonor"):
                requeststate = 2    # 2 for requests rejected by Donors
            elif(self.request == "AcceptRecipient"):
                requeststate = 3    # 3 for requests accepted by both Donor and Recipient
            elif(self.request == "DeclineRecipient"):
                requeststate = 4    # 4 for requests rejected by Donors
            if(duc.setRequestsStatus(self.requestID, requeststate)):
                return True
            else:
                return False
        except Exception as err:
            return False

    def sendEmail(self):
        try:
            if(self.request == "AcceptDonor"):
                msg = Message('Receiver Intimitatiion', sender= 'amcamcwinter@gmail.com', recipients=[self.userEmail])
                msg.body = 'Your request has been accepted by the Donor'
                mail.send(msg)
                return True
            elif(self.request == "DeclineDonor"):
                msg = Message('Receiver Intimitatiion', sender= 'amcamcwinter@gmail.com', recipients=[self.userEmail])
                msg.body = 'Your request has been denied by the Donor'
                mail.send(msg)
                return True
            elif(self.request == "AcceptRecipient"):
                msg = Message('Donor Intimitatiion', sender= 'amcamcwinter@gmail.com', recipients=[self.userEmail])
                msg.body = 'Your request has been accepted by the Receiver'
                mail.send(msg)
                return True
            elif(self.request == "DeclineRecipient"):
                msg = Message('Donor Intimitatiion', sender= 'amcamcwinter@gmail.com', recipients=[self.userEmail])
                msg.body = 'Your request has been denied by the Receiver'
                mail.send(msg)
                return True
        except Exception as err:
            return False
