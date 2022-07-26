from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola, mundo!"

@app.route("/<string:nombre>")
def hola(nombre):
    return "Hola, {}!".format(nombre)
