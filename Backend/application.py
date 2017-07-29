from flask import Flask, render_template, request, url_for, redirect
from database_setup import Pics, LessonPlan, User, Videos, Tag, Comment,DBSession 
from werkzeug import secure_filename
import os
from flask_login import LoginManager, UserMixin,login_required, login_user, logout_user, current_user

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = "./uploads/"
application.secret_key = 'super secret key'
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = "login"
login_manager.session_protection = "strong"
@login_manager.user_loader
def load_user(userid):
    user = User()
    user.id = userid
    return user

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
				login_user(user)
				return redirect(url_for("dashboard"))
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
			return redirect(url_for('dashboard'))
		else:
			return render_template("login.html")
	except Exception as e:
		raise e 


@application.route("/dashboard", methods = ["GET", "POST"])
@login_required
def dashboard():
	session = DBSession()
	lesson_plans = session.query(LessonPlan).filter_by(user_id = current_user.get_id()).all()
	return render_template('dashboard.html', plans = lesson_plans)

@application.route("/lesson_plan", methods = ["GET", "POST"])
@login_required
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
			user_id_value = current_user.get_id()
			print user_id_value
			file = request.files["video"]
			file.save(os.path.join("./uploads", secure_filename(file.filename)))
			lesson_plan = LessonPlan(unit = unit_value,
									title = title_value,
									purpose = purpose_value,
									class_value = grade_value,
									user_id = user_id_value,
									description = description_value,
									timestamp = time_value)
			session.add(lesson_plan)
			added_lesson_plans = session.query(LessonPlan).all()
			pic = Pics(path = application.config["UPLOAD_FOLDER"] + file.filename, lesson_id = added_lesson_plans[-1].id)
			print application.config["UPLOAD_FOLDER"] + file.filename,
			session.add(pic)
			session.commit()
			return "Success"
		else:
			return render_template("create_lesson.html")
	except Exception as e:
		raise e

@application.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
if __name__ == "__main__":
	application.run(debug=True)

