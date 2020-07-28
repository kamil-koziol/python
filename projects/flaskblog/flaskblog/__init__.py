from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = '3cc7534e7c9f1c30fe3d33982836208840f6390f390c89ad1521d29162ce8a42'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
from flaskblog import routes