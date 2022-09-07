import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    vuelos = db.execute("SELECT * FROM vuelos").fetchall()
    return render_template("index.html", vuelos=vuelos)

@app.route("/reservar", methods=["POST"])
def reservar():
    """Reservar un vuelo."""

    # Obtener informacion de formulario.
    nombre = request.form.get("nombre")
    try:
        id_vuelo = int(request.form.get("id_vuelo"))
    except ValueError:
        return render_template("error.html", mensaje="Numero de vuelo no valido.")

    # Asegurarnos que el vuelo existe.
    if db.execute("SELECT * FROM vuelos WHERE id = :id", {"id": id_vuelo}).rowcount == 0:
        return render_template("error.html", mensaje="No existe un vuelo con ese ID.")
    db.execute("INSERT INTO pasajeros (nombre, id_vuelo) VALUES (:nombre, :id_vuelo)",
            {"nombre": nombre, "id_vuelo": id_vuelo})
    db.commit()
    return render_template("exito.html")

@app.route("/vuelos")
def vuelos():
    """Listar todos los vuelos."""
    vuelos = db.execute("SELECT * FROM vuelos").fetchall()
    return render_template("vuelos.html", vuelos=vuelos)

@app.route("/vuelos/<int:id_vuelo>")
def vuelo(id_vuelo):
    """Lista los detalles de un vuelo."""

    # Asegurarnos que el vuelo existe.
    vuelo = db.execute("SELECT * FROM vuelos WHERE id = :id", {"id": id_vuelo}).fetchone()
    if vuelo is None:
        return render_template("error.html", mensaje="No existe ese vuelo.")

    # Obtener todos los pasajeros.
    pasajeros = db.execute("SELECT nombre FROM pasajeros WHERE id_vuelo = :id_vuelo",
                            {"id_vuelo": id_vuelo}).fetchall()
    return render_template("vuelo.html", vuelo=vuelo, pasajeros=pasajeros)
