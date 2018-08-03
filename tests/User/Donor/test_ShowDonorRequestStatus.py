import mock
import logging
import organdonationwebapp.User.Donor.ShowDonorRequestStatus as donorstatus

@mock.patch.object(donorstatus.duc, 'getOpenRequestsStatus')
def test_ShowDonorRequestStatus_pass(mock_donorstatus):
    mock_donorstatus.return_value = {"approved": [], "pending": [()]}
    donorobj = donorstatus.ShowDonorRequestStatus("iwk@gmail.com","hemant2712@gmail.com",logging.getLogger())
    assert donorobj.getRequestsStatus() =={"approved": [], "pending": []}

# @mock.patch.object(donorstatus.duc, 'donorHospitalShowDonorProfile')
# def test_ShowDonorRequestStatus_fail(mock_donormail):
#     mock_donormail.return_value = None
#     donorobj = donor.Donor("abc@gmail.com")
#     assert donorobj.donorHospitalRequestPage()  == None

@mock.patch.object(donorstatus.duc, 'getOpenRequestsStatus')
def test_ShowDonorRequestStatus_execption(mock_donorstatus):
    mock_donorstatus.side_effect = Exception("createRequest exception")
    donorobj = donorstatus.ShowDonorRequestStatus("","",logging.getLogger())
    donorobj.getRequestsStatus()
