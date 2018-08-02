import mock
import organdonationwebapp.User.UpdateMedicalReports as umr

@mock.patch.object(umr.uc, 'updateReport')
def test_updateReports(mock_user_updatereport):
    mock_user_updatereport.return_value = True
    userReports = umr.UpdateMedicalReports("user1@test.com", "reports", "donor")
    assert userReports.updateReports() == True

@mock.patch.object(umr.uc, 'updateReport')
def test_updateReports_failed(mock_user_updatereport):
    mock_user_updatereport.return_value = False
    userReports = umr.UpdateMedicalReports("user1@test.com", "reports", "donor")
    assert userReports.updateReports() == False
