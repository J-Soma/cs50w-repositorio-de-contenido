class Vuelo:

    contador = 1

    def __init__(self, origen, destino, duracion):

        # Mantener rastro de numero de id.
        self.id = Vuelo.contador
        Vuelo.contador += 1

        # Llevar rastro de los pasajeros.
        self.pasajeros = []

        # Detalles del vuelo.
        self.origen = origen
        self.destino = destino
        self.duracion = duracion

    def imprimir_informacion(self):
        print(f"Origen del vuelo: {self.origen}")
        print(f"Destino del vuelo: {self.destino}")
        print(f"Duracion del vuelo: {self.duracion}")

        print()
        print("Pasajeros:")
        for pasajero in self.pasajeros:
            print(f"{pasajero.nombre}")

    def demorar(self, minutos):
        self.duracion += minutos

    def agregar_pasajero(self, p):
        self.pasajeros.append(p)
        p.id_vuelo = self.id


class Pasajero:

    def __init__(self, nombre):
        self.nombre = nombre


def main():

    # Crear vuelo.
    v1 = Vuelo(origen="New York", destino="Paris", duracion=540)

    # Crear pasajeros.
    alice = Pasajero(nombre="Alice")
    bob = Pasajero(nombre="Bob")

    # Agregar pasajeros.
    v1.agregar_pasajero(alice)
    v1.agregar_pasajero(bob)

    v1.imprimir_informacion()


if __name__ == "__main__":
    main()
