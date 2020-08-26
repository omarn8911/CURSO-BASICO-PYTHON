# -*- coding: utf-8 -*-
#Este código, hace una búsqueda binaria

def binary_serach(numbers, number_to_find, low, high):

	if low > high:  # Si esto pasa es porque el número no se encuentra en la lista
		return False 

	mid = round((low + high) / 2) #redondeo porque python 3 no ignora decimales

	#si el número que está en el indice de la mitad es el que buscamos
	if numbers[mid] == number_to_find:
		return True

	#si el numero de la mitad es mayor que el que buscamos
	elif numbers[mid] > number_to_find:
	#entonces nuestro indice alto disminuye 1 y el bajo se mantiene igual
		return	binary_serach(numbers, number_to_find, low, mid -1)
	else:
		#si el numero que buscamos es mayor que la mitad
		#entocnes nuestro indice inferior aumenta 1 y el alto se mantiene
		return binary_serach(numbers, number_to_find, mid + 1, high )


	

if __name__ == '__main__':
	numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

	number_to_find = int(input("Ingresa un número: "))

	#Llamo la función mandandole como parametro, la lista, el número a buscar
	# 0 como límite inferior, y el largo de la lista -1 como superior
	result = binary_serach(numbers, number_to_find, 0, len(numbers) -1)

	if result is True:
		print("El número si está en la lista. ")
	else:
		print("El número no está en la lista. ")


