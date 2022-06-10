
from calendar import c
import datetime



#listado de fechas feriados

diaDeAñoNuevo=datetime.datetime(2022,1,1)
lunesCarnaval=datetime.datetime(2022,2,28)
martesCarnaval=datetime.datetime(2022,3,1)
buenViernes=datetime.datetime(2022,4,15)
pascua=datetime.datetime(2022,4,17)
diaDeTrabajo=datetime.datetime(2022,5,1)
batallaDePichincha=datetime.datetime(2022,5,23)
diaSimonBolivar=datetime.datetime(2022,7,25)
diaDeIdependencia=datetime.datetime(2022,8,10)
independenciaGuayaquil=datetime.datetime(2022,10,9)
diaMuertos=datetime.datetime(2022,11,2)
independenciaDeCuenca=datetime.datetime(2022,11,3)
fundacionQuito=datetime.datetime(2022,12,6)
navidad=datetime.datetime(2022,12,25)



#clase Cliente
class bancoBarrial:
    def __init__(self, nombre, telefono, nombreBanco,numeroCedula):
        self.nombre=nombre
        self.telefono=telefono
        self.nombreBanco=nombreBanco
        self.numeroCedula=numeroCedula
    #Metodo registrar clave
    def registrarse(self, clave):     
       
       clave=clave

    #Metodo iniciar secion con numero de cedula y clave
    def inicioSecion(self, usu,contra):
        usu=usu
        contra=contra

fechaActual2=datetime.datetime.now()

#menu principal
if fechaActual2!=diaDeAñoNuevo:
                                          
            
 subMenu2=int(input("============================\n Menu Banco Barrial: \n 1-Registrarse \n 2-Iniciar sesion \n 3-salir \n============================\n Ingrese una opcion: ")) 
 while subMenu2 != 3:
     if subMenu2 ==1:
         print("Registrarse en Banco Barrial ")
         nombreBanco=str(input("Ingrese nombre de Banco: "))
         nombre=str(input("Ingrese nombre de cuenta: "))
         telefono=str(input("Ingrese su telefono: "))
         numeroCedula=str(input("Ingrese su cedula: "))
         clave=str(input("Ingrese clave para registrar: "))
         z=bancoBarrial(nombre, telefono,nombreBanco,numeroCedula,).registrarse(clave)       #instanciar cliente y metodo registrarse
         print("usted se a registrado")

     elif subMenu2 ==2:
         print("Inicie sesion")

         print("A continuacion ingrese los datos: ")
        #metodo iniciosesion comparar clave y numero de cedula ingresada para acceder
         usu=str(input("Ingrese nombre de cuenta ya registrado: "))
         contra=str(input("Ingrese contraseña ya registrado: "))
         if usu==nombre and contra==clave:
              print("Acceso concedido")
             #submenu3
              subMenu3=int(input("============================\n Sub Menu Movimientos 2: \n 1-Depositar \n 2-Retirar \n 3-Mostrar Monto \n 4-Regresar \n============================\n Ingrese una opcion: "))
              while subMenu3 != 4:
                  if subMenu3 ==1:

                    
                     monto=int(input("Ingrese monto de deposito a realizar: "))

                     if monto<501:
                       print("______________________________________________\n")
                       print("               Registro de Deposito: \n")
                       print("Nombre Banco: ",nombreBanco)
                       print("Nombre de Cuenta: ",nombre)
                       print("Numero Telefono: ",telefono)
                       print("Numero Cedula: ",numeroCedula)
                       fechaActual=datetime.datetime.now()
                       fechaActual1=datetime.datetime.strftime(fechaActual, '%b %d %Y %H:%M:%S')
                       print("Cantidad Depositada:",monto," Fecha de movimiento ",fechaActual1)
                       print("______________________________________________\n")
                     else:
                           print("Error no puede depositar mas de 500 vuelva a intentar")          
                                

                  elif subMenu3 ==2:

                     retiro=int(input("Ingrese monto de retiro a realizar, maximo hasta 500: "))

                     if monto>retiro:
                         
                         if retiro<501:

                            retiroTotal=monto-retiro

                            print("______________________________________________\n")
                            print("              Registro de Retiro              ")
                            print("Nombre Banco: ",nombreBanco)
                            print("Nombre de Cuenta: ",nombre)
                            print("Numero Telefono: ",telefono)
                            print("Numero Cedula: ",numeroCedula)
                            fechaActual=datetime.datetime.now()
                            fechaActual1=datetime.datetime.strftime(fechaActual, '%b %d %Y %H:%M:%S')
                            print("Cantidad retirada:",retiro," Fecha de movimiento ",fechaActual1)
                            print("______________________________________________\n")

                         else:
                             print("su retiro no puede ser mayor a 500 vuelva a intentar")
                            
                             

                     else:
                        print("error su retiro no debe ser mayor a tu monto de cuenta")
                        print("vuelva a intentar")


                    
                  elif subMenu3 ==3:
                     
                    
                     print("monto total",retiroTotal)


                  elif subMenu3 ==4:
                     print("Regresar ")

                  else:
                     print("Por favor ingrese una opcion correcta: ")
                  subMenu3=int(input("============================\n Sub Menu Clientes 2: \n 1-Depositar \n 2-Retirar \n 3-Transferir \n 4-Regresar \n============================\n Ingrese una opcion: "))
         else:
             print("acceso denegado")
     elif subMenu2 ==3:
         print("salir ")
     else:
          print("Por favor ingrese una opcion correcta: ")
     subMenu2=int(input("============================\n Menu Banco Barrial: \n 1-Registrarse \n 2-Iniciar sesion \n 3-salir \n============================\n Ingrese una opcion: ")) 
else:
    print("_____________________________________________________________________\n")
    print("No se puede hacer transaccion en Dias feriados intentelo mas tarde")
    print("_____________________________________________________________________\n")

    
         


