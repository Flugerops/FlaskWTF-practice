from app import app
from app.forms import UserNameForm, PasswordForm
from flask import flash, request, render_template, Request, redirect, url_for
from flask_wtf import Form


@app.get("/")
def index():
    return render_template("base.html")


@app.get("/success")
def success():

    return render_template("success.html")


@app.get("/register_username")
def username_get():
    form = UserNameForm(request.form)
    return render_template("username.html", form=form)


@app.post("/register_username")
def username_post():
    form = UserNameForm(
        request.form,
    )
    form: Form
    if form.validate():
        return redirect(url_for("password_get"))
    print(f"{form.errors=}")
    return render_template("username.html", form=form)


@app.get("/register_password")
def password_get():
    form = PasswordForm(request.form)
    return render_template("password.html", form=form)


@app.post("/register_password")
def password_post():
    form = PasswordForm(
        request.form,
    )
    form: Form
    if form.validate():
        return redirect(url_for("success"))
    print(f"{form.errors=}")
    return render_template("password.html", form=form)
