from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#Initiaze app and database connection
app = Flask(__name__)

#Configuring MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://pwl:pwl123@localhost:3306/db_flask_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()
