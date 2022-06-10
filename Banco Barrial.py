
from ast import For
from datetime import date, datetime
from time import time

#CREAMOS LAS LISTAS EN UN AMBITO GLOBAL 

global lista_Usu
global lista_Transacciones
global lista_Clientes
lista_Usu=list()
lista_Clientes=list()
lista_Transacciones=list()

#SE CREA LA CLASE USUARIOS
class Usuario:
    Id=0
    Usuario=""
    Clave=""
    Nombres=""
    Apellidos=""

def Registro_Usuario():
    print("****** Registro de Usuarios ******")
    a=Usuario()
    a.Id=input("Ingrese Id: ")
    a.Usuario=input("Ingrese Usuario: ")
    a.Clave=input("Ingrese Clave: ")
    a.Nombres=input("Ingrese Nombres: ")
    a.Apellidos=input("Ingrese Apellidos: ")
    lista_Usu.append(a)

def Mostrar_Usuarios():
    print("****** Lista de Usuarios Registrados ******")
    for a in lista_Usu:
        print (a.Id, "-",a.Usuario, "-",a.Nombres, "-",a.Apellidos)

def Iniciar_Sesion():
    print("****** Inicio de Sesión ******")
    Usu=input("Ingrese Usuario: ")
    Cla=input("Ingrese Clave: ")

    #RECCORRE LA LISTA PARA LOCALIZAR EL USUARIO Y CONTRASEÑA QUE COINCIDA
    for a in lista_Usu:
        if a.Usuario==Usu and a.Clave==Cla:
            #PASA AL MENU DE LOS SERVICIOS BANCARIOS
            print("###### Menu Servicios Bancarios - Usuario: " + Usu)
            menu_Bancario()
        else:
            print("****** Datos ingresados no existen o son incorrectos ******")

def menu_Usu():
    op=0
    Salir=4
    while op != 4:
        #Mostrar Menu
        print("****** MENU PRINCIPAL ******")
        print("1.- Registrar")
        print("2.- Iniciar Sesión")
        print("3.- Mostrar Usuarios")
        print("4.- Salir")

        op = int(input("Digite la opción deseada: "))
        if op == 1:
            Registro_Usuario()
        elif op == 2:
            Iniciar_Sesion()
        elif op == 3:
            Mostrar_Usuarios()
        elif op == 4:
           break

#CREAMOS LA CLASE CLIENTES
class Clientes:
    Cedula=""
    Nombres=""
    Apellidos=""
    Ncuenta=""
    Saldo=""

def Llenar_Clientes():
    x=0
    while x !=4:
        a=Clientes()
        a.Cedula=input("Ingrese Cédula: ")
        a.Nombres=input("Ingrese Nombres: ")
        a.Apellidos=input("Ingrese Apellidos: ")
        a.Ncuenta=input("Ingrese Numero Cuenta: ")
        a.Saldo=input("Ingrese Saldo: ")
        lista_Clientes.append(a)
        x=x+1


    print("Lista de Clientes Registrados")
    for a in lista_Clientes:
        print ("Cedula:" + a.Cedula, "- Nombres: ",a.Nombres, "- Apellidos: ",a.Apellidos, "- Cuenta: ",a.Ncuenta, "- Saldo: ",a.Saldo)

#SE CREA EL MENU DE LOS SERVICIOS BANCARIOS UNA VEZ QUE SE HAYA INICIADO SESION CORRECTAMENTE

def menu_Bancario():
    op=0
    Salir=4
    while op != 4:
        #Mostrar Menu
        print("****** Menu de Servicios Bancarios ******")
        print("1.- Ver Clientes")
        print("2.- Depositos")
        print("3.- Retiros")
        print("4.- Salir")

        op = int(input("Digite la opción deseada: "))
        if op == 1:
            Llenar_Clientes()
        elif op == 2:
            Depositos()
        elif op == 3:
            pass
            Retiros()
        elif op == 4:
           break


#CREAMOS LA CLASE PARA LAS TRANSACCIONES BANCARIAS

class Transacciones():
    nMov=0
    n_Cuenta=""
    Valor=0
    Tipo=""
    Fecha=""
    Depositante=""

#METODOS PARA REALIZAR LAS TRANSACCIONES

def Depositos():
    print("****** Transacciones Bancarias: DEPOSITOS ******")
    a=Transacciones()
    a.nMov=input("Ingrese numero de movimiento: ")
    a.n_Cuenta=input("Ingrese Cuenta: ")
    a.Valor=int(input("Ingrese Valor: "))
    a.Tipo="DEPOSITO"
    a.Fecha=datetime.now()
    a.Depositante=input("Ingrese Depositante: ")
    if a.Valor<500:
        lista_Transacciones.append(a)
        print("Deposito realizado: ")
        for a in lista_Transacciones:
            print ("NMov: " + a.nMov, "- #Cuenta: ",a.n_Cuenta, "- Valor: ",a.Valor, "- Tipo Transaccion: ",a.Tipo, "- Fecha Actual: " ,a.Fecha, "- Depositante: ",a.Depositante)
    else:
        print("Valor no permitido")

def Retiros():
    print("****** Transacciones Bancarias: RETIROS ******")
    a=Transacciones()
    a.nMov=input("Ingrese numero de movimiento:  ")
    a.n_Cuenta=input("Ingrese Cuenta: ")
    a.Valor=int(input("Ingrese Valor: "))
    a.Tipo="RETIRO"
    a.Fecha=datetime.now()
    if a.Valor<500:
        lista_Transacciones.append(a)
        print("Retiros realizado: ")
        for a in lista_Transacciones:
            print ("NMov: " + a.nMov, "- #Cuenta: ",a.n_Cuenta, "- Valor: ",a.Valor, "- Tipo Transaccion: ",a.Tipo, "- Fecha Actual: " ,a.Fecha, "- Depositante: ",a.Depositante)
    else:
        print("Valor no permitido")

#VERIFICAMOS QUE LA FECHA ACTUAL NO SEA FESTIVO PARA PODER EJECUTAR
fechaActual=datetime.now()
fechax=fechaActual.strftime("%y-%m-%d")

#menu principal

if fechax != "22-01-01" and "2022-01-02" and "2022-01-03" and "2022-02-28" and "2022-03-01" and "2022-03-02" and "2022-04-11" and "2022-04-12" and "2022-04-13" and "2022-04-14" and "2022-04-15" and "2022-04-16" and "2022-04-17" and "2022-05-24" and "2022-12-25":
    print(">>>>>>>Bienvenido a los Servicios Bancarios <<<<<<<<")
    menu_Usu()
else:
    print("No trabajamos en dias festivos, gracias por su comprension")

