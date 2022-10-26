import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    vuelos = db.execute("SELECT origin, destino, duracion FROM Vuelo").fetchall()
    for vuelo in vuelos:
        print(f"{vuelo.origen} hacia {vuelo.destino}, {vuelo.duracion} minutos.")

if __name__ == "__main__":
    main()
