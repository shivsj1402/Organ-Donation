import mock
import organdonationwebapp.User.Recipient.RecipientListDetails as newrecipientlistdetails

@mock.patch.object(newrecipientlistdetails.ruc, 'getRecepientList')
def test_getRecipientsList_pass(mock_recepientlist):
    mock_recepientlist.return_value = [("firstone","firsttwo","emailone@gmail.com"),("secondone","secondtwo","emailtwo@gmail.com")]
    mock_recepient_object = newrecipientlistdetails.RecipientListDetails("test@gmail.com")
    assert mock_recepient_object.getRecipientsList("Test Hospital") == [("firstone","firsttwo","emailone@gmail.com"),("secondone","secondtwo","emailtwo@gmail.com")]

@mock.patch.object(newrecipientlistdetails.ruc, 'getRecepientList')
def test_getRecipientsList_fail(mock_recepientlist):
    mock_recepientlist.return_value = None
    mock_recepient_object = newrecipientlistdetails.RecipientListDetails("test@gmail.com")
    assert mock_recepient_object.getRecipientsList("Test Hospital") == None

@mock.patch.object(newrecipientlistdetails.ruc, 'getRecepientList')
def test_getReceiverList_execption(mock_recepientlist):
    mock_recepientlist.side_effect = Exception("createRequest exception")
    mock_recepient_object = newrecipientlistdetails.RecipientListDetails("")
    mock_recepient_object.getRecipientsList("")