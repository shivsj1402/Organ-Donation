#Load up the app
from organdonationwebapp import app

from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb




mysql = MySQL()

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'CSCI5308_16_DEVINT_USER'
app.config['MYSQL_DATABASE_PASSWORD'] = 'CSCI5308_16_DEVINT_16175'
app.config['MYSQL_DATABASE_DB'] = 'CSCI5308_16_DEVINT'
app.config['MYSQL_DATABASE_HOST'] = 'db-5308.cs.dal.ca'
app.config['port'] = '3306'
mysql.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/AdminHome")
def AdminHome():
    return render_template("AdminHome.html")

@app.route("/Adminlogin.html")
def AdminLogin():
    return render_template("Adminlogin.html")

@app.route("/DonorList.html")
def DonorList():
    return render_template("DonorList.html")

@app.route("/HospitalHome.html")
def HospitalHome():
    return render_template("HospitalHome.html")


@app.route("/HospitalLogin.html")
def HospitalLogin():
    return render_template("HospitalLogin.html")

@app.route("/Loginpage.html")
def Loginpage():
    return render_template("Loginpage.html")



@app.route("/Signin.html", methods=['GET','POST'])
def Signin():
    if request.method == 'GET':
        try:
        	emailID = request.form['emailID']
        	password = request.form['password']
            # Open database connection
            db = MySQLdb.connect("localhost","CSCI5308_16_DEVINT_USER","CSCI5308_16_DEVINT_16175","CSCI5308_16_DEVINT")

			# prepare a cursor object using cursor() method
			cursor = db.cursor()

			# Select Query Example :- Selecting data from the table.
			sql = "SELECT * FROM user WHERE emailID = 'emailID' AND password = 'password'"
			try:
				# Execute the SQL command
				cursor.execute(sql)
				# Fetch all the rows in a list of lists.
				results = cursor.fetchall()
				for row in results:
					userFirstName = row[0]
					userLastName = row[1]
					# Now print fetched result
					print ("userFirstName=%s,userLastName=%s" % (userFirstName, userLastName))
					print ("New userFirstName=,userLastName=" % (userFirstName, userLastName))
			except:
				print (“Value Fetch properly”)


@app.route("/DonorReceiverRequest.html", methods=['GET','POST'])
def DonorReceiverRequest():
    if request.method == 'GET':
        try:
        	emailID = request.form['emailID']
        	password = request.form['password']
            # Open database connection
            db = MySQLdb.connect("db-5308.cs.dal.ca","CSCI5308_16_DEVINT_USER","CSCI5308_16_DEVINT_16175","CSCI5308_16_DEVINT")

			# prepare a cursor object using cursor() method
			cursor = db.cursor()

			# Select Query Example :- Selecting data from the table.
			sql = "SELECT * FROM user WHERE emailID = %s"
			try:
				# Execute the SQL command
				cursor.execute(sql)
				# Fetch all the rows in a list of lists.
				results = cursor.fetchall()
				for row in results:
					userFirstName = row[0]
					# Now print fetched result
					print ("emailID=%s" % (emailID))
					print ("New password=" % (password))
			except:
				print (“Value Fetch properly”)


# Launching server
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=False)
