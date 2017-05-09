class Nodo:

    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.clave = ""
        self.siguiente = None
        self.anterior = None

    def getnombre(self):
        return self.nombre

    def setnombre(self, nombre):
        self.nombre = nombre

    def getapellido(self):
        return self.apellido

    def setapellido(self, apellido):
        self.apellido = apellido

    def getclave(self):
        return self.clave

    def setclave(self, clave):
        self.clave = clave

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, siguiente):
        self.siguiente = siguiente

    def getanterior(self):
        return self.anterior

    def setanterior(self, anterior):
        self.anterior = anterior


class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def getVacio(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def insertar(self, nombre, apellido, clave):
        nuevo = Nodo()
        nuevo.setnombre(nombre)
        nuevo.setapellido(apellido)
        nuevo.setclave(clave)
        if self.getVacio() == True:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

    def imprimir(self):
        datos=""
        if self.getVacio() == True:
            print("Lista vacia")
        else:
            validar = True
            temp =  self.primero
            while(validar):
                datos=datos+ temp.nombre + "\n"
                if temp == self.ultimo:
                    validar = False
                else:
                    temp = temp.siguiente
        return datos

    def cuerpo(self):
        aux = self.primero
        cuerpo = ""
        while aux is not None:
            if aux.siguiente is not None:
                cuerpo = cuerpo + '"'+aux.nombre+'" -> '+ '"'+aux.siguiente.nombre+'";\n'
                cuerpo = cuerpo + '"'+aux.siguiente.nombre+'" -> '+ '"'+aux.nombre+'";\n'
            else:
                cuerpo = cuerpo + '"'+aux.nombre+'";\n'
            if aux.siguiente is not None:
                aux = aux.siguiente
            else:
                break
        cuerpo = cuerpo 

        return cuerpo                

    def iniciar(self, nombre, clave):
        bien = False
        if self.getVacio() == True:
            print("Lista vacia")
        else:
            validar = True
            temp =  self.primero
            while(validar):
                if temp.nombre == nombre and temp.clave == clave:
                    bien = True
                    return bien
                if temp == self.ultimo:
                    validar = False
                else:
                    temp = temp.siguiente
        return bien