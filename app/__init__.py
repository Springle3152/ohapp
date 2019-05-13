from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# create and config app
app = Flask(__name__)
app.config.from_object(Config)

# set up plugins
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'  # set the login page

from app import routes, models  # noqa