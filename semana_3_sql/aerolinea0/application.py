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

    # Asegurarnos de que el vuelo existe.
    if db.execute("SELECT * FROM vuelos WHERE id = :id", {"id": id_vuelo}).rowcount == 0:
        return render_template("error.html", mensaje="No existe un vuelo con ese ID.")
    db.execute("INSERT INTO pasajeros (nombre, id_vuelo) VALUES (:nombre, :id_vuelo)",
            {"nombre": nombre, "id_vuelo": id_vuelo})
    db.commit()
    return render_template("exito.html")

