# -*- coding: utf-8 -*-
#Ejercicio de poblaciones pro país con manejo de errores perzonalizado


def run():
	counter = 0
	with open('aleph.txt', encoding='utf-8') as f:
			#la siguiente linea convierte el archivo en una lista que contiene cada línea como elemento (String) de la lista
			#print(f.readlines()) 

			for line in f: 
				counter += line.count("Beatriz") #suma uno cada vez que encuentre Beatriz

	print("Beatriz se encuentra {} veces en el texto ".format(counter))


	


if __name__ == '__main__':
	run()
