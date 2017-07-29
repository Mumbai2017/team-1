from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Pics(Base):

	__tablename__ = "Pics"

	id = Column(Integer, primary_key = True)
	path = Column(String(100), unique = True, nullable = False)
	lesson_id = Column(Integer, unique = False)


class LessonPlan(Base):

	__tablename__ = "LessonPlan"

	id = Column(Integer, primary_key = True)
	unit = Column(String(100), unique = False)
	title = Column(String(100), unique = False)
	purpose = Column(String(1000), unique = False)
	class_value = Column(String(10), unique = False)
	user_id = Column(Integer, unique = False)
	description = Column(String(10000), unique = False, nullable = False)
	timestamp = Column(String(100), unique = False, nullable = False)

class User(Base):

	__tablename__ = "User"

	id = Column(Integer, primary_key = True)
	email = Column(String(100), unique = True, nullable = False)
	name = Column(String(100), unique = False, nullable = False)
	password = Column(String(1000), unique = False, nullable = False)
	location = Column(String(100), unique = False, nullable = False)
	unit_preferred = Column(String(100), unique = False, nullable = False)
	phone_number = Column(String(10), unique = True, nullable = False)

class Videos(Base):

	__tablename__ = "Videos"

	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, unique = False, nullable = False)
	video_link = Column(String(100), unique = True, nullable = False)
	tags = Column(MutableList.as_mutable(ARRAY(String(100))))

class Tag(Base):

	__tablename__ = "Tag"

	id = Column(Integer, primary_key = True)
	tag_value = Column(String(100), unique = False, nullable = False)
	video_id = Column(Integer, unique = False, nullable = False)
	
class Comment(Base):

	__tablename__ = "Comment"

	id = Column(Integer, primary_key = True)
	data = Column(Text, unique = False, nullable = False)
	timestamp = Column(String(100), unique = False, nullable = False)
	video_id = Column(Integer, unique = False, nullable = False)
	user_id = Column(Integer, unique = False, nullable = False)
	parent_id = Column(Integer, unique = False, nullable = True)

engine = create_engine("sqlite:///codeforgood.db")
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

