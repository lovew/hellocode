import flask
from myfun import *
from flask import Flask, request, make_response
app = Flask(__name__)


@app.route("/")
def hello():
    first_name = request.args.get('name', '')
    print(first_name)
    myhello1(first_name)
    return "Hello World!"
