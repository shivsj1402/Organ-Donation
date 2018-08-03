# import mock
# import organdonationwebapp.Hospital.DBValidatePassword as dbval



# @mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
# def test_validateCapitalLetters(mock_parsepassword):
#     mock_parsepassword.return_value = {"capital_letters": 2, "small_letter": 5}
#     dbvalpass = dbval.DBValidatePassword("Password1P")
#     assert dbvalpass.validateCapitalLetters() == True

# @mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
# def test_validateCapitalLetters_failed(mock_parsepassword):
#     mock_parsepassword.return_value = {"capital_letters": 4, "small_letter": 5}
#     dbvalpass = dbval.DBValidatePassword("Password1")
#     assert dbvalpass.validateCapitalLetters() == False