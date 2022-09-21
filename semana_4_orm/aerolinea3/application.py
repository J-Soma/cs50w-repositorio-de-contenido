from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    vuelos = Vuelo.query.all()
    return render_template("index.html", vuelos=vuelos)


@app.route("/reservar", methods=["POST"])
def reservar():
    """Reserva un vuelo."""

    # Obtener información de formulario.
    name = request.form.get("name")
    nombre = request.form.get("nombre")
    try:
        id_vuelo = int(request.form.get("id_vuelo"))
    except ValueError:
        return render_template("error.html", mensaje="Número de vuelo no válido.")

    # Asegurarnos de que el vuelo existe.
    vuelo = Vuelo.query.get(id_vuelo)
    if vuelo is None:
        return render_template("error.html", mensaje="No existe un vuelo con ese id.")

    # Agregar pasajero.
    vuelo.agregar_pasajero(nombre)
    return render_template("exito.html")


@app.route("/vuelos")
def vuelos():
    """Lista todos los vuelos."""
    vuelos = Vuelo.query.all()
    return render_template("vuelos.html", vuelos=vuelos)


@app.route("/vuelos/<int:id_vuelo>")
def vuelo(id_vuelo):
    """Lista los detalles de un solo vuelo."""

    # Asegurarnos de que el vuelo existe.
    vuelo = Vuelo.query.get(id_vuelo)
    if vuelo is None:
        return render_template("error.html", mensage="No existe ese vuelo.")

    # Obtener todos los pasajeros.
    pasajeros = Pasajero.query.filter_by(id_vuelo=id_vuelo).all()
    return render_template("vuelo.html", vuelo=vuelo, pasajeros=pasajeros)
