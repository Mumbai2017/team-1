from flask import Flask, render_template, request, url_for, redirect, login_required
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
				return redirect(url_for('dashboard'))
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

@application.route("/dashboard", methods = ["GET", "POST"])
def dashboard():
	return render_template('dashboard.html')

@application.route("/lesson_plan", methods = ["GET", "POST"])
def lesson_plan():
	try:
		if request.method == "POST":
			session = DBSession()
			unit_value = request.form["unit"]
			title_value = request.form["title"]
			purpose_value = request.form["purpose"]
			grade_value = request.form["grade"]
			description_value = request.form["description"]
			time_value = request.form["time"]
			user_id_value = 1
			lesson_plan = LessonPlan(unit = unit_value,
									title = title_value,
									purpose = purpose_value,
									class_value = grade_value,
									user_id = user_id_value,
									description = description_value,
									timestamp = time_value)
			session.add(lesson_plan)
			session.commit()
			return "Success"
		else:
			return render_template("create_lesson.html")
	except Exception as e:
		raise e

if __name__ == "__main__":
	application.run(host = "0.0.0.0", port=5000)