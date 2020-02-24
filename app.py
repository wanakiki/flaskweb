from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world</h1>'

@app.route('/<name>')
def say_hello(name):
    return '<h1>hello %s!' % name
    