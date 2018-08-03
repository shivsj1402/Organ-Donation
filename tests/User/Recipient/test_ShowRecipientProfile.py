import mock
import organdonationwebapp.User.Recipient.ShowRecipientProfile as showrecipientprofiletest

@mock.patch.object(showrecipientprofiletest.ruc, 'receiverHospitalShowProfile')
def test_getRecipientProfile_pass(mock_recipientProfile):
    mock_recipientProfile.return_value = [("firstone","firsttwo","emailone@gmail.com"),("secondone","secondtwo","emailtwo@gmail.com")]
    mock_recepient_object = showrecipientprofiletest.ShowRecipientProfile("test@gmail.com")
    assert mock_recepient_object.getRecipientProfile() == [("firstone","firsttwo","emailone@gmail.com"),("secondone","secondtwo","emailtwo@gmail.com")]

@mock.patch.object(showrecipientprofiletest.ruc, 'receiverHospitalShowProfile')
def test_getRecipientProfile_fail(mock_recipientProfile):
    mock_recipientProfile.return_value = None
    mock_recepient_object = showrecipientprofiletest.ShowRecipientProfile("test@gmail.com")
    assert mock_recepient_object.getRecipientProfile()  == None

@mock.patch.object(showrecipientprofiletest.ruc, 'receiverHospitalShowProfile')
def test_getRecipientProfile_execption(mock_recipientProfile):
    mock_recipientProfile.side_effect = Exception("recipientProfile exception")
    mock_recepient_object = showrecipientprofiletest.ShowRecipientProfile("")
    mock_recepient_object.getRecipientProfile()


@mock.patch.object(showrecipientprofiletest.ruc, 'getRecipientOrgans')
def test_getRecipientOrgans_pass(mock_recipientorgan):
    mock_recipientorgan.return_value = [("Liver",),("Heart",)]
    mock_recepient_object = showrecipientprofiletest.ShowRecipientProfile("abc@gmail.com")
    assert mock_recepient_object.getRecipientOrgans() == [("Liver",),("Heart",)]

@mock.patch.object(showrecipientprofiletest.ruc, 'getRecipientOrgans')
def test_getRecipientOrgans_fail(mock_recipientorgan):
    mock_recipientorgan.return_value = None
    mock_recepient_object = showrecipientprofiletest.ShowRecipientProfile("abc@gmail.com")
    assert mock_recepient_object.getRecipientOrgans()  == None

@mock.patch.object(showrecipientprofiletest.ruc, 'getRecipientOrgans')
def test_getRecipientOrgans_execption(mock_recipientorgan):
    mock_recipientorgan.side_effect = Exception("createReques exception")
    mock_recepient_object = showrecipientprofiletest.ShowRecipientProfile("")
    mock_recepient_object.getRecipientOrgans()