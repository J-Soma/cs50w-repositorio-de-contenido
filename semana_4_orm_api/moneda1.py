import requests

def main():
    respuesta = requests.get("https://api.fixer.io/latest?base=USD&symbols=EUR")
    if respuesta.status_code != 200:
        raise Exception("ERROR: Consulta de API no exitosa.")
    datos = respuesta.json()
    tasa = datos["rates"]["EUR"]
    print(f"1 USD es igual a {tasa} EUR")

if __name__ == "__main__":
    main()
