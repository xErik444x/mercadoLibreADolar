import requests
from urllib.request import urlopen, Request
import sys
from bs4 import BeautifulSoup
from termcolor import colored, cprint



dolar = ""
urlApiDolar = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
r = requests.get(urlApiDolar)
dolarHoy = r.json()[0]["casa"]["compra"]
dolar = float(str(dolarHoy).replace(",","."))
print(colored("----- Dolar Hoy -----".center(30), 'blue'))
print(colored(dolarHoy.center(30), 'yellow'))
print(colored("----- Provided by dolarsi.com -----".center(20), 'blue'))

#establezco un header para hacerlo pasar como si fuera un usuario normal
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}

def calcular(url1):
    req = Request(url=url1, headers=headers) 
    datos = urlopen(req).read()
    soup = BeautifulSoup(datos, 'html.parser')

    titulo = (soup.title.string.split('-'))[0]

    urlImagen = soup.find_all("img", class_="ui-pdp-image ui-pdp-gallery__figure__image")[0]["src"] 

    precio = soup.find_all("span", class_="price-tag-fraction")
    precio = str(precio).split(">")[1].split("<")[0]
    precio = precio.replace(".","")
    precio = int(precio)

    precioDolar = round(float(precio) / float(dolar),2)
    
    valores = {"dolar":dolar,"titulo":titulo,"precio":precio,"precioDolar":precioDolar,"img":urlImagen,"oferta":"NO"}
    return(valores)


def verificarURL(url2):
    print(url2)
    print("--"*30)
    print(url2.split("https://articulo.mercadolibre.com.ar/"))
    if len(url2.split("https://articulo.mercadolibre.com.ar/")) > 1:
        return True
    else:
        return False