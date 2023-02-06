import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__, static_folder='static')
 
 # this DEBUG config here will be overridden by FLASK_DEBUG shell environment
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '4c4e82067c705665274f8d1d33d5fd847622416172c2f7ef'
 
app.config['JSON_AS_ASCII'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

from app import views  # noqa