import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Vuelo(db.Model):
    __tablename__ = "vuelos"
    id = db.Column(db.Integer, primary_key=True)
    origen = db.Column(db.String, nullable=False)
    destino = db.Column(db.String, nullable=False)
    duracion = db.Column(db.Integer, nullable=False)

    def agregar_pasajero(self, nombre):
        p = Pasajero(nombre=nombre, id_vuelo=self.id)
        db.session.add(p)
        db.session.commit()


class Pasajero(db.Model):
    __tablename__ = "pasajeros"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    id_vuelo = db.Column(db.Integer, db.ForeignKey("vuelos.id"), nullable=False)
