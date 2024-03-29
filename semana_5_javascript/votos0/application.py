import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("guardar voto")
def voto(dato):
    seleccion = dato["seleccion"]
    emit("anunciar voto", {"seleccion": seleccion}, broadcast=True)
