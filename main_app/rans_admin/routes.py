# Import flask dependencies
from flask import Blueprint, render_template, redirect, url_for

# for hashing passwords
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user, login_required, current_user

# Import database object from main_app
from main_app import db, login_manager

# Import from forms.py
from main_app.rans_admin.forms import LoginForm, RegisterForm

# Import user models from models folder
from main_app.rans_admin.models.users import User


# Blueprint definition
mod_admin = Blueprint('rans_admin', __name__)



@mod_admin.route('/')
def index():
    return render_template('rans_admin/index.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@mod_admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('rans_admin/dashboard'))

        return '<h1> Invalid username or password </h1>'


    return render_template('rans_admin/login.html', form=form)

@mod_admin.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>' + form.username.data + ' has been registered </h1>'


    return render_template('rans_admin/signup.html', form=form)

@mod_admin.route('/dashboard')
@login_required
def dashboard():
    return render_template('rans_admin/dashboard.html', name=current_user.username)

@mod_admin.route('/logout')
@login_required
def logout():
    return redirect(url_for('index'))