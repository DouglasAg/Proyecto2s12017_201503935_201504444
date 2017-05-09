class Nodo(object):

    dato=""
    archivo=None
    izdo=None
    dcho=None

    def Nodo(self, valor, archivo):
        self.dato=valor
        self.archivo=archivo
        self.izdo=None
        self.dcho=None

    def Nodos(self, ramaIzdo, valor, ramaDcho):
        self.dato=valor
        self.izdo=ramaIzdo
        self.dcho=ramaDcho

    def valorNodo(self):
        return self.dato

    def subarbolIzdo(self):
        return self.izdo 

    def subarbolDcho(self):
        return self.dcho

    def nuevoValor(self, d):
        self.dato = d

    def ramaIzdo(self, n):
        self.izdo = n

    def ramaDcho(self, n):
        self.dcho = n


class NodoAvl(Nodo):

    fe=0

    def __init__(self, valor):
        super().Nodo(valor)
        fe=0

    def NodoAvls(self, valor, ramaIzdo, ramaDcho):
        super().Nodos(ramaIzdo, valor, ramaDcho) 
        fe=0

    def visitar(self):
        print(self.valorNodo())


class ArbolAvl:

    raiz = None
    cuerpo = ""

    def __init__(self):
        raiz = None

    def raiArbol(self):
        return self.raiz

    def rotacionII(self, n, n1):
        n.ramaIzdo(n1.subarbolDcho())
        n1.ramaDcho(n)
        # actualización de los factores de equilibrio
        if n1.fe == -1:
            n1.fe = 0
            n.fe = 0
        else:
            n.fe = -1
            n.fe = 1
        return n1

    def rotacionDD(self, n, n1):
        n.ramaDcho(n1.subarbolIzdo())
        n1.ramaIzdo(n)
        # actualización de los factores de equilibrio
        if n1.fe == 1:
            n.fe = 0
            n1.fe = 0
        else:
            n.fe = 1
            n.fe = -1
        return n1

    def rotacionID(self, n, n1):
        
        n2 = n1.subarbolDcho()
        n.ramaIzdo(n2.subarbolDcho())
        n2.ramaDcho(n)
        n1.ramaDcho(n2.subarbolIzdo())
        n2.ramaIzdo(n1)
        #actualización de los factores de equilibrio
        if n2.fe == 1:
            n1.fe = -1
        else:
            n1.fe = 0
        if n2.fe == -1:
            n.fe = 1
        else:
            n.fe = 0
            n2.fe = 0
        return n2

    def rotacionDI(self, n, n1):
        
        n2 = n1.subarbolIzdo()
        n.ramaDcho(n2.subarbolIzdo())
        n2.ramaIzdo(n)
        n1.ramaIzdo(n2.subarbolDcho())
        n2.ramaDcho(n1)
        #actualización de los factores de equilibrio
        if n2.fe == 1:
            n.fe = -1
        else:
            n.fe = 0
        if n2.fe == -1:
            n1.fe = 1
        else:
            n1.fe = 0
            n2.fe = 0
        return n2

    def insertar (self, valor):
        try:
            a=False
            h = Logical(a)
            dato = valor
            self.raiz = self.insertarAvl(self.raiz, dato, h)
        except Exception as e:
            print("no se inserto")

    def insertarAvl(self, raiz, dato, h):
        try:
            
            if raiz == None:
                raiz = NodoAvl(dato)
                h.setLogical(True)
            elif dato < raiz.valorNodo():
                
                iz = self.insertarAvl(raiz.subarbolIzdo(), dato, h)
                raiz.ramaIzdo(iz)
                #regreso por los nodos del camino de búsqueda
                if h.booleanValue():
                    #decrementa el fe por aumentar la altura de rama izquierda

                    if raiz.fe == 1:
                        raiz.fe = 0
                        h.setLogical(False)
                    else:                           
                        if raiz.fe == 0:
                            raiz.fe = -1
                        else:
                            if raiz.fe == -1:
                                n1 = raiz.subarbolIzdo()
                                if n1.fe == -1:
                                    raiz = self.rotacionII(raiz, n1)
                                else:
                                    raiz = self.rotacionID(raiz, n1)
                                h.setLogical(False)
            elif dato > raiz.valorNodo():
                dr = self.insertarAvl(raiz.subarbolDcho(), dato, h)
                raiz.ramaDcho(dr)
                # regreso por los nodos del camino de búsqueda
                if h.booleanValue():
                    #incrementa el fe por aumentar la altura de rama izquierda
                    if raiz.fe == 1:
                        n1 = raiz.subarbolDcho()
                        if n1.fe == 1:
                            raiz = self.rotacionDD(raiz, n1)
                        else:
                            raiz = self.rotacionDI(raiz, n1)
                            h.setLogical(False)
                    else:
                        if raiz.fe == 0:
                            raiz.fe = 1
                        else:
                            if raiz.fe == -1:
                                raiz.fe = 0
                                h.setLogical(False)
            else:
                print("No puede haber claves repetidas " )
            return raiz
        except Exception as e:
            print("No puede haber claves repetidas dsfdsf")


    def imprimir(self):
        print(self.raiz.valorNodo())
        print(self.raiz.subarbolIzdo().valorNodo())
        print(self.raiz.subarbolDcho().valorNodo())


    def eliminar(self, valor):
        #try:
            dato = valor
            flag = Logical(False)
            self.raiz = self.borrarAvl(self.raiz, dato, flag)
        #except Exception as e:
            #raise e

    def borrarAvl(self, r, clave, cambiaAltura):
        #try:
            if r == None:
                print("No se encontro")
            elif clave < r.valorNodo():
                iz = self.borrarAvl(r.subarbolIzdo(), clave, cambiaAltura)
                r.ramaIzdo(iz)
                if cambiaAltura.booleanValue():
                    r = self.equilibrar1(r, cambiaAltura)
            elif clave > r.valorNodo():
                dr = self.borrarAvl(r.subarbolDcho(), clave, cambiaAltura)
                r.ramaDcho(dr)
                if cambiaAltura.booleanValue():
                    r = self.equilibrar2(r, cambiaAltura)
            else: # nodo encontrado
                q = r
                if q.subarbolIzdo() == None:
                    r = q.subarbolDcho()
                    cambiaAltura.setLogical(True)
                elif q.subarbolDcho() == None:
                    r = q.subarbolIzdo()
                    cambiaAltura.setLogical(True)
                else: #tiene rama izquierda y derecha
                    iz = self.reemplazar(r, r.subarbolIzdo(), cambiaAltura)
                    r.ramaIzdo(iz)
                    if cambiaAltura.booleanValue():
                        r.equilibrar1(r, cambiaAltura)
                q = None
            return r
        #except Exception as e:
            #raise e


    def reemplazar(self, n, act, cambiaAltura):
        if act.subarbolDcho() != None:
            d = self.reemplazar(n, act.subarbolDcho(), cambiaAltura)
            act.ramaDcho(d)
            if cambiaAltura.booleanValue():
                act = self.equilibrar2(act, cambiaAltura)
        else: 
            n.nuevoValor(act.valorNodo())
            n = act
            act = act.subarbolIzdo()
            n = None
            cambiaAltura.setLogical(True)
        return act

    def equilibrar1(self, n, cambiaAltura):
        if n.fe == -1:
            n.fe = 0
        elif n.fe == 0:
            n.fe = 1
            cambiaAltura.setLogical(False)
        elif n.fe == 1:
            n1 = n.subarbolDcho()
            if n1.fe >= 0:
                if n1.fe == 0:
                    cambiaAltura.setLogical(False)
                n = self.rotacionDD(n, n1)
            else:
                n = self.rotacionDI(n, n1)
        return n

    def equilibrar2(self, n, cambiaAltura):
        if n.fe == -1:
            n1 = n.subarbolIzdo()
            if n1.fe <= 0:
                if n1.fe == 0:
                    cambiaAltura.setLogical(False)
                n = self.rotacionII(n, n1)
            else:
                n = self.rotacionDD(n, n1)
        elif n.fe == 0:
            n.fe = -1
            cambiaAltura.setLogical(False)
        elif n.fe == 1:
            n.fe = 0
        return n

    def preorden(self, r, cadena):
        if r != None:

            r.visitar()
            
            if r.subarbolIzdo() != None:  
                cadena = cadena + '"' + str(r.valorNodo()) + '" -> ' + '"' + str(r.subarbolIzdo().valorNodo()) + '";\n'          
                cadena = self.preorden(r.subarbolIzdo(), cadena)
                
            if r.subarbolDcho() != None:
                cadena = cadena + '"' + str(r.valorNodo()) + '" -> ' + '"' + str(r.subarbolDcho().valorNodo()) + '";\n'          
                cadena = self.preorden(r.subarbolDcho(), cadena)
                 
        return cadena

    def dor(self):
        print(self.cuerpo)
        return self.cuerpo


    def reset(self):
        self.cuerpo = ""
     

class Logical:

    v = False

    def __init__(self, f):
        self.v = f

    def setLogical(self, f):
        self.v = f

    def booleanValue(self):
        return self.v



