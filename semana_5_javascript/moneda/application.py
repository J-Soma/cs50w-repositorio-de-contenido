import requests
import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convertir", methods=["POST"])
def convertir():

    # Consultar por tasa de cambio de moneda
    moneda = request.form.get("moneda")
    print(moneda)
    respuesta = requests.get(f"https://api.apilayer.com/fixer/latest?symbols={moneda}&base=USD",
                            headers={"apikey": os.getenv("API_KEY")})

    # Asegurarnos que la solicitud es exitosa
    if respuesta.status_code != 200:
        return jsonify({"exito": False})

    # Asegurarnos de que la moneda se encuentra en la respuesta
    datos = respuesta.json()
    print(datos)

    if moneda not in datos["rates"]:
        return jsonify({"exito": False})

    return jsonify({"exito": True, "tasa": datos["rates"][moneda]})
