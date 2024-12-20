#Dylan Forck
#Project
#Description: Student Management System - SQL Alchemy



#Import SQL alchemy module
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base

#Create the base class
Base = declarative_base()

#Create the engine object
engine = create_engine('sqlite:///students.db', echo=True)

#Create the Student Class
class Student(Base):

    #Create the student table
    __tablename__ = 'student'

    #Student table columns
    id = Column(String(9), primary_key=True, unique=True)
    name = Column(String(32), nullable=False)
    age = Column(Integer)
    gender = Column(String(1))
    major = Column(String(32))
    phone = Column(String(32))


#Create the User Class
class User(Base):

    #Create the user table
    __tablename__ = 'user'

    #User table columns
    username = Column(String(32), primary_key=True, nullable=False)
    password = Column(String(32), nullable=False)

#Create the Score Class
class Score(Base):

    #Create the score table
    __tablename__ = 'score'

    #Score table columns
    id = Column(String(9), primary_key=True, unique=True)
    name = Column(String(32), nullable=False)
    CS1030 = Column(Integer)
    CS1100 = Column(Integer)
    CS2030 = Column(Integer)

#Create tables
Base.metadata.create_all(engine)

#Create a session
Session = sessionmaker(bind=engine)
session = Session()

