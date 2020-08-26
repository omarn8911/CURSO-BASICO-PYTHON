	# -*- coding: utf-8 -*-
	#Encriptar mensajes usando diccionarios de Python 3

	KEYS = {
	    'a': 'w',
	    'b': 'E',
	    'c': 'x',
	    'd': '1',
	    'e': 'a',
	    'f': 't',
	    'g': '0',
	    'h': 'C',
	    'i': 'b',
	    'j': '!',
	    'k': 'z',
	    'l': '8',
	    'm': 'M',
	    'n': 'I',
	    'o': 'd',
	    'p': '.',
	    'q': 'U',
	    'r': 'Y',
	    's': 'i',
	    't': '3',
	    'u': ',',
	    'v': 'J',
	    'w': 'N',
	    'x': 'f',
	    'y': 'm',
	    'z': 'W',
	    'A': 'G',
	    'B': 'S',
	    'C': 'j',
	    'D': 'n',
	    'E': 's',
	    'F': 'Q',
	    'G': 'o',
	    'H': 'e',
	    'I': 'u',
	    'J': 'g',
	    'K': '2',
	    'L': '9',
	    'M': 'A',
	    'N': '5',
	    'O': '4',
	    'P': '?',
	    'Q': 'c',
	    'R': 'r',
	    'S': 'O',
	    'T': 'P',
	    'U': 'h',
	    'V': '6',
	    'W': 'q',
	    'X': 'H',
	    'Y': 'R',
	    'Z': 'l',
	    '0': 'k',
	    '1': '7',
	    '2': 'X',
	    '3': 'L',
	    '4': 'p',
	    '5': 'v',
	    '6': 'T',
	    '7': 'V',
	    '8': 'y',
	    '9': 'K',
	    '.': 'Z', 
	    ',': 'D',
	    '?': 'F',
	    '!': 'B',
	    ' ': '&'
	}

	def cypher(message):
		words = message.split(' ') #Toma el mensaje y lo guarda palabra por palabra en una lista
		cypher_message = []

		for word in words:
			cypher_word = ''
			for letter in word:
				cypher_word += KEYS[letter] #cifra cada letra de cada palabra

			cypher_message.append(cypher_word) #agrega cada palabra al mensaje cifrado final

		return ' '.join(cypher_message) #volvemos a juntar cada palabra cifrada en un solo string

	def decypher(message):
		words = message.split(' ')
		decypher_message = []

		for word in words:
			decypher_word = ''

			for letter in word:

				for key, value in KEYS.items(): #iteramos en toda la lista
					if value == letter:
						decypher_word += key #y deciframos solo la que encontramos

			decypher_message.append(decypher_word)

		return	' '.join(decypher_message)


	def run():
	    while True:

	        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

	            Bienvenido a criptografía. ¿Qué deseas hacer?

	            [c]ifrar mensaje
	            [d]ecifrar mensaje
	            [s]alir
	        '''))

	        if command == 'c':
	        	message = str(input("Escribe tu mensaje: "))
	        	cypher_message = cypher(message)
	        	print(cypher_message)

	        elif command == 'd':
	        	message = str(input("Escribe tu mensaje cifrado: "))
	        	decypher_message = decypher(message)
	        	print(decypher_message)

	        elif command == 's':
	        	break


	if __name__ == '__main__':
			print("M E N S A J E S  C I F R A D O S")
			run()

