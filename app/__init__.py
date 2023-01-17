from flask import Flask
 
app = Flask(__name__, static_folder='static')
 
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '4c4e82067c705665274f8d1d33d5fd847622416172c2f7ef'
 
app.config['JSON_AS_ASCII'] = False

from app import views  # noqa