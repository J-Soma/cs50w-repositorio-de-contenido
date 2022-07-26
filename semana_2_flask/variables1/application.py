import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    titulo = random.choice(["Hola, mundo!", "Hey, hola!", "Buenos d&iacute;as!"])
    return render_template("index.html", titulo=titulo)
