# -*- coding: utf-8 -*-

def factorial (number):
    if number == 0: #Si es cero (0) entonces el factorial es 1 por defecto
        return 1
    #si no es cero entonces aplicamos el factorial:
    return number * factorial(number - 1) #definimos que el factorial de un número es igual al número multiplicado por el factorial del mismo número menos(-) 1

if __name__ == '__main__': #indica el arrance del programa
    number = int(input('Escribe un número: ')) #El arranque del programa solicita un número

    result = factorial(number) #guardamos el factorial del número en una variable

    print('El factorial de ' + str(number) +' es: ' + str(result))
     