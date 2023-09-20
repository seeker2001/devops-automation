import os
from flask import Flask, render_template, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
appli_context = app.app_context()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.abspath(os.getcwd())+"\market.db"
app.config['SECRET_KEY'] = 'a814b9cc43b61cd4bb427e2f'
db = SQLAlchemy(app) 
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes