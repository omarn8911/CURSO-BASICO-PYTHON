# -*- coding: utf-8 -*-

## Calculadora que conviete pesos mexicanos a pesos colombianos o a dólares. 
#Esta versión de la calculadora si tiene validaciones al escoger la moneda y así no falla si pone un valor inválido.

def foreign_exchange_calculator(ammount, moneda):  #Función que hace la conversión de moneda mexicana a otras divisas ($ Col, USD$ )
    mex_to_col_rate = 145.97  # Se asigna tasa de cambio peso mexicano a peso colombiano
    mex_to_usa_rate = 0.045   # Se asgina tasa de cambio peso mexicano a dólares 

    # A continuación se valida que moneda escogió
    if (moneda == 1):  
        ammount = mex_to_col_rate * ammount
        return ammount

    elif (moneda == 2):

        ammount = mex_to_usa_rate * ammount
        return ammount

    else:  #Esto se pone por si escogió un valor de moneda incorrecto, aunque realmente en la ejecución del menú de opciones de moneda ya se ha prevalidado y no es necesario, pero lo pongo por segurdiad "just in case"

        return moneda #regresa el valor de la moneda escogida en el menú (just in case)

def run (): #se define la función run que es la que inicia el programa
    print ('CALCULADORA DE DE DIVISAS')
    print('Convierte pesos mexicanos a pesos cololombianos o a dólares')
    print('')

    moneda = int(input('Si quieres convertir a pesos colombianos ingresa 1, si quieres convertir a dólares ingresa 2: '))

    if (moneda <= 2): #aquí se valida que las opción de moneda escogida sea correcta
        ammount = float(input('Ingresa la cantidad de pesos mexicanos que quieres convertir: '))

        result = foreign_exchange_calculator(ammount, moneda)

        if (moneda == 1):
        
            print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))
            print('')
    
        elif (moneda == 2):
            print('${} pesos mexicanos son ${} dólares'.format(ammount,result))
            print('')

    else: #Si no pone un valor de moneda correcto lo devuelve al principio del programa
        print('Valor de moneda inválido, por favor intente de nuevo')
        print('')
        print('')
        run()


if __name__ == '__main__':
    run()