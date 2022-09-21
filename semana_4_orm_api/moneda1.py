import requests
import os

def main():
    respuesta = requests.get("https://api.apilayer.com/fixer/convert?to=EUR&from=USD&amount=1",
                headers={"apikey":os.get_env("API_KEY")})
    if respuesta.status_code != 200:
        raise Exception("ERROR: Consulta de API no exitosa.")
    datos = respuesta.json()
    tasa = datos["info"]["rate"]
    print(f"1 USD es igual a {tasa} EUR")

if __name__ == "__main__":
    main()
