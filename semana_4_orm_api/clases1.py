class Vuelo:

    def __init__(self, origen, destino, duracion):
        self.origen = origen
        self.destino = destino
        self.duracion = duracion


def main():

    # Crear vuelo.
    v = Vuelo(origen="New York", destino="Paris", duracion=540)

    # Cambiar el valor de la variable
    v.duracion += 10

    # Imprimir detalles del vuelo.
    print(v.origen)
    print(v.destino)
    print(v.duracion)

if __name__ == "__main__":
    main()
