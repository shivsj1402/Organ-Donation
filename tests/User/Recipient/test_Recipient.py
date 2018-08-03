import mock
import organdonationwebapp.User.Recipient.Recipient as recipient
import organdonationwebapp.API.Logger as logger

@mock.patch.object(logger, 'MyLogger')
@mock.patch.object(recipient.ruc, 'donorHospitalShowReceiverProfile')
def test_donorHospitalPageRecipientList(mock_recipientmail, mock_logger):
    mock_recipientmail.return_value = [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]
    recipientobj = recipient.Recipient("abc@gmail.com",logger)
    assert recipientobj.donorHospitalPageRecipientList() == [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]

@mock.patch.object(logger, 'MyLogger')
@mock.patch.object(recipient.ruc, 'donorHospitalShowReceiverProfile')
def test_donorHospitalPageRecipientList_nodata(mock_recipientmail, mock_logger):
    mock_recipientmail.return_value = None
    recipientobj = recipient.Recipient("someuser@gmail.com", logger)
    assert recipientobj.donorHospitalPageRecipientList() == None

@mock.patch.object(logger, 'MyLogger')
@mock.patch.object(recipient.ruc, 'donorHospitalShowReceiverProfile')
def test_donorHospitalPageRecipientList_exception(mock_recipientmail, mock_logger):
    mock_recipientmail.side_effect = Exception("createRequest exception")
    recipientobj = recipient.Recipient("", "")
    recipientobj.donorHospitalPageRecipientList()