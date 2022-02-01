import os
import pymysql
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# Create an instance of Flask
app = Flask(__name__)
Bootstrap(app)
csrf = CSRFProtect(app)


# Initialise database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('secretkey')
db = SQLAlchemy(app)

import application.models
import application.forms
import application.routes