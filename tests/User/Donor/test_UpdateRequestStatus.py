import mock
import logging
import organdonationwebapp.User.Donor.UpdateRequestStatus as updatestatus

# @mock.patch.object(updatestatus.duc,'sendEmail')
# def test_sendEmailAcceptDonor_pass(mock_updatestatus):
#     mock_updatestatus.return_value = True
#     donorobj = updatestatus.UpdateRequestStatus("AcceptDonor","5","hemant2712@gmail.com",logging.getLogger())
#     assert donorobj.sendEmail() ==True

# def test_sendEmailAcceptDonor_pass(mock_updatestatus):
#     mock_updatestatus.return_value = True
#     donorobj = updatestatus.UpdateRequestStatus("AcceptDonor","5","hemant2712@gmail.com",logging.getLogger())
#     assert donorobj.sendEmail() ==True

# def test_sendEmailAcceptDonor_pass(mock_updatestatus):
#     mock_updatestatus.return_value = True
#     donorobj = updatestatus.UpdateRequestStatus("AcceptDonor","5","hemant2712@gmail.com",logging.getLogger())
#     assert donorobj.sendEmail() ==True

# def test_sendEmailAcceptDonor_pass(mock_updatestatus):
#     mock_updatestatus.return_value = True
#     donorobj = updatestatus.UpdateRequestStatus("AcceptDonor","5","hemant2712@gmail.com",logging.getLogger())
#     assert donorobj.sendEmail() ==True

# @mock.patch.object(updatestatus.duc,'Message')
# def test_sendEmail_execption(mock_updatestatus):
#     mock_updatestatus.side_effect = Exception("createRequest exception")
#     donorobj = updatestatus.UpdateRequestStatus("","","",logging.getLogger())
#     donorobj.sendEmail()