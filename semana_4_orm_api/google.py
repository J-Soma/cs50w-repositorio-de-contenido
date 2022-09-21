import requests

def main():
    respuesta = requests.get("https://www.google.com/")
    print(respuesta.text)

if __name__ == "__main__":
    main()
