import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():

    # Listar todos los vuelos.
    vuelos = db.execute("SELECT id, origen, destino, duracion FROM vuelos").fetchall()
    for vuelo in vuelos:
        print(f"Vuelo {vuelo.id}: {vuelo.origen} hacia {vuelo.destino}, {vuelo.duracion} minutos.")

    # Solicitar al usuario escoger un vuelo.
    id_vuelo = int(input("\nID vuelo: "))
    vuelo = db.execute("SELECT origen, destino, duracion FROM vuelos WHERE id = :id",
                        {"id": id_vuelo}).fetchone()

    # Asegurarnos que el vuelo es valido.
    if vuelo is None:
        print("Error: No existe ese vuelo.")
        return

    # Listar pasajeros.
    pasajeros = db.execute("SELECT nombre FROM pasajeros WHERE id_vuelo = :id_vuelo",
                            {"id_vuelo": id_vuelo}).fetchall()
    print("\nPasajeros:")
    for pasajero in pasajeros:
        print(pasajero.nombre)
    if len(pasajeros) == 0:
        print("No hay pasajeros.")

if __name__ == "__main__":
    main()
