from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ver-mas")
def ver_mas():
    return render_template("ver-mas.html")
