# import mock
# import organdonationwebapp.hospital.hospital as hospital
# import organdonationwebapp.API.Logger as logger

# hospital_json = {
#     "hospital_name": "hospital",
#     "email": "hospital1@test.com",
#     "phone_number": "1234",
#     "address": "hospital1 address",
#     "province": "province",
#     "city": "city",
#     "bloodgroup": "AB+",
#     "hospitaltype": "donor",
#     "organ": "liver"
#     "password": "fakepass"
# }

# @mock.patch.object(hospital.uc, 'hospitalRegistration')
# @mock.patch.object(hospital, 'url_for')
# @mock.patch.object(logger, 'MyLogger')
# def test_register(mock_logger, mock_url_for, mock_hospital_reg):
#     ahospital = hospital.hospital()
#     ahospital.initialize(hospital_json)
#     ahospital.setLogger(mock_logger)
#     mock_url_for.return_value = "http://url"
#     mock_hospital_reg.return_value = True
#     assert ahospital.register() == (True, "http://url")


# @mock.patch.object(hospital.uc, 'hospitalRegistration')
# @mock.patch.object(logger, 'MyLogger')
# def test_register_failed(mock_logger, mock_hospital_reg):
#     ahospital = hospital.hospital()
#     ahospital.initialize(hospital_json)
#     ahospital.setLogger(mock_logger)
#     mock_hospital_reg.return_value = False
#     assert ahospital.register() == (False, "Registration Failed.")

# @mock.patch.object(hospital.uc, 'hospitalRegistration')
# def test_register_exception(mock_hospital_reg):
#     ahospital = hospital.hospital()
#     ahospital.initialize(hospital_json)
#     mock_hospital_reg.side_effect = Exception("register exception")
#     ahospital.register()

# @mock.patch.object(logger, 'MyLogger')
# def test_setlogger(mock_logger):
#     ahospital = hospital.hospital()
#     ahospital.setLogger(mock_logger)

# def test_login():
#     ahospital = hospital.hospital()
#     assert ahospital.login() == NotImplementedError

# @mock.patch.object(logger, 'MyLogger')
# def test_build_hospital(mock_logger):
#     ahospital = hospital.hospital()
#     ahospital.initialize(hospital_json)
#     ahospital.setLogger(logger)
#     assert hospital.build_hospital(hospital.hospital, hospital_json, logger) == ahospital
