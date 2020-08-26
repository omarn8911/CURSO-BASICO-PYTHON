# -*- coding: utf-8 -*-
import binascii #importamos librería para convertir a binarios
import re #importamos librería para usar expresiones regulares


def cypher(message):
    encoding='utf-8'
    errors='surrogatepass'
    bits = bin(int(binascii.hexlify(message.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def decipher(message):
    encoding='utf-8'
    errors='surrogatepass'
    n = int(message, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografí­a. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje tu cifrado: '))
            if re.match('^[0-9]*$', message):
                decypher_message = decipher(message)
                print(decypher_message)
            else:
                print("Formato no válido, por favor ingrese un mensaje cifrado en binario. \n")
                message = ''
                run()

        elif command == 's':
            return False
        else:
            print('Â¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()