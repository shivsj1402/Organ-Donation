import mock
import organdonationwebapp.Hospital.Hospital as hospital
import organdonationwebapp.API.Logger as logger

hospital_json = {
    "hospital_name": "hospital",
    "email": "hospital1@test.com",
    "phone_number": "1234",
    "address": "hospital1 address",
    "province": "province",
    "city": "city",
    "password": "fakepass",
    "data": "certificate"
}


# @mock.patch.object(hospital.hc, 'hospitalRegistration')
# @mock.patch.object(hospital, 'url_for')
# @mock.patch.object(logger, 'MyLogger')
# def test_register(mock_logger, mock_url_for, mock_hospital_reg):
#     aHospital = hospital.Hospital()
#     aHospital.initialize(hospital_json)
#     aHospital.setLogger(mock_logger)
#     mock_url_for.return_value = "http://url"
#     mock_hospital_reg.return_value = True
#     assert aHospital.register() == (True, "http://url")


# @mock.patch.object(hospital.hc, 'hospitalRegistration')
# @mock.patch.object(logger, 'MyLogger')
# def test_register_failed(mock_logger, mock_hospital_reg):
#     aHospital = hospital.Hospital()
#     aHospital.initialize(hospital_json)
#     aHospital.setLogger(mock_logger)
#     mock_hospital_reg.return_value = False
#     print(aHospital.register())
    #assert aHospital.register() == (False, "Registration Failed.")


@mock.patch.object(hospital.hc, 'hospitalRegistration')
def test_register_exception(mock_hospital_reg):
    aHospital = hospital.Hospital()
    aHospital.initialize(hospital_json)
    mock_hospital_reg.side_effect = Exception("register exception")
    aHospital.register()


@mock.patch.object(logger, 'MyLogger')
def test_setlogger(mock_logger):
    aHospital = hospital.Hospital()
    aHospital.setLogger(mock_logger)


# def test_login():
#     aHospital = hospital.Hospital()
#     assert aHospital.login() == NotImplementedError


@mock.patch.object(logger, 'MyLogger')
def test_build_hospital(mock_logger):
    aHospital = hospital.Hospital()
    aHospital.initialize(hospital_json)
    aHospital.setLogger(logger)
    assert type(hospital.build_Hospital(hospital.Hospital, hospital_json, logger)).__name__ == type(aHospital).__name__