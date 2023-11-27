from flask import Blueprint, render_template, request, redirect
from db import db
from db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
#from flask_login import login_user, login_required, current_user

lab6 = Blueprint("lab6", __name__)

@lab6.route("/lab6/check")
def main():
    my_users = users.query.all()
    print(my_users)
    return "result in console!"


@lab6.route("/lab6/checkarticles")
def mainart():
    my_articles = articles.query.all()
    for article in my_articles:
        print(f"{article.title}-{article.article_text}")
    return "Result in console!"


@lab6.route("/lab6/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register6.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    isUserExist = users.query.filter_by(username = username_form).first()

    errors = []

    if isUserExist is not None:
        errors.append("Такой пользователь уже существует!")
        return render_template("register6.html", errors = errors)
    elif not username_form:
        errors.append("Введите имя пользователя!")
        return render_template("register6.html", errors=errors)
    elif len(password_form) < 5:
        errors.append("Пароль должен содержать не менее 5 символов!")
        return render_template("register6.html", errors=errors)
    


    hashedPswd = generate_password_hash(password_form, method="pbkdf2")

    newUser = users(username = username_form, password = hashedPswd)

    db.session.add(newUser)

    db.session.commit()

    return redirect("login.html")

