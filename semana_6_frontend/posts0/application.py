import time

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts", methods=["POST"])
def posts():

    # Obtener punto de inicio y fin para generar posts.
    inicio = int(request.form.get("inicio") or 0)
    fin = int(request.form.get("fin") or (inicio + 9))

    # Generar lista de posts.
    datos = []
    for i in range(inicio, fin + 1):
        datos.append(f"Post #{i}")

    # Demorar artificialmente la velocidad de respuesta.
    time.sleep(1)

    # Retornar lista de posts.
    return jsonify(datos)
