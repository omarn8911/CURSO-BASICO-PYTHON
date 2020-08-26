# -*- coding: utf-8 -*-
#Ejercicio de poblaciones pro país con manejo de errores perzonalizado

def run():
	with open('numeros.txt', 'w') as f:
		for i in range(10):
			f.write(str(i))


if __name__ == '__main__':
	run()

