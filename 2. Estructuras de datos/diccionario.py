# -*- coding: utf-8 -*-
#Primer ejercicio con un diccionario que contiene calificaciones y saca un promedio

calificaciones = {}
calificaciones ['algoritmos'] = 9
calificaciones ['matematicas'] = 10
calificaciones ['web'] = 8
calificaciones ['bases de datos'] = 10

for key in calificaciones: #iterando a través de las llaves
	print(key)


for value in calificaciones.values(): #iterando entre los valores
	print(value)

for key, value in calificaciones.items(): #iterando en clave, valor
	print("llave: {}, valor: {}".format(key,value))

suma_calificaciones = 0

for calificacion in calificaciones.values():
	suma_calificaciones += calificacion

promedio = suma_calificaciones / len(calificaciones.values())

print("El promedio es: "+str(promedio))