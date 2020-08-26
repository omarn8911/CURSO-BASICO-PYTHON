# -*- coding: utf-8 -*-
#Ejercicio de poblaciones pro país con manejo de errores perzonalizado

countries = {
	'mexico' : 122,
	'colombia' : 49,
	'argentina' : 43,
	'chile' : 18,
	'peru' : 31,
}

while True:
	country = str(input("Escribe el nombre de un país: ")).lower() #la función agregada lower convierte todo lo que ingresen a minúsculas
	try:
		print("La población de {} es: {} millones".format(country, countries[country]))

	except KeyError:
		print("El país {} no está en nuestro listado \n".format(country))
		new_country = int(input("Escribe la población para: {} ".format(country)))
		countries[country] = new_country


 
