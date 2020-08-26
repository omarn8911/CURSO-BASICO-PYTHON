# -*- coding: utf-8 -*-

def run():

	while running == True:

	    word = str(raw_input('Escribe una palabra: '))
	    if(word == word[::-1]):  #Recorre la palabra como vector a la inversa
	        print('La palabra es un palindromo')
	    else:
	        print('La palabra NO es un palindromo')

	     running = bool(input('¿Deseas validar otra palabra? '))
	     if  

if __name__ == '__main__': #start, inicio del programa.
    run()