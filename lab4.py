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


@lab4.route("/lab4/offer/", methods=["POST", "GET"])
def offer():
    type_offer = request.form.get("type_offer")
    if request.method == "GET":
        return render_template("offer.html")
    
    weight = request.form.get("weight")
    if not weight:
        error = "Не введён вес!"
        return render_template("offer.html", error = error)
    elif int(weight) <= 0:
        error = "Неверное значение веса!"
        return render_template("offer.html", error = error)
    elif int(weight) > 500:
        error = "Такого объёма сейчас нет в наличии!"
        return render_template("offer.html", error = error)
    elif str(type_offer) == "zerno":
        error = "Выберите зерно!"
        return render_template("offer.html", error = error)
    elif int(weight) <= 500 and int(weight) >= 50:
        weight = int(weight)
        prices = {
        'yach': 12000,
        'oves': 8500,
        'psh': 8700,
        'poz': 14000
        }
        price_per_ton = prices[type_offer]
        total_price = weight * price_per_ton
        total_price *= 0.9

        if type_offer == "yach":
            type_offer = "ячмень"
        elif type_offer == "psh":
            type_offer = "пшеница"
        elif type_offer == "poz":
            type_offer = "рожь"
        else:
            type_offer = "овес"

        return render_template("offer_conf%.html", total_price = total_price, type_offer = type_offer)
    else:
        weight = int(weight)
        prices = {
        'yach': 12000,
        'oves': 8500,
        'psh': 8700,
        'poz': 14000
        }
        price_per_ton = prices[type_offer]
        total_price = weight * price_per_ton

        if type_offer == "yach":
            type_offer = "ячмень"
        elif type_offer == "psh":
            type_offer = "пшеница"
        elif type_offer == "poz":
            type_offer = "рожь"
        else:
            type_offer = "овес"

        return render_template("offer_conf.html", total_price = total_price, weight = weight, type_offer = type_offer)


    return render_template("offer.html")
