from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password or username!", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login.html", boolean=True)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign", methods=["GET", "POST"])
def sign():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        pw = request.form.get("pass")
        pw_rep = request.form.get("pass_rep")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists!", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters!", category="error")
        elif len(name) < 2:
            flash("Name must be greater than 1 character!", category="error")
        elif pw != pw_rep:
            flash("Paswords do not match!", category="error")
        elif len(pw) < 7:
            flash("Password must be greater than 6 characters!", category="error")
        else:
            new_user = User(email=email, password=generate_password_hash(pw, method='pbkdf2'), name=name)
            db.session.add(new_user)
            db.session.commit()

            flash("Account created!", category="success")
            login_user(new_user, remember=True)
            return redirect(url_for("views.home"))

    return render_template("signup.html")