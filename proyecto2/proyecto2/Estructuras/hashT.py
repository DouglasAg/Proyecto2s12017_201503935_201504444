#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

class THash:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return "[Nombre: %s ---- ID: %i]" % (self.nombre,self.id,)
TablaHash1 = list()
class HashMap:
	def __init__(self):
		self.size = 6
		self.map = [None] * self.size
		
	def _get_hash(self,key):
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash % self.size
		
	def add(self, key, value):
		key_hash = self._get_hash(key)
		key_value = [key, value]
		
		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True
		else:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] = value
					return True
			self.map[key_hash].append(key_value)
			return True
	
	def get(self, key):
		key_hash = self._get_hash(key)
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None
	
	def delete(self, key):
		key_hash = self._get_hash(key)
		
		if self.map[key_hash] is None:
			return False
		for i in range (0, len(self.map[key_hash])):
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return True
	
	def print(self):
		print('----------------------------------------------------> TABLA HASH <----------------------------------------------------')
		for item in self.map:
			if item is not None:
				print(str(item))
	
h= HashMap()


conador = 0
xs=[]
xs2=[]
xsOrN=[]
xsOrI=[]
TT = 0
indice =0
def menu():
	
	print("")
	print("")
	print ("Seleccione Una Opción:")
	print("")
	print ("\t1 - Ingresar Datos")
	print("")
	print ("\t2 - Mostrar Tabla Hash")
	print("")
	print ("\t3 - Buscar Elemento")
	print("")
	print ("\t5 - salir")
	print("")
	print("")
 
 
while True:
	menu()
	opcionMenu = input("Elegir una Opcion >> ")
	print("")
	
	if opcionMenu=="1":
		
		t = input("Ingrese un Elemento: ")
		c=""
		p=0
		primero = ""
		segundo = ""
		id = 0
		suma = 0
		
		for i in t:
			d = ord(f"{i}")
			### Letra entrante y Codigo
			#print(f"Entra una {i}")
			#print(d)
			c+=str(d)
		for i in c:
			p = p+1
			#print(str(p))
			segundo +=str(i)
			if p==int(3):
				primero = segundo
				segundo = ""
			if (p==int(6))|(p==int(9))|(p==int(12))|(p==int(15))|(p==int(18))|(p==int(21))|(p==int(24))|(p==int(26))|(p==int(30))|(p==int(33))|(p==int(36))|(p==int(39))|(p==int(42))|(p==int(45))|(p==int(48))|(p==int(51))|(p==int(54))|(p==int(57))|(p==int(60))|(p==int(63))|(p==int(66))|(p==int(69))|(p==int(72))|(p==int(75))|(p==int(78))|(p==int(81))|(p==int(84))|(p==int(87))|(p==int(90))|(p==int(93))|(p==int(96))|(p==int(99)):				
				#print("------- Posicion TRES -----> "+str(p)+" numero: "+ str(i))
				suma = int(primero) + int(segundo) 
				#print("suma: ")
				#print(suma)
				primero = suma
				segundo = ""
		try:
			suma = int(primero) + int(segundo)
			##print(suma)
		except ValueError:
			print("")
		Ssuma = str(suma)
		cantidadensuma = 0
		pp=0
		terceros = ""
		cuartos = ""
		suma2 = ""
		#print(suma)
		for i in Ssuma:
			cantidadensuma = cantidadensuma +1
			#print(cantidadensuma)
		if (cantidadensuma==int(4))|(cantidadensuma==int(5)|(cantidadensuma==int(6))|(cantidadensuma==int(7))|(cantidadensuma==int(8))):			
			suma=""
			for i in Ssuma:
				pp = pp+1
				#print(pp)
				cuartos +=str(i)				
				if pp==int(1):
					terceros = cuartos
					cuartos = ""
		try:			
			suma = int(terceros)+int(cuartos)
		except ValueError:
			print("")
		
		id = suma		
				
		conador = conador +1
		#print("Envio Nombre: "+t +" Identificador Recibido: "+ id + "\t\t\t")
		print("\tEnvio Palabra: "+str(t))
		print("\tRecibio Id: " + str(id))
		#################h.add(t,id)
		xs.append(t)
		xs2.append(id)
		print(" ")
		print("Vista Segun Se ingresan:\n")
		print(xs)
		print(xs2)
		TablaHash1.append(THash(id,t))
		#h.print()
		print(" ")
		
	elif opcionMenu=="2":
		print(" ")
		print(" ")
		TablaHash1.sort(key=lambda THash: THash.id)
		print ("-----------> TablaHash <---------")
		for i in TablaHash1:
			print (str(indice)+". "+str(i))
			indice+=1
		print(" ")
		print(" ")
	
	elif opcionMenu=="3":
		xsOrN = sorted(xs)
		xsOrI = sorted(xs2)
		#print(308 in xs2)
		print("Sabe el nombre? (si/no)")
		venga = input()
		print("Sabe ID? (si/no)")
		venga2 = input()
		if venga == "si":
			print("Escriba El nombre: ")
			nombreE = input()
			if (str(nombreE) in xs) == True:
				valor = 0
				valor = int(xs.index(nombreE))
				idd = 0
				idd = int(xs2[valor])
				valor2 = 0
				valor2 = int(xsOrI.index(idd))
				print("")
				print("      ___________________________________________________________________________________________")
				print("     [El Nombre ~"+nombreE +"~ Esta ingresado en la TablaHash con ID ~"+ str(xs2[valor]) +"~ En Posicion ~"+ str(valor2)+"~}")
				print("      -------------------------------------------------------------------------------------------")
				print("")
				
			else:
				print("")
				print("               __________________________________________________________")
				print("               [El Nombre "+nombreE +" No Esta ingresado en la TablaHash }")
				print("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				print("")
		else:
			if venga2 == "si":
				print("Escriba El ID: ")
				IDE = input()
				if (int(IDE) in xs2) == True:
					#xs elemento
					#xs2 id
					valorG = 0
					valorG = int(xs2.index(int(IDE)))
					#print(valorG)
					iddG = 0
					iddG = int(xs2[valorG])
					#print(iddG)
					valor2G = 0
					valor2G = int(xsOrI.index(iddG))
					print("")
					print("      __________________________________________________________________________________")
					print("     [El ID ~"+IDE +"~ Esta ingresado en la TablaHash con Nombre ~"+str(xs[valorG])+"~ En Posicion ~"+str(valor2G)+"~}")
					print("      ----------------------------------------------------------------------------------")
					print("")
				else:
					print("")
					print("               __________________________________________________")
					print("               [El ID "+IDE +" No Esta ingresado en la TablaHash }")
					print("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
					print("")
			else:
				print(" ")
				print("NO LE PODEMOS AYUDAR")
				print(" ")
	elif opcionMenu=="5":
		break
	else:
		print ("")
		input("Ingrese correctamente la opcion\npulsa una tecla para continuar")

