class Vuelo:

    def __init__(self, origen, destino, duracion):
        self.origen = origen
        self.destino = destino
        self.duracion = duracion

    def imprimir_informacion(self):
        print(f"Origen del vuelo: {self.origen}")
        print(f"Destino del vuelo: {self.destino}")
        print(f"Duracion del vuelo: {self.duracion}")


def main():

    v1 = Vuelo(origen="New York", destino="Paris", duracion=540)
    v1.imprimir_informacion()

    v2 = Vuelo(origen="Tokyo", destino="Shanghai", duracion=185)
    v2.imprimir_informacion()


if __name__ == "__main__":
    main()
