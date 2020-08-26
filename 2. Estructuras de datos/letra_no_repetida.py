# -*- coding: utf-8 -*-
#Encriptar mensajes usando diccionarios de Python 3

def first_not_repeating_char(char_sequence):
	seen_letters = {}

	for idx, letter in enumerate(char_sequence):
		if letter not in seen_letters:
			#si no la he visto agrego una tupla a la lista con la letra y el número 1 (de primera vez)
			seen_letters[letter] = (idx, 1) 
		else:
		#si la he visto ya entonces a la lista le agrego en la posición en la que voy la letra (vista anteriormente[0]) y el conteo [1] + 1
			seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter] [1] + 1)


	final_letters = []
	for key, value in seen_letters.items(): #recorro la lista seen_letters 
		if value[1] == 1:
			final_letters.append((key, value[0])) #y a final_letters agrego sólo las que están 1 sóla vez

	#usamos el método sorted para ordenar las letras en final_letters, 
	#recibimos el valor desde final_letters usando función tipo lambda, de acuerdo al índice en el que se encontraron "value[1]"
	not_repeated_letters = sorted(final_letters, key = lambda value: value[1])
	
	if not_repeated_letters: #si esto tiene algo 
		return not_repeated_letters [0][0] #regresamos el primer valor

	else:
		return '_'


if __name__ == '__main__':
	
	char_sequence = str(input("Ingresa una secuencia de caracteres: "))

	result = first_not_repeating_char(char_sequence)

	if result == '_':
		print("Todos los caracteres se repiten. ")
	else:
		print("El primer caracter no repetido es: "+str(result))
	


