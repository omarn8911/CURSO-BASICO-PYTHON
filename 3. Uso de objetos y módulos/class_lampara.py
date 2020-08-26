# -*- coding: utf-8 -*-
#Ejercicio sencillo con la clase lámpara

class Lamp:
	"""Clase Lámpara que prende y apaga"""

	_LAMPS = ['''  #declaramos la variable de clase _LAMPS en mayúscula porque todas las instancias de la clase la
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

	def __init__(self, is_turned_on):
		self.is_turned_on = False
		self._display_image() #llamamos este método para mostrar la lámpara

	def turn_on(self): #declarando método encendido como público
		self.is_turned_on = True
		self._display_image()

	def turn_off(self):
		self.is_turned_on = False
		self._display_image()

	def _display_image(self):  #el guión aquí indica que el método es privado
		#lo hicimos privado porque no queremos que los usuarios de este lo manejen a su antojo
		if self.is_turned_on == True:
			print(self._LAMPS[0])
		else:
			print(self._LAMPS[1])


def run():
	lamp = Lamp(is_turned_on = False) #pasamos el parámetro para crear la lámpara apagada 

	while True:
		command = str(input('''
                             ¿Qué desea hacer?

                             [E]ncender.
                             [A]pagar.
                             [S]alir.
                             \n\t Eleccion: ''')).lower()

		if command == 'e':
			lamp.turn_on()
		elif command == 'a':
			lamp.turn_off()
		else:
			break

if __name__ == '__main__':
	run()


