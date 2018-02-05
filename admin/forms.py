from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo

# Abstract Representaion of Login form
class LoginForm(FlaskForm):
    username = StringField('username', [InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', [InputRequired(), Length(min=8, max=50)])
    remember = BooleanField('Remember Me')

# Abstract Representaion of Signup form
class RegisterForm(FlaskForm):
    name = StringField('full name', [InputRequired()])
    email = StringField('email', [InputRequired(), Email(message ='Invalid email'), Length(max=50)])
    username = StringField('username', [InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', [InputRequired(), Length(min=8, max=50), EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')