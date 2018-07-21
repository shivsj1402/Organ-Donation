from organdonationwebapp.models.SqlClient import SqlClient

class UserModel(SqlClient):
    def __init__(self):
        super(UserModel,self).__init__()


    def userRegistration(self, user):
        try:
            for item in user.organ:
                self.cursor.callproc('userregistration',[user.first_name, user.last_name, user.phone_number, user.email, user.sex, user.dob, user.address, user.province, user.city, user.hospital, user.bloodgroup, user.usertype, user.item])
                self.connection.commit()
            return True
        except Exception as err:
            print(err)
            return False