from sqlalchemy import Column, Integer, String
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
	timestamp = Column(Stirng(100), unique = False, nullable = False)

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
	
