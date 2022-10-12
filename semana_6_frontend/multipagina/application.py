from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def primera():
    return render_template("primera.html")

@app.route("/segunda")
def segunda():
    return render_template("segunda.html")

@app.route("/tercera")
def tercera():
    return render_template("tercera.html")
