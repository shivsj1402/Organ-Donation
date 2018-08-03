import mock
import organdonationwebapp.API.AdminViews as adminviews

class fakeViewCertificate(object):
    def __init__(self, emailid, certificate):
        self.emailid = emailid
        self.certificate = certificate
    def getHospitalCerti(self):
        return self.certificate

class fakeDeleteHospital(object):
    def __init__(self, emailid, isdeleted):
        self.emailid = emailid
        self.isdeleted = isdeleted
    def deleteHospital(self):
        return self.isdeleted

class fakeValidateHospital(object):
    def __init__(self, body,logger, isvalidated):
        self.body = body
        self.logger = logger
        self.isvalidated = isvalidated
    def updateValidateHospitalFlag(self):
        return self.isvalidated

class fakeHospitalList(object):
    def __init__(self, body):
        self.body = body
    def getGlobalHospitalList(self):
        return self.body

class mock_request_form(object):
    def __init__(self, body):
        self.body = body
    def to_dict(self):
        return self.body

@mock.patch.object(adminviews.hlo, 'HospitalList')
@mock.patch.object(adminviews, 'render_template')
@mock.patch.object(adminviews, 'g')
@mock.patch.object(adminviews.vho, 'ValidateHospital')
@mock.patch.object(adminviews, 'request')
def test_adminHomePage_validate(mock_fl_re, mock_vho_validate, mock_g, mock_fl_ren, mock_hlo_li):
    mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
    adminviews.request.method = 'POST'
    adminviews.request.form = mock_request_form({"hospital": "hospital1", "validate": "true"})
    #mock_flash.return_value = "Hospital validated"
    mock_vho_validate.return_value = fakeValidateHospital({"hospital": "hospital1", "validate": "true"},"g","True")
    mock_fl_ren.return_value = "<h2>admin page</h2>"
    assert adminviews.adminHomepage() == "<h2>admin page</h2>"

def test_adminHomePage_validate_failed():
    pass

@mock.patch.object(adminviews.hlo, 'HospitalList')
@mock.patch.object(adminviews, 'render_template')
@mock.patch.object(adminviews, 'flash')
@mock.patch.object(adminviews, 'g')
@mock.patch.object(adminviews.dho, 'DeleteHospital')
@mock.patch.object(adminviews, 'request')
def test_adminHomePage_delete(mock_fl_re, mock_dho_delete, mock_g, mock_flash, mock_fl_ren, mock_hlo_li):
    mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
    adminviews.request.method = 'POST'
    adminviews.request.form = mock_request_form({"hospital": "hospital1", "delete": "hospital1"})
    mock_flash.return_value = "deleted successfully"
    mock_dho_delete.return_value = fakeDeleteHospital({"hospital": "hospital1", "delete": "hospital1"},"True")
    mock_fl_ren.return_value = "<h2>admin page</h2>"
    assert adminviews.adminHomepage() == "<h2>admin page</h2>"

def test_adminHomePage_delete_failed():
    pass

@mock.patch.object(adminviews.hlo, 'HospitalList')
@mock.patch.object(adminviews, 'render_template')
@mock.patch.object(adminviews, 'send_file')
@mock.patch.object(adminviews, 'BytesIO')
@mock.patch.object(adminviews, 'g')
@mock.patch.object(adminviews.vc, 'ViewCertificate')
@mock.patch.object(adminviews, 'request')
def test_adminHomePage_certificate(mock_fl_re, mock_vc_certi, mock_g, mock_bytesio, mock_send_file, mock_fl_ren, mock_hlo_li):
   mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
   adminviews.request.method = 'POST'
   adminviews.request.form = mock_request_form({"hospital": "hospital1", "certificate": "hospital1@test.com"})
   mock_send_file.return_value = "sent successfully"
   mock_bytesio.return_value = str.encode("sent successfully")
   mock_vc_certi.return_value = fakeViewCertificate("hospital1@test.com", [["certificate"]])
   assert adminviews.adminHomepage() == "sent successfully"


@mock.patch.object(adminviews.hlo, 'HospitalList')
@mock.patch.object(adminviews, 'render_template')
@mock.patch.object(adminviews.vc, 'ViewCertificate')
@mock.patch.object(adminviews, 'g')
@mock.patch.object(adminviews, 'request')
def test_adminHomePage_certificate_failed(mock_fl_re, mock_g, mock_vc_certi, mock_fl_ren, mock_hlo_li):
   mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
   adminviews.request.method = 'POST'
   adminviews.request.form = mock_request_form({"hospital": "hospital1", "certificate": None})
   mock_vc_certi.return_value = fakeViewCertificate("hospital1@test.com", None)
   mock_fl_ren.return_value = "<h2>admin page</h2>"
   assert adminviews.adminHomepage() == "<h2>admin page</h2>"


def test_adminHomePage_nooption():
    pass


def test_adminHomePage_get():
    pass

def test_adminHomePage_nohospitallist():
    pass
