import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    vuelos = Vuelo.query.all()
    for vuelo in vuelos:
        print(f"Vuelo {vuelo.id}: {vuelo.origen} to {vuelo.destino}, {vuelo.duracion} minutos.")

    # Solicitarle al usuario escoger un vuelo.
    id_vuelo = int(input("\nID Vuelo: "))
    vuelo = Vuelo.query.get(id_vuelo)

    # Asegurarnos de que el vuelo es valido.
    if vuelo is None:
        print("Error: No existe ese vuelo.")
        return

    pasajeros = Pasajero.query.filter_by(id_vuelo=id_vuelo).all()
    print("\nPasajeros:")
    for pasajero in pasajeros:
        print(pasajero.nombre)
    if len(pasajeros) == 0:
        print("No hay pasajeros.")

if __name__ == "__main__":
    with app.app_context():
        main()
