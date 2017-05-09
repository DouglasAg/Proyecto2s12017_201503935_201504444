from django.shortcuts import render
from proyecto2.Estructuras import ListaDoble
from proyecto2.Estructuras import ListaDobleC
from proyecto2.Estructuras import Historial
from proyecto2.Estructuras import ArbolB
import time


driveusu = ListaDoble.ListaDoble()
driveh = Historial.Historial()
calendarh = Historial.Historial()
calusu = ListaDobleC.ListaDoble()

def index(request):
    return render(request, 'index.html')

def logdrive(request):
    return render(request,"log_drive.html")

def pridive(request):
    return render(request,'pri_drive.html')

def moddrive(request):
    return render(request,'modificar.html')

def historialdrive(request):
    hola = driveh.listar()
    return hola

def historialcalendar(request):
    hola = calendarh.listar()
    return hola

def listadrive(request):
    hola = driveusu.cuerpo()
    return hola

def listacalendar(request):
    hola = calusu.cuerpo()
    return hola

def iniciarcalendar(request):
    if request.method == 'POST':
        bien = False
        try:
            nombre = request.POST['nomb']
            clave = request.POST['passw']
            print(nombre)
            print(clave)
            bien = calusu.iniciar(nombre,clave)
            request.session['usuario'] = nombre
        except Exception as ex:
            print("No llegaron los datos del loging calendar ")
            bien=False

        if bien:
            b = " Fecha y Hora: " + time.strftime("%c") + " Regitro: Nuevo inicio de seccion usuario: " + nombre 
            driveh.agregarFinal(b)
            return render(request, 'pri_drive.html',{'usuario':nombre})
        else:
            b = " Fecha y Hora: " + time.strftime("%c") + " Regitro: Intento de iniciar seccion co usuario: " + nombre 
            driveh.agregarFinal(b)
            return render(request, 'log_calendar.html',{'bien':bien})


def calendarenew(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['nom']
            apellido = request.POST['apellido']
            clave = request.POST['password']
            confirmacion = False
            print("nombre: "+nombre)
            print("apellido: "+apellido)
            print("clave: "+clave)
            calusu.insertar(nombre, apellido, clave)
            print(calusu.imprimir())
            b = " Fecha y Hora: " + time.strftime("%c") + " Regitro: Nuevo usuario creado Nombre: " + nombre + " Apellido: " + apellido
            calendarh.agregarFinal(b)
            print(calendarh.listar())
            confirmacion = True
        except Exception as inst:
            confirmacion = False
            print("Error ingresar usuario en drive")
    return render(request, 'log_drive.html',{'confirmacion': confirmacion})

def drivenew(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['nom']
            apellido = request.POST['apellido']
            clave = request.POST['password']
            confirmacion = False
            print("nombre: "+nombre)
            print("apellido: "+apellido)
            print("clave: "+clave)
            driveusu.insertar(nombre, apellido, clave)
            print(driveusu.imprimir())
            b = " Fecha y Hora: " + time.strftime("%c") + " Regitro: Nuevo usuario creado Nombre: " + nombre + " Apellido: " + apellido
            driveh.agregarFinal(b)
            print(driveh.listar())
            confirmacion = True
        except Exception as inst:
            confirmacion = False
            print("Error ingresar usuario en drive")
    return render(request, 'log_drive.html',{'confirmacion': confirmacion})


def nuevacarpeta(request):
        if request.method == 'POST':           
            try:
                usuariio = request.POST['usuario']
                nombre = request.POST['nombre']
                ruta = request.POST['ruta']
                confirmacion = False
                print("usuario: " + usuariio)
                print("noobre: " + nombre)
                print("ruta: "+ ruta)
                if ruta == "/":
                    a = driveusu.nuevacarpeta(usuariio, nombre)
                    print(a)
                    b = " Fecha y Hora: " + time.strftime("%c") + " Regitro: Nuevo inicio de seccion usuario: " + nombre 
                    driveh.agregarFinal(b)
                else:
                    car = ruta.split("/")
                    for x in car:
                        print(x)


                    x = len(car)

                    arbol = driveusu.getarbol(usuariio)
                    for xd in range(x):
                        arbol.buscarcarpeta(arbol.p, car)
                    otro = arbol.encontrado
                    try:
                        otro.insertar(nombre)
                    except Exception as error:
                        print("No se encontro ruta")
            except Exception as inst:
                confirmacion = False
                print("Error carpeta")
        return render(request, 'pri_drive.html',{'usuario':usuariio})


def cargararchivo(request):
    if request.method == 'POST':
        confirm = False
        arch = request.FILES['arch']
        path = request.POST['ruta']
        usuario = request.POST['nombre']
        fs = FileSystemStorage()
        nombrefile = fs.save(arch.name, arch)
        upload_dir = fs.url(nombrefile)
        ruta = settings.BASE_DIR+"\\media\\"+nombrefile
        archivo = drivenew.archivo(ruta)
        lista = ruta.split("\\")
        x = len(lista) - 1
        nombre = lista[x]
        lista2 = nombre.split(".")
        extension = lista2[1]
        name = lista2[0]
        if path == "":
            Avl = lista_usuario.obtener_archivos(usuario)
            try:
                print("entro aqui porque path es vacio")
                Avl.agregar(name, extension, archivo)
                cadena = Avl.graficar()
                confirm = True
                print(cadena)
            except Exception as r:
                confirm = False
                print("error... "+str(r))
        else:
            print("entro cuando hay una carpeta")
            listadocarpetas = path.split("/")
            dir = lista_usuario.obtener_directorio(usuario)
            nodoaux = lista_usuario.buscar_avl(dir, listadocarpetas)
            try:
                nodoaux.files.agregar(nombre, extension, archivo)
                cadena = nodoaux.files.graficar()
                confirm = True
                print(cadena)
            except Exception as err:
                confirm = False
                print("Error "+str(err))
        return render(request, 'pri_drive.html',{'usuario':usuariio})


def iniciar(request):
    if request.method == 'POST':
        bien = False
        try:
            nombre = request.POST['nomb']
            clave = request.POST['passw']
            print(nombre)
            print(clave)
            bien = driveusu.iniciar(nombre,clave)
            request.session['usuario'] = nombre
        except Exception as ex:
            print("No llegaron los datos del loging drive ")
            bien=False

        if bien:
            b = " Fecha y Hora: " + time.strftime("%c") + " Regitro: Nuevo inicio de seccion usuario: " + nombre 
            driveh.agregarFinal(b)
            return render(request, 'pri_drive.html',{'usuario':nombre})
        else:
            b = " Fecha y Hora: " + time.strftime("%c") + " Regitro: Intento de iniciar seccion co usuario: " + nombre 
            driveh.agregarFinal(b)
            return render(request, 'log_drive.html',{'bien':bien})


def nuevoa(request):
    return render(request, 'nuevo.html')

def nuevo(request):
    if request.method == 'POST':
        bien = False
        try:
            nombre = request.POST['nomb']
            clave = request.POST['passw']
            print(nombre)
            print(clave)
            request.session['usuario'] = nombre
        except Exception as ex:
            print("No llegaron los datos del loging drive ")
            bien=False

        if bien:
            b = " Fecha y Hora: " + time.strftime("%c") + " Regitro: Nuevo inicio de seccion usuario: " + nombre 
            driveh.agregarFinal(b)
            return render(request, 'pri_drive.html',{'usuario':nombre})
        else:
            return render(request, 'log_drive.html',{'bien':bien})