# -*- coding: utf-8 -*-
#Script que descarga imagenes de la web https://xkcd.com/ y las guarda en el directorio local
import requests #libreria para enviar solicitudes y recibir informacion en jsons
from bs4 import BeautifulSoup #parsear el texto HTML y poder modificarlo y acceder a él como un árbol
import urllib.request #para guardar las imagenes de forma sencilla 


def run():

	for i in range(1, 6):
		response = requests.get('https://xkcd.com/{}'.format(i)) #url mas el número en el que va
		soup = BeautifulSoup(response.content, 'html.parser') # parseando documento, instanciando la clase BeautifulSoup
		image_container = soup.find(id='comic') #el id que esta en el div de la imagen

		image_url = image_container.find('img') ['src'] #etiqueta imagen (img) y atributo source (src)
		image_name = image_url.split('/') [-1] #el nombre de la imagen es el último elemento de la url despyués de /
		print("Descargando la imagen {}".format(image_name))
		urllib.request.urlretrieve('https:{}'.format(image_url), image_name)


if __name__ == '__main__':
	run()

