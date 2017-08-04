from flask import Blueprint

mod_website = Blueprint('rans_website', __name__,)

@mod_website.route('/home')
def index():
    return '<h1>You are on the home page </h1>'