import mock
import organdonationwebapp.Hospital.HospitalDonorList as hdl


@mock.patch.object(hdl.hc, 'getHospitalDonorList')
def test_getDonorList(mock_hos_donorlist):
    mock_hos_donorlist.return_value = ["Pratik", "Shiv"]
    donList = hdl.HospitalDonorList("IWK","logger")
    assert donList.getDonorList() == ["Pratik", "Shiv"]


@mock.patch.object(hdl.hc, 'getHospitalDonorList')
def test_getDonorList_nodata(mock_hos_donorlist):
    mock_hos_donorlist.return_value = None
    donList = hdl.HospitalDonorList("IWK","logger")
    assert donList.getDonorList() == None


@mock.patch.object(hdl.hc, 'getHospitalDonorList')
def test_getDonorList_exception(mock_hos_donorlist):
    donorList = hdl.HospitalDonorList("","")
    mock_hos_donorlist.side_effect = Exception("register exception")
    donorList.getDonorList()