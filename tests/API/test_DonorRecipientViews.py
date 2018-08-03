import mock
import organdonationwebapp.API.DonorRecipientViews as drview
from test_helpers import fakeViewCertificate, fakeHospitalList, fakeDeleteHospital, fakeValidateHospital, mock_request_form, fakeRegister, fakeOpenRequestDetails


@mock.patch.object(drview.hlo, 'HospitalList')
@mock.patch.object(drview.res, 'Register')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview, 'redirect')
@mock.patch.object(drview, 'url_for')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview, 'request')
def test_registerUser(mock_request, mock_g, mock_url_for,
                      mock_redirect, mock_flash, mock_reg, mock_hlo_li):
    mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
    drview.request.method = 'POST'
    mock_g.user = "user"
    drview.request.form = mock_request_form({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]})
    mock_reg.return_value = fakeRegister({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]}, "donor", True)
    mock_flash.return_value = "Registered Successfully"
    mock_url_for.return_value = "http://url"
    mock_redirect.return_value = "<h2>hospital home</h2"
    assert drview.registerUser("donor") == "<h2>hospital home</h2"


@mock.patch.object(drview.hlo, 'HospitalList')
@mock.patch.object(drview.res, 'Register')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview, 'redirect')
@mock.patch.object(drview, 'url_for')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview, 'request')
def test_registerUser_nouser(mock_request, mock_g, mock_url_for,
                      mock_redirect, mock_flash, mock_reg, mock_hlo_li):
    mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
    drview.request.method = 'POST'
    mock_g.user = None
    drview.request.form = mock_request_form({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]})
    mock_reg.return_value = fakeRegister({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]}, "donor", True)
    mock_flash.return_value = "Registered Successfully"
    mock_url_for.return_value = "http://url"
    mock_redirect.return_value = "<h2>login</h2"
    assert drview.registerUser("donor") == "<h2>login</h2"


@mock.patch.object(drview.hlo, 'HospitalList')
@mock.patch.object(drview.res, 'Register')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview, 'request')
@mock.patch.object(drview, 'g')
def test_registerUser_invalid(mock_g, mock_request, mock_flash, mock_reg, mock_hlo_li):
    mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
    drview.request.method = 'POST'
    drview.request.form = mock_request_form({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]})
    mock_reg.return_value = fakeRegister({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]}, "donor", False)
    mock_flash.return_value = "Registration error"
    assert drview.registerUser("donor") == "<h2> Registration failed </h2>"