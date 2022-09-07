import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    vuelos = db.execute("SELECT origen, destino, duracion FROM vuelos").fetchall()
    for vuelo in vuelos:
        print(f"{vuelo.origen} to {vuelo.destino}, {vuelo.duracion} minutes.")

if __name__ == "__main__":
    main()