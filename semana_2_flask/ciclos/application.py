from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nombres = ["Alice", "Bob", "Charlie"]
    return render_template("index.html", nombres=nombres)
