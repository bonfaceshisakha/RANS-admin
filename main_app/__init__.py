# import flask and template operators
from flask import Flask
# database connection library
from flask_sqlalchemy import SQLAlchemy
# Import Bootstrap Flask library
from flask_bootstrap import Bootstrap
# Import LoginManager module in flask_login
from flask_login import LoginManager

# Flask app Initialization
app = Flask(__name__)

# Import configuration settings
app.config.from_pyfile('config.py')

# database object for routes in various blueprints
db = SQLAlchemy(app)

# Other initializations
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import various blueprint modules
from main_app.api.routes import mod_api
from main_app.rans_admin.routes import mod_admin
from main_app.rans_website.routes import mod_website

# Register blueprint modules
app.register_blueprint(mod_website)
app.register_blueprint(mod_admin, url_prefix='/admin')
app.register_blueprint(mod_api, url_prefix='/api')