from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# Instantiate app object
app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config.from_pyfile('instance/config.py')

# Initializations of the libraries
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from admin.views import *

if __name__ == '__main__':
    app.run()


