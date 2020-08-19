
import requests
from bs4 import BeautifulSoup

def main():
    print(" Programado Por Parker \n")

    ip = raw_input("IP o enter para saber su localizacion: ")
    cabeceras = {"User-Agent" : "Edge"}
    a = requests.get("https://es.geoipview.com/?q={}&x=0&y=0".format(ip),headers = cabeceras)
    if a.status_code == 200:

        soup = BeautifulSoup(a.text, "html.parser")
        pais = soup.find(id="ipinfo_show")
        eti1 = pais.find_all("td")
        for eti2 in eti1:
            print(eti2.string)

    else:
        ("Error de conexion...")



if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print(chr(27)+"[1;33m""Proceso detenido por el usuario")
        exit()
