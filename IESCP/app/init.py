from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

my_app = Flask(__name__)
my_app.config['SECRET_KEY'] = 'your_secret_key'
my_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
database = SQLAlchemy(my_app)
migrate = Migrate(my_app, database)
login_manager = LoginManager(my_app)
bcrypt = Bcrypt(my_app)

from app import routes, models
