from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, NIG!</p>"

@app.route('/hello/')
def hello_world1():
    return '<h1>Hi my name is Thiti<h2>'