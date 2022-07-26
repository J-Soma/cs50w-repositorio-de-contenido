from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola, mundo!"

@app.route("/david")
def david():
    return "Hola, David!"
