from organdonationwebapp.models.SqlClient import SqlClient

class UserModel(SqlClient):
    def __init__(self):
        super(UserModel,self).__init__()


    def userRegistration(self, first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, organ):
        query = """INSERT INTO user(userFirstName,userLastName,phone,emailID,sex,dob,address,province,city,hospital,bloodGroup,donationType,organ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        for item in organ:
            try:
                self.cursor.execute(query,(first_name, last_name, phone_number, email, sex, dob, address, province, city, hospital, bloodgroup, usertype, item))
                self.connection.commit()
                return True
            except Exception as err:
                return False