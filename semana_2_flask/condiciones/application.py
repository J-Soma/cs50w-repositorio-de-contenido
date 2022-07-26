import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    fecha_actual = datetime.datetime.now()
    anio_nuevo = fecha_actual.month == 1 and fecha_actual.day == 1
    print(fecha_actual)
    return render_template("index.html", anio_nuevo=anio_nuevo)
