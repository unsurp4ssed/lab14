from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import UserMixin
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'gdzfiuyg543x==+_(jhytjnhv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbb.db'
db = SQLAlchemy(app)


class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    brand = db.Column(db.String(255))
    price = db.Column(db.Integer)
    photo = db.Column(db.String(255))


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable = False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, default=False)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tovar_id = db.Column(db.Integer)
    like = db.Column(db.Integer)
    comment = db.Column(db.Text)


with app.app_context():
    db.create_all()
