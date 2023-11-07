from flask import Blueprint, render_template, request
lab4 = Blueprint("lab4", __name__)


@lab4.route("/lab4/")
def lab():
    return render_template("lab4.html")


@lab4.route("/lab4/login/", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        print(request.method)
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")
    if username == "alex" and password == "123":
        return render_template("success4.html", username=username)

    if not username and not password:
        error = "Не введен логин и пароль!"
        return render_template("login.html", error=error, username=username, password=password)
    elif not password:
        error = "Не введён пароль!"
        return render_template("login.html", error=error, username=username, password=password)
    elif not username:
        error = "Не введён логин!"
        return render_template("login.html", error=error, username=username, password=password)
    else:
        error = "Неверный логин и/или пароль!"
        return render_template("login.html", error=error, username=username, password=password)


@lab4.route("/lab4/fridge/", methods=["POST", "GET"])
def fridge():
    if request.method == "GET":
        return render_template("fridge.html")

    temp = request.form.get("temp")
    if not temp:
        error = "Ошибка: не задана температура!"
        return render_template("fridge.html", error = error)
    elif int(temp) < -12:
        error = "Не удалось установить температуру — слишком низкое значение!"
        return render_template("fridge.html", error = error)
    elif int(temp) > -1:
        error = "Не удалось установить температуру — слишком высокое значение!"
        return render_template("fridge.html", error = error)
    elif int(temp) >= -12 and int(temp) <= -9:
        error = "Установлена температура: " + str(temp) + "°С ❆❆❆"
        return render_template("temp.html", error = error)
    elif int(temp) >= -8 and int(temp) <= -5:
        error = "Установлена температура: " + str(temp) + "°С ❆❆"
        return render_template("temp.html", error = error)
    else:
        error = "Установлена температура: " + str(temp) + "°С ❆"
        return render_template("temp.html", error = error)
