def anunciar(f):
    def empacador():
        print("A punto de ejecutar la función...")
        f()
        print("Finalizada ejecución de la función.")
    return empacador

@anunciar
def hola():
    print("Hola, mundo!")

hola()
