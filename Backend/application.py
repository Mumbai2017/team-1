from flask import Flask
from database_setup import Pics LessonPlan, User, Videos, Tag, Comment,DBSession 
application = Flask(__name__)

@application.route("/login", methods = ["GET", "POST"])
def login():
	try:
		if request.method == "POST":
			session = DBSession()
			username = request.form["username"]
			password = reques.form["password"]
			print username
			print password
		else:
			return render_template("login.html")
	except Exception as e:
		print e

@application.route("/signup", method = ["POST, GET"])
def signup():
	try:
		if request.method == "POST":
			session = DBSession()
			email = request.form["email"]
			name = request.form["name"]
			password = request.form["password"]
			location = request.form["location"]
			unit_preferred = request.form["unit"]
			phone_number = request.form["phone"]
		else:
			return render_template("signup.html")
	except Exception as e:
		raise e 