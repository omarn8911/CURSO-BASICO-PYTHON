# -*- coding: utf-8 -*-

def palindrome(word):
	reversed_word = word [::-1]

	if reversed_word == word:
		return True

	return False

if __name__ == '__main__': #Inicio del programa - aquí arranca mi código
	word = str(input("Escribe una palabra: "))

	result = palindrome(word) #llamando la función que comprueba el palíndromo y asignandosela al resultado

	if result is True:
		print ("{} Sí es un palíndromo.".format(word)) #la función "format" llena los espacios que quedan en la concatenación 
	else: 
		print("{} No es un palíndromo.".format(word))