from flask import Blueprint, render_template
lab2 = Blueprint("lab2", __name__)


@lab2.route("/lab2/example")
def example():
    name, get_lab_num, get_cou_num, get_gro_num = "Артём Донельчук", 2, 3, "ФБИ-13"
    fruits = [
        {"name": "яблоки", "price": 100},
        {"name": "груши", "price": 120},
        {"name": "апельсины", "price": 80},
        {"name": "мандарины", "price": 95},
        {"name": "манго", "price": 321}
    ]
    books = [
        {"author": "Иван Тургенев", "book_name": "Ася", "genre": "повесть", "pages": "11"},
        {"author": "Николай Гоголь", "book_name": "Ревизор", "genre": "комедия", "pages": "31"},
        {"author": "Фёдор Достоевский", "book_name": "Преступление и наказание", "genre": "роман", "pages": "113"},
        {"author": "Александр Пушкин", "book_name": "Пиковая дама", "genre": "повесть", "pages": "6"},
        {"author": "Михаил Шолохов", "book_name": "Они сражались за Родину", "genre": "роман", "pages": "34"},
        {"author": "Антон Чехов", "book_name": "Дама с собачкой", "genre": "рассказ", "pages": "4"},
        {"author": "Нора Робертс", "book_name": "Отныне и навсегда", "genre": "роман", "pages": "114"},
        {"author": "Михаил Булгаков", "book_name": "Собачье сердце", "genre": "повесть", "pages": "32"},
        {"author": "Лев Толстой", "book_name": "Анна Каренина", "genre": "роман", "pages": "196"},
        {"author": "Максим Горький", "book_name": "Старуха Изергиль", "genre": "рассказ", "pages": "4"}
    ]
    return render_template("example.html",get_lab_num=get_lab_num, fruits=fruits, books=books)


@lab2.route("/lab2")
def lab_dva():
    return render_template("lab2.html")


@lab2.route("/lab2/rose")
def rose():
    return render_template("rose.html")

