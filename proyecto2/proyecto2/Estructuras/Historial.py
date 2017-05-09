import time
class Nodo:
	def __init__(self):
		self.Historial=""
		self.siguiente=None


	def __str__(self):
		return str(self.carga)

	def getHistorial(self):
		return self.Historial

	def setHistorial(self,Historial):
		self.Historial=Historial

	def getSiguiente(self):
		return self.siguiente

	def setSiguiente(self,siguiente):
		self.siguiente=siguiente



class Historial:
	def __init__(self):
		self.inicio=None
		self.tamanio=0

	def nueva(self):
		self.inicio=None
		self.tamanio=0

	def esVacio(self):
		return self.inicio==None

	def getTamanio(self):
		return self.tamanio


	def agregarFinal(self,Historial):
		nuevo= Nodo()
		nuevo.setHistorial(Historial)
		if self.esVacio():
			self.inicio=nuevo
		else:
			aux = self.inicio
			while aux.getSiguiente() != None:
				aux = aux.getSiguiente()
			aux.setSiguiente(nuevo)
		self.tamanio+=1



	def listar(self):
		if self.esVacio() != True:
			aux = self.inicio
			i = 0
			mostrar=""
			while aux!=None:
				mostrar = mostrar + aux.getHistorial() + "\n"
				aux=aux.getSiguiente()
				i+=1
		return mostrar


	def getInicio(self):
		return self.inicio

