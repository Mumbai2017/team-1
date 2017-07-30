from flask import Flask, render_template, request, url_for, redirect, flash
from database_setup import Pics, LessonPlan, User, Videos, Tag, Comment,DBSession
from werkzeug import secure_filename
import os
from flask_login import LoginManager, UserMixin,login_required, login_user, logout_user, current_user
import hashlib
import os

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
			candidate = 'secret'
			user = session.query(User).filter_by(email = username).first()
			password_value = (hashlib.md5(request.form["password"].encode())).hexdigest()
			if username == "admin@email.com" and request.form["password"] == "admin":
				return render_template("admin_dashboard.html")
			elif user is not None and password_value == user.password:
				login_user(user)
				return redirect(url_for("dashboard"))
			return "Error"
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
			password_value = (hashlib.md5(request.form["password"].encode())).hexdigest()
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
			unit_value = request.form.get("unit", None)
			title_value = request.form.get("title", None)
			purpose_value = request.form.get("purpose")
			grade_value = request.form.get("grade")
			description_value = request.form.get("description", None)
			time_value = request.form.get("time", None)
			user_id_value = current_user.get_id()
			file = request.files["video"]
			if file is not None:
				file.save(os.path.join("./uploads", secure_filename(file.filename)))
			lesson_plan = LessonPlan(unit = unit_value,
									title = title_value,
									purpose = purpose_value,
									class_value = grade_value,
									user_id = user_id_value,
									description = description_value,
									timestamp = time_value)
			session.add(lesson_plan)
			if file is not None:
				added_lesson_plans = session.query(LessonPlan).all()
				pic = Pics(path = application.config["UPLOAD_FOLDER"] + file.filename, lesson_id = added_lesson_plans[-1].id)
				session.add(pic)
			session.commit()
			return redirect(url_for("lesson_detail"))
		else:
			return render_template("create_lesson.html")
	except Exception as e:
		raise e

@application.route("/video_upload", methods = ["GET", "POST"])
def video_upload():
	return render_template("video_upload.html")

@application.route("/lesson_detail", methods = ["GET", "POST"])
@login_required
def lesson_detail():
	try:
		session = DBSession()
		video_values = session.query(Videos).filter_by(user_id = current_user.get_id()).all()
		return render_template("lesson_page.html", videos = video_values)
	except Exception as e:
		raise e


@application.route("/add_video/<videoid>", methods = ["GET"])
@login_required
def add_video(videoid):
	try:
		session = DBSession()
		video = Videos(user_id = current_user.get_id(), video_link = videoid)
		session.add(video)
		session.commit()
		return redirect(url_for("lesson_detail"))
	except Exception as e:
		raise e

@application.route("/video_detail/<link>", methods = ["GET"])
@login_required
def video_detail(link):
	session = DBSession()
	comments_array = session.query(Comment).filter_by(video_id = "https://www.youtube.com/embed/" + link).all()
	return render_template("comments.html", video_link = "https://www.youtube.com/embed/" + link, comments = comments_array)

@application.route("/comments", methods = ["GET", "POST"])
def comments():
	try:
		if request.method == "POST":
			session = DBSession()
			comment = request.form.get("comment", None)
			time = request.form.get("time", None)
			video = request.form.get("video_link",None)
			comment_value = Comment(data = comment, timestamp = time, video_id = video, user_id = current_user.get_id(), parent_id = 1)
			session.add(comment_value)
			session.commit()
			data = ["video_detail", video]
			return redirect(url_for('lesson_detail'))
 	except Exception as e:
		print e

@application.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
if __name__ == "__main__":
	#application.run(debug=True)
	#application.run(host="0.0.0.0", port=8080)
	application.run(host = '0.0.0.0', port = int(os.environ.get("PORT")))
