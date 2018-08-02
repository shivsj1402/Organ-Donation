import mock
import organdonationwebapp.User.OpenRequestDetails as ored

@mock.patch.object(ored.uc, 'organRequest')
def test_getOpenRequestData(mock_user_organreq):
    mock_user_organreq.return_value = ["organ1", "organ2"]
    openReq = ored.OpenRequestDetails("request1")
    assert openReq.getOpenRequestData() == ["organ1", "organ2"]

@mock.patch.object(ored.uc, 'organRequest')
def test_getOpenRequestData_nodata(mock_user_organreq):
    mock_user_organreq.return_value = None
    openReq = ored.OpenRequestDetails("request1")
    assert openReq.getOpenRequestData() == None