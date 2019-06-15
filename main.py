from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/welcome/<name>")
def welcome(name):
    return "Hello {}!, welcome to this Flask App!".format(name)
