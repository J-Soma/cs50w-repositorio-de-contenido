class Vuelo:

    def __init__(self, origen, destino, duracion):
        self.origen = origen
        self.destino = destino
        self.duracion = duracion

    def imprimir_informacion(self):
        print(f"Origen del vuelo: {self.origen}")
        print(f"Destino del vuelo: {self.destino}")
        print(f"Duracion del vuelo: {self.duracion}")

    def demorar(self, minutos):
        self.duracion += minutos


def main():

    v1 = Vuelo(origen="New York", destino="Paris", duracion=540)
    v1.demorar(10)
    v1.imprimir_informacion()


if __name__ == "__main__":
    main()
