from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import Koolitus, Tooted

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html")


@views.route("/tooted")
def tooted():
    toys = Tooted.query.filter_by(tag="toy")
    food = Tooted.query.filter_by(tag="food")
    misc = Tooted.query.filter_by(tag="misc")
    return render_template("tooted.html", toys=toys,food=food, misc=misc)

@views.route("/kursused")
def kursused():
    return render_template("kursused.html")


@views.route("/koolitused")
def koolitused():
    resp = Koolitus.query.all()
    return render_template("koolitused.html", resp1=resp)