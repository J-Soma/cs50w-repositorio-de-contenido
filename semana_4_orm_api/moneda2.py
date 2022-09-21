import requests
import os

def main():
    base = input("Primer moneda: ")
    otra = input("Segunda moneda: ")
    respuesta = requests.get(f"https://api.apilayer.com/fixer/latest?symbols={otra}&base={base}",
                       headers={"apikey": os.getenv("API_KEY")})
    if respuesta.status_code != 200:
        raise Exception("ERROR:Consulta de API no exitosa.")
    datos = respuesta.json()
    tasa = datos["rates"][otra]
    print(f"1 {base} es igual a {tasa} {otra}")

if __name__ == "__main__":
    main()
