# -*- coding: utf-8 -*-
#Proyecto de una agenda de contactos
import csv #libreria para trabajar con CSV's

class Contact:
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

class ContactBook:

	def __init__(self):
		self._contacts = [] #el constructor inicializa con una lista vacía

	def add(self, name, phone, email):
		contact = Contact(name, phone, email)
		self._contacts.append(contact)  #agregando nuevo contacto a la lista de contactos
		self._save() #guardando en disco

	def show_all(self):
		for contact in self._contacts:
			self._print_contact(contact) #llamamos al método privado para que imprima cada uno de los contactos

	def _print_contact(self, contact): #método privado que imprime contactos
		print('--- * --- * --- * --- * --- * --- * --- * ---')
		print('Nombre: {}'.format(contact.name))
		print('Teléfono: {}'.format(contact.phone))
		print('Email: {}'.format(contact.email))
		print('--- * --- * --- * --- * --- * --- * --- * ---')

	def delete(self, name):
		for idx, contact in enumerate(self._contacts): #enummerate nos da el índice (idx ) además del elemento
			if contact.name.lower() == name.lower():
				del self._contacts[idx] #el índice lo usamos para decir cual vamos a borar con más exactitud
				self._save() #guardando cambios en disco

	def search(self, name):
		for contact in self._contacts:
			if contact.name.lower() == name.lower():
				self._print_contact(contact)
				break
		else:                 #este else pertecnece al for, se ejecuta cuando el ciclo se completa sin haber ejecutado ninguna instrucción
			self._not_found()

	def update(self, name):
		for idx, contact in enumerate(self._contacts):

			if contact.name == name:
				contact.name = str(input('Ingrese un nuevo nombre: '))
				contact.tel = str(input('Ingrese un nuevo tel: '))
				contact.email = str(input('Ingrese un nuevo email: '))
				self._contacts[idx] = contact
				self._save()
				break

		else:
			self._not_found()

	def _save(self):   #método que guarda los contactos en disco
		with open("contacts.csv", "w") as f:
			writer = csv.writer(f)
			writer.writerow( ("name", "phone", "email"))

			for contact in self._contacts:
				writer.writerow((contact.name, contact.phone, contact.email))


	def _not_found(self):
		print("*********")
		print("!!Contacto no encontrado!!")
		print('*********')



def run():

	contact_book = ContactBook()

	with open('contacts.csv', "rt", encoding="utf8") as f:  #este procedimiento lee el archivo CSV previamente guardado (si existe)
		reader = csv.reader(f)
		for idx, row in enumerate(reader):
			if idx == 0:
				continue
			if row == []:
				continue

			contact_book.add(row[0], row[1], row[2])



	while True:

		command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

		if command == 'a':

			name = str(input("Escribe el nombre del contacto: "))
			phone = str(input("Escribe el número de telefono de contacto: "))
			email = str(input("Escribe el email del contacto: "))

			contact_book.add(name, phone, email)

		elif command == 'ac':
			name = str(input("Escriba el nombre del contacto a editar: "))
			contact_book.update(name)

		elif command == 'b':
			name = str(input("Escriba el nombre del contacto a editar: "))
			contact_book.search(name)

		elif command == 'e':
			name = str(input("Por favor escriba el nombre del contacto a eliminar: "))

			contact_book.delete(name)

		elif command == 'l':
			
			contact_book.show_all()

		elif command == 's':
			break
		else:
			print('Comando no encontrado.')


if __name__ == '__main__':
	print('B I E N V E N I D O  A  L A  A G E N D A')
	run()
