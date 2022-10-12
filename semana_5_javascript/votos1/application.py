import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

votos = {"si": 0, "no": 0, "talvez": 0}


@app.route("/")
def index():
    return render_template("index.html", votos=votos)


@socketio.on("guardar voto")
def voto(dato):
    seleccion = dato["seleccion"]
    votos[seleccion] += 1
    emit("total votos", votos, broadcast=True)
