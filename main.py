from flask import Flask
from datetime import datetime

# print(__name__)

app = Flask(__name__)

books = {1: "Python book", 2: "Java book", 3: "Flask book"}


@app.route("/bmi/name=<name>&height=<h>&weight=<w>")
def get_bmi(name, h, w):
    try:
        bmi = round(eval(w) / (eval(h) / 100) ** 2, 2)
        return f"<h1>{name} BMI:{bmi}</h1>"
    except Exception as e:
        return f"<h1 style='color:red'>參數不正確誤!!!<br>{e}</h1>"


@app.route("/sum/x=<x>&y=<y>")
def my_sum(x, y):
    # 參數不正確，請輸出參數錯誤 (try + except)
    try:
        total = eval(x) + eval(y)
        return f"<h1>{x}+{y}={total}</h1>"
    except Exception as e:
        return f"<h1 style='color:red'>參數不正確誤!!!<br>{e}</h1>"


@app.route("/book/<int:id>")
def show_book(id):
    if id in books:
        return f"<h1> 第{id}本書:{books[id]}</h1>"
    else:
        return f"<h1 style='color:red'>{id}......無此編號!!!</h1>"


@app.route("/books")
def show_books():
    return books[1]


@app.route("/")
def index():
    today = datetime.now()
    print(today)
    a = 1
    b = 2
    return f"<h1>Ha Ha Ha Ha ! <br>{today}</h1> <br>{a+b}"


app.run(debug=True)
