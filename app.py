from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ ФБ Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>

        <ol>
            <li><a href="http://127.0.0.1:5000/lab1">Первая лабораторная</a></li>
            <li><a href="http://127.0.0.1:5000/lab2">Вторая лабораторная</a></li>
        <ol>

        </main>

        <footer>
            &copy; Донельчук Артём, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Донельчук Артём Вячеславович, лабораторная работа 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
              программирования Python, использующий набор инструментов Werkzeug,
                а также шаблонизатор Jinja2. Относится к категории так называемых
                  микрофреймворков — минималистичных каркасов веб-приложений,
                    сознательно предоставляющих лишь самые базовые возможности.
        </p>
        
        <p>
            <a href="http://127.0.0.1:5000/menu">Меню</a>
        </p>

        <h1>Реализованные роуты</h1>

        <ul>
            <li><a href="http://127.0.0.1:5000/lab1/oak">/lab1/oak - дуб</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/student">/lab1/student - студент</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/python">/lab1/python - python</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/jinja">/lab1/jinja - jinja</a></li>
        </ul>

        <footer>
            &copy; Донельчук Артём, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
            <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
<head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Донельчук Артём Вячеславович</h1>
            <img src="''' + url_for('static', filename='logo.png') + '''">
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
<head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Python</h1>
        <p>
            Python — это язык программирования, который широко используется в интернет-приложениях, 
            разработке программного обеспечения, науке о данных и машинном обучении.
            Разработчики используют Python, потому что он эффективен, прост в изучении и работает на разных платформах.
        </p>

        <p>
            Для него написано множество фреймворков: FastAPI, Flask, Tornado, Pyramid, 
            TurboGears, CherryPy и, самый популярный, Django. Ещё на Python пишут парсеры для сбора информации с веб-страниц.
        </p>

        <p>
            Минусом является его малое быстродействие и недостаточные возможности статического анализа кода. 
            Эти проблемы взаимосвязаны, и решение последней автоматически откроет дорогу для решения первой.
        </p>
            <img src="''' + url_for('static', filename='python.png') + '''">
    </body>
</html>
'''

@app.route("/lab1/jinja")
def jinja():
    return '''
<!doctype html>
<html>
<head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Jinja</h1>
        <p>
            Jinja — это шаблонизатор для языка программирования Python. Он подобен шаблонизатору 
            Django, но предоставляет Python-подобные выражения, обеспечивая исполнение шаблонов в 
            песочнице. Это текстовый шаблонизатор, поэтому он может быть использован для 
            создания любого вида разметки, а также исходного кода.
        </p>

        <p>
            Шаблонизаторы — специализированные библиотеки, которые позволяют описывать шаблон отдельно от остальной части кода.
        </p>

        <p>
           Преимущества языка шаблонов Jinja2: 
           <ol>
                <li>Автоматическая система экранирования HTML для предотвращения XSS.</Li>
                <li>Наследование шаблонов, поддержка макросов.</li>
                <li>Шаблоны компилируются до оптимального кода Python.</li>
           </ol>
        </p>
            <img src="''' + url_for('static', filename='jinja.png') + '''">
    </body>
</html>
'''

@app.route("/lab2/example")
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

@app.route("/lab2")
def lab2():
    return render_template("lab2.html")

@app.route("/lab2/rose")
def rose():
    return render_template("rose.html")
