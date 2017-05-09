from proyecto2.Estructuras import ArbolB

class Nodo:

    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.clave = ""
        self.siguiente = None
        self.anterior = None
        self.arbol = ArbolB.ArbolB()

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

    def nuevacarpeta(self, usuario, nombre):
        if self.getVacio() == True:
            print("Lista vacia")
        else:
            validar = True
            temp =  self.primero
            while(validar):
                if temp == self.ultimo or temp.nombre == usuario:
                    validar = False
                else:
                    temp = temp.siguiente
            if validar == False:

                ar = temp.arbol.insertar(nombre)

        return "Si"

    def getarbol(self, usuario):
        if self.getVacio() == True:
            print("Lista vacia")
            return False
        else:

            validar = True
            temp =  self.primero
            while(validar):
                if temp == self.ultimo or temp.nombre == usuario:
                    validar = False
                else:
                    temp = temp.siguiente
            if validar == False:

                ar = temp.arbol

            return ar

    def getotroarbol(self, raiz, salida):
        regresar = None
        if raiz != None:               
            salida2 = raiz.liss()
            a = ""
            if len(salida) > 0:
                a = salida.pop(0)
            for x in salida2:
                if x.clave == a:
                    regresar = x.carpetas
                    break
            if len(salida) > 0:
                return self.getotroarbol(regresar, salida)
            else:
                return regresar

    def archivo(self, ruta):
        infile = open(ruta, 'rb')
        lista = ruta.split("\\")
        x = len(lista) - 1
        nombre = lista[x]
        lista2 = nombre.split(".")
        extension = lista2[1]
        buffer = infile.read()
        size = len(buffer)/1000000
        archivo = Archivos.Archivo(nombre, extension, infile)
        archivo.size = size
        return archivo