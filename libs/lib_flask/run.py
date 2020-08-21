from flask import Flask, url_for, request, render_template
from markupsafe import Markup, escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template("hello.html", name=name)

@app.route("/user/<username>")
def user(username):
    return "User %s" % escape(username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "ELO"
    else:
        return "NIEELO"