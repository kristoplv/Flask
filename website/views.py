from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    return render_template("home.html")


@views.route("/tooted")
def tooted():
    return render_template("tooted.html")

@views.route("/kursused")
def kursused():
    return render_template("kursused.html")


@views.route("/koolitused")
def koolitused():
    return render_template("koolitused.html")