from organdonationwebapp.models.SqlClient import SqlClient

class UserModel(SqlClient):
    def __init__(self):
        super(UserModel,self).__init__()


    def userRegistration(self, first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, organ):
        try:
            for item in organ:
                self.cursor.callproc('userregistration',[first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, item])
                self.connection.commit()
            return True
        except Exception as err:
            print(err)
            return False