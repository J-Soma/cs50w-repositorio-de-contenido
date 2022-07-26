from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "Hola, mundo!"
    return render_template("index.html", titulo=titulo)
