import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
# from flask_mail import Mail

# Create an instance of Flask
app = Flask(__name__)
Bootstrap(app)
csrf = CSRFProtect(app)

# Initialise database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # Database for offline testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('secretkey')
db = SQLAlchemy(app)


import application.models
import application.forms
import application.routes


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')