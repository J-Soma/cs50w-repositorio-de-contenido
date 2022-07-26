from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hola", methods=["POST"])
def hola():
    nombre = request.form.get("nombre")
    return render_template("hola.html", nombre=nombre)
