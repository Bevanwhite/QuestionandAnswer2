import os
import numpy as np
from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
import pymysql


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manger = LoginManager(app)
login_manger.login_view = 'users.login'
login_manger.login_message_category = 'info'
mail = Mail(app)

from flaskblog.listening.routes import listening
from flaskblog.reading.routes import reading
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.writing.routes import writing
from flaskblog.speaking.routes import speaking
from flaskblog.quiz.routes import quiz

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(writing)
app.register_blueprint(speaking)
app.register_blueprint(reading)
app.register_blueprint(listening)
app.register_blueprint(quiz)
