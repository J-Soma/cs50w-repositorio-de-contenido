import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("vuelos.csv")
    filas = csv.reader(f)
    for origen, destino, duracion in filas:
        db.execute("INSERT INTO vuelos (origen, destino, duracion) VALUES (:origen, :destino, :duracion)",
                    {"origen": origen, "destino": destino, "duracion": duracion})
        print(f"Agregado vuelo desde {origen} hasta {destino} durando {duracion} minutos.")
    db.commit()

if __name__ == "__main__":
    main()
