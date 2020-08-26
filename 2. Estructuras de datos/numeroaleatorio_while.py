# -*- coding: utf-8 -*-

import random #librería para hacer aleatorios

def run():
	
	number_found = False #iniacializa variable de número encontrado en falso
	print("Bienvenido al juego del número aleatorio!")
	print("")
	
	max_random = int(input("Inserte el número máximo para su rángo aleatorio (debe ser positivo): "))
	
	if max_random > 0:	
		random_number = random.randint(0, max_random) #asigna un numero aleatorio entre 0 y 20
		
		while not number_found: #este while se va a ejecutar hasta que encontremos el número aleatorio.
			number = int(input("Intenta un número: "))

			if number == random_number:
				print("Felicidades, econtraste el número\n")
				play_again = int(input("(1) Jugar de nuevo, (2) para finalizar: "))

				if play_again == 2:
					break
				else:
					number_found=True #Seteo en True antes de ejecutar de nuevo 
									  #la función ya que si lo dejo false, 
									  #al enviarle False de nuevo en el inicio 
									  #de la función False + False = True, lo que perjudicaría la lógica del While.
					run() 

			elif number > random_number:
				print("El número oculto es más pequeño, inténtalo de nuevo")
		
			else: 
				print("El número oculto es más grande, inténtalo de nuevo.")
	
	else:
		print("El máximo para su rango aleatorio debe ser positivo! \n")
		run()


if __name__ == '__main__': #Inicio del programa - aquí arranca mi código
	run()


	