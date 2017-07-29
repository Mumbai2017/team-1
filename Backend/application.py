from flask import Flask, render_template, request, url_for
from database_setup import Pics, LessonPlan, User, Videos, Tag, Comment,DBSession 

application = Flask(__name__)

@application.route("/", methods = ["GET", "POST"])
@application.route("/login", methods = ["GET", "POST"])
def login():
	try:
		if request.method == "POST":
			session = DBSession()
			username = request.form["username"]
			password_value = request.form["password"]
			user = session.query(User).filter_by(email = username, password = password_value).first()
			if user is not None:
				print username
				print password_value
		else:
			return render_template("login.html")
	except Exception as e:
		print e

@application.route("/signup", methods = ["POST", "GET"])
def signup():
	try:
		if request.method == "POST":
			session = DBSession()
			email_value = request.form.get("email", None)
			name_value = request.form.get("name", None)
			password_value = request.form.get("password", None)
			location_value = request.form.get("location", None)
			unit_preferred_value = request.form.get("unit", None)
			phone_number_value = request.form.get("phone", None)
			school_value = request.form.get("school", None)
			user = User(email = email_value,
						name = name_value,
						password = password_value,
						location = location_value,
						unit_preferred = unit_preferred_value,
						school = school_value,
						phone_number = phone_number_value
						)
			session.add(user)
			session.commit()
			return "Success"
		else:
			return render_template("login.html")
	except Exception as e:
		raise e 


if __name__ == "__main__":
	application.run(debug = True)