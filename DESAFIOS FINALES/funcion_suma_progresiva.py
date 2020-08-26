"""
@author Omar Andrés Narváez Ortega
@linkedin: https://www.linkedin.com/in/omar-andr%C3%A9s-narv%C3%A1ez-ortega-6b3868107/
@github: https://github.com/omarn8911

Python version: 3.x 
"""


# -*- coding: utf-8 -*-
#Función que suma progresivamente

def suma_progresiva(final):
	suma = 0

	for i in range(1, final+1):
		suma = suma + i

	return suma


def run():
	print("Esta función suma progresivamente empezando en (1)")
	final = int(input("Inserte el número con el que quiere finalizar la suma:"))
	
	if final >0:
		resultado = suma_progresiva(final)
		print("El resultado de tu suma progresiva es: "+str(resultado))
	else:
		print("Debe insertar un número positivo, para poder sumar progresivamente! \n")
		run()


if __name__ == '__main__':
	print('B I E N V E N I D O  A  S U M A P R O G R E S I V A \n')
	run()