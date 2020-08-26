# -*- coding: utf-8 -*-
#Programa que determina si un número es primo

def is_prime(number):

    if (number < 2):  #El único número entero menor que 2 es 1 y 1 no es primo.
        return False

    elif(number == 2): #El 2 es primo
        return True

    elif(number > 2 and number % 2 == 0): #Cualquier número mayor que 2 que sea divisible entre 2 no es primo (porque es par)
        return False

    else:
        for i in range(3, number): #le sacamos mod(residuo) a la división de nuestro número por todos los enteros mayores que 2 hasta llegar al anterior a él mismo, si alguno es divisible tampoco es primo.
            if number % i == 0:
                return False
            
    return True #si no es divisible por ninguno a partir de 3, excepto el mismo entonces es primo


def run(): #la función principal recibe el número a evaluar como primo
    number = int(input('Escribe un número: '))
    result = is_prime(number)

    if result is True:
        print('El número es primo. ')

    else:
        print('El número no es primo. ')


if __name__ == '__main__': #Esto determina en cual archivo inicia el program
    run()