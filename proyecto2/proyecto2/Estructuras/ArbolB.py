from proyecto2.Estructuras import ArbolAVL


class Nodo:
	def __init__(self, clave):
		self.clave = clave
		self.avl = ArbolAVL.ArbolAvl()
		self.carpetas = ArbolB()


class Clave:
	def __init__(self, clave):
		self.Ramas = [Clave]*5
		self.Claves  = [Nodo]*4
		self.Cuenta = 0
		self.Claves[0] = clave

	def buscar(self, clave):
		hola = None
		for x in range(0, self.Cuenta):
			if self.Claves[x].clave == calve:
				hola = self.Claves[x].carpetas
				return  hola
		return hola


class ArbolB:

	def __init__(self):
		self.p = Clave(None)
		self.Xder = Clave(None)
		self.Xizq = Clave(None)
		self.encontrado = ArbolB
		self.X = None
		self.Xr = None
		self.salida = list()
		self.imps = ""
		self.EmpA = False
		self.Esta = False


	def insertar(self, clave):
		nuevacla = Nodo(clave)
		self.insertar2(nuevacla, self.p)

	def insertar2(self, clave, raiz):
		self.Empujar(clave, raiz)
		if  self.EmpA:
			self.p = Clave(None)
			self.p.Cuenta = 1
			self.p.Claves[0] = self.X
			self.p.Ramas[0] = raiz
			self.p.Ramas[1] = self.Xr
			self.EmpA = False
			print("insertado")


	def Empujar(self, clave, raiz):
		k = 0
		self.Esta = False
		if  self.Vacio(raiz):
			self.EmpA = True
			self.X = clave
			self.Xr = None
		else:
			k = self.BuscarNodo(clave, raiz)
			if self.Esta:
				print("No claves repetidas")
				self.EmpA = False
			else:
				self.Empujar(clave, raiz.Ramas[k])
				if self.EmpA:
					if raiz.Cuenta < 4:
						self.EmpA = False
						self.MeterHoja(self.X, raiz, k)
					else:
						self.EmpA = True
						self.DividirN(self.X, raiz, k)



	def MeterHoja(self, clave, raiz, k):
		i = raiz.Cuenta
		while i != k:
			raiz.Claves[i] = raiz.Claves[i-1]
			raiz.Ramas[i+1] = raiz.Ramas[i]
			i = i-1
		raiz.Claves[k] = clave
		raiz.Ramas[k+1] = self.Xr
		raiz.Cuenta = raiz.Cuenta + 1

	def DividirN(self, clave, Raiz, k):
		pos = 0
		Posmda = 0
		if k <= 2:
			Posmda = 2
		else:
			Posmda = 3
		Mder = Clave(None)
		pos = Posmda + 1
		while pos != 5:
			Mder.Claves[pos - Posmda - 1] = Raiz.Claves[pos - 1]
			Mder.Ramas[pos - Posmda] = Raiz.Ramas[pos]
			pos = pos + 1 
		Mder.Cuenta = 4 - Posmda
		Raiz.Cuenta = Posmda
		if k <= 2:
			self.MeterHoja(clave, Mder, k)
		else:
			self.MeterHoja(clave, Mder, k - Posmda)
		self.X = Raiz.Claves[Raiz.Cuenta - 1]
		Mder.Ramas[0] =  Raiz.Ramas[Raiz.Cuenta]
		Raiz.Cuenta = Raiz.Cuenta - 1
		self.Xr = Mder

	def eliminar(self, clave):
		if self.Vacio(self.p):
			print("No elementos")
		else:
			self.eliminar2(self.p, clave)

	def eliminar2(self, Raiz, clave):
		try:
			self.EliminarRegistro(Raiz, clave)
		except Exception as e:
			self.Esta = False
		
		if self.Esta:
			if Raiz.Cuenta == 0:
				Raiz = Raiz.Ramas[0]
			self.p = Raiz
			print("fin eliminacion")
		else:
			print("no se encontro el elemento")

	def EliminarRegistro(self, raiz, c):
		pos = 0
		if self.Vacio(raiz):
			self.Esta = False
		else:
			pos = self.BuscarNodo(c, raiz)
			if self.Esta:
				if self.Vacio(raiz.Ramas[pos - 1]):
					self.Quitar(raiz, pos)
				else:
					self.Sucesor(raiz, pos)
					self.EliminarRegistro(raiz.Ramas[pos, raiz.Claves[pos - 1]])
			else:
				self.EliminarRegistro(raiz.Ramas[pos], c)
				if raiz.Ramas[pos] != None and raiz.Ramas[pos].Cuenta < 2:
					self.Restablecer(raiz, pos)

	def Sucesor(self, raiz, k):
		q = raiz.Ramas[k]
		while not self.Vacio(q.Ramas[0]):
			q = q.Ramas[0]
		raiz.Claves[k - 1] = q.Claves[0]

	def Combina(self, raiz, pos):
		self.Xder = raiz.Ramas[pos]
		self.Xizq = raiz.Ramas[pos - 1]
		self.Xizq.Cuenta = self.Xizq.Cuenta + 1
		self.Xizq.Claves[self.Xizq.Cuenta - 1] = raiz.Claves[pos - 1]
		self.Xizq.Ramas[self.Xizq.Cuenta] = self.Xder.Ramas[0]
		j = 1
		while j != self.Xder.Cuenta + 1:
			self.Xizq.Cuenta = self.Xizq.Cuenta + 1
			self.Xizq.Claves[self.Xizq.Cuenta - 1] =  self.Xder.Claves[j - 1]
			self.Xizq.Ramas[self.Xizq.Cuenta] =  self.Xder.Ramas[j]
			j = j + 1      
		self.Quitar(raiz, pos)

	def MoverDer(self, raiz, pos):
		i = raiz.Ramas[pos].Cuenta
		while i != 0:
			raiz.Ramas[pos].Claves[i] = raiz.Ramas[pos].Claves[i - 1]
			raiz.Ramas[pos].Ramas[i + 1] = raiz.Ramas[pos].Ramas[i]
			i = i - 1
		raiz.Ramas[pos].Cuenta = raiz.Ramas[pos].Cuenta + 1
		raiz.Ramas[pos].Ramas[1] = raiz.Ramas[pos].Ramas[0]
		raiz.Ramas[pos].Claves[0] = raiz.Claves[pos - 1]
		raiz.Claves[pos - 1] = raiz.Ramas[pos - 1].Claves[raiz.Ramas[pos - 1].Cuenta - 1]
		raiz.Ramas[pos].Ramas[0] = raiz.Ramas[pos - 1].Ramas[raiz.Ramas[pos - 1].Cuenta]
		raiz.Ramas[pos - 1].Cuenta = raiz.Ramas[pos - 1].Cuenta - 1

	def MoverIzq(self, raiz, pos):
		raiz.Ramas[pos - 1].Cuenta = raiz.Ramas[pos - 1].Cuenta + 1
		raiz.Ramas[pos - 1].Claves[raiz.Ramas[pos - 1].Cuenta - 1] = raiz.Claves[pos - 1]
		raiz.Ramas[pos - 1].Ramas[raiz.Ramas[pos - 1].Cuenta] = raiz.Ramas[pos].Ramas[0]
		raiz.Claves[pos - 1] = raiz.Ramas[pos].Claves[0]
		raiz.Ramas[pos].Ramas[0] = raiz.Ramas[pos].Ramas[1]
		raiz.Ramas[pos].Cuenta = raiz.Ramas[pos].Cuenta - 1
		i = 1
		while i != (raiz.Ramas[pos].Cuenta + 1) :
			raiz.Ramas[pos].Claves[i - 1] = raiz.Ramas[pos].Claves[i]
			raiz.Ramas[pos].Ramas[i] = raiz.Ramas[pos].Ramas[i + 1]
			i = i + 1


	def Quitar(self, raiz, pos):
		j = pos + 1
		while j != (raiz.Cuenta + 1):
			raiz.Claves[j - 2] = raiz.Claves[j - 1]
			raiz.Ramas[j - 1] = raiz.Ramas[j]
			j = j + 1 
		raiz.Cuenta = raiz.Cuenta - 1

	def Restablecer(self, raiz, pos):
		if pos > 0:
			if raiz.Ramas[pos - 1].Cuenta > 2:
				self.MoverDer(raiz, pos)
			else:
				self.Combina(raiz, pos)
		elif raiz.Ramas[1].Cuenta > 2:
			self.MoverIzq(raiz, 1)
		else:
			self.Combina(raiz, 1)

	def Vacio(self, raiz):
		if raiz is None or raiz.Cuenta is 0:
			return True
		else:
			return False


	def BuscarNodo(self, Clave, raiz):
		j = 0
		if Clave.clave < raiz.Claves[0].clave:
			self.Esta = False
			j = 0
		else:
			j = raiz.Cuenta
			while Clave.clave < raiz.Claves[j -1].clave and j > 1:
				j = j - 1

			self.Esta = Clave.clave == raiz.Claves[j - 1].clave	
		return j
	
	def liss(self):
		self.salida.clear()
		self.lis(self.p)
		return self.salida
        

	def lis(self, raiz):
		if(raiz.Cuenta > 0) and (raiz.Ramas[0] is not None):
			self.alista(raiz)
			for x in range(1, raiz.Cuenta+1):
				if raiz.Ramas[x] is not None:
					self.alista(raiz.Ramas[x])
					self.lis(raiz.Ramas[x-1])
    
	def alista(self, raiz):
		for x in range(0, raiz.Cuenta):
			self.salida.append(raiz.Claves[x])
    
	def buscarcarpeta(self, raiz, clave):
		if(raiz.Cuenta > 0) and (raiz.Ramas[0] is not None):
			for x in range(0, raiz.Cuenta + 1):
				if raiz.Ramas[x] != None:
					if raiz.Ramas[x].buscar(clave) != None:
						self.encontrado = raiz.Ramas[x].buscar(clave)
						break
					self.buscarcarpeta(raiz.Ramas[x],clave)

