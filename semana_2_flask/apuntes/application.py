from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

apuntes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        apunte = request.form.get("apunte")
        apuntes.append(apunte)

    return render_template("index.html", apuntes=apuntes)
