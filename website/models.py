from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    data = db.Column(db.String(10000))
    href = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Koolitus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    data = db.Column(db.String(10000))
    when = db.Column(db.String(10000))
    img = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Tooted(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    data = db.Column(db.String(10000))
    qty = db.Column(db.String(10000))
    img = db.Column(db.String(10000))
    tag = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())