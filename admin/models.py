from run import db
from flask_login import UserMixin

# Class for the users table in MySQL database
class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column('user_ID', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode, unique=True)
    email = db.Column('email', db.Unicode)
    username = db.Column('username', db.Unicode)
    password = db.Column('password', db.Unicode)
    date = db.Column('created_date', db.TIMESTAMP)
