# -*- coding: utf-8 -*-

def palindrome (word):
	reversed_letters = []

	for letter in word:
		reversed_letters.insert(0, letter) #por cada letra en word insertamos esa misma letra en el indice 0.

	reversed_word = ''.join(reversed_letters) # generamos un string vacío y con el join le mandamos la secuencia que acabamos de construir

	if reversed_word == word: #validamos si la palabra al revés es igual a la palabra al derecho

		return True

	return False #Si no se cumplió la validación devuelve falso

if __name__ == '__main__': #Inicio del programa - aquí arranca mi código
	word = str(input("Escribe una palabra: "))

	result = palindrome(word) #llamando la función que comprueba el palíndromo y asignandosela al resultado

	if result is True:
		print ("{} Sí es un palíndromo.".format(word)) #la función "format" llena los espacios que quedan en la concatenación 
	else: 
		print("{} No es un palíndromo.".format(word))