import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("vuelos.csv")
    lector = csv.reader(f)
    for origen, destino, duracion in lector:
        vuelo = Vuelo(origen=origen, destino=destino, duracion=duracion)
        db.session.add(vuelo)
        print(f"Agregado vuelo desde {origen} hacia {destino} durando {duracion} minutos.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
