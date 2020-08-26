# -*- coding: utf-8 -*-
#Ejercicio sencillo con la clase lámpara

def protected(func_parameter): #función que recibe otra función
	
	def wrapper(password): #declaramos otra función interna que si recibe la contraseña

		if password == 'platzi':
			return func_parameter() #regreso la funcion parámetro osea protected_func que muestra el mensaje de contraseña correcta

		else:
			print("La contraseña no es correcta. ")

	return wrapper # estoy devolviendo la función interior para que se ejecute lo anterior cuando llamo a @protected

@protected #decoramos la funcion protected_func encapsulando la complejidad de la funcion protected
def protected_func():
	print("Tu contraseña es correcta. ")




if __name__ == '__main__':
	password = str(input("Escribe la contraseña: "))

	protected_func(password) #ejectuto mi función decorada
	

