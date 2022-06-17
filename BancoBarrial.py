"""LIBRERIAS LAS CUALES NOS SIRVEN PARA OBTENER LA FECHA ACTUAL DE LA PC"""
from ast import For
from time import time

import os
import requests
import json

from datetime import date,datetime

import holidays
from holidays.holiday_base import HolidayBase


from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, FR
from holidays.constants import FEB,APR, MAR, JAN,JUL, MAY, AUG, OCT, NOV, DEC



class HolidayEcuador(HolidayBase):    #
    """
   Clase para hacer mas sencillo los feriados.
        el cual tendra referncia las provincias las cuales son pasados por herencia.
                     https://www.turismo.gob.ec/wp-content/uploads/2020/03/CALENDARIO-DE-FERIADOS.pdf
    ...
    Atributos (clase padre) 
    ---------- prov: str código de provincia según ISO3166-2 Métodos ------- 
        __init__(self, plate, date, time, online=False) : 
                 Construye todos los atributos necesarios para el objeto HolidayEcuador.
        _populate(self, year): Devuelve si una fecha es festiva o no
        """     
    # Códigos ISO 3166-2 (estan en los metodos)), 
    # # llamadas provincias
    # https://es.wikipedia.org/wiki/ISO_3166-2:EC
    PROVINCES = ["EC-SD"]  # TODO add more provinces        #

    def __init__(self, **kwargs):                    # 
        """
         Construye todos los atributos necesarios para el objeto HolidayEcuador.
        """         
        self.country = "ECU"
        self.prov = kwargs.pop("prov", "ON")
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):                             #
        """
        Comprueba si una fecha es festiva o no 
        Parámetros 
        ----------
             year : str año de una fecha Devuelve 
         ------
             Devuelve verdadero si una fecha es festiva de lo contrario false
        """                    
        # New Year's Day 
        self[date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"           #
        
        # Christmas
        self[date(year, DEC, 25)] = "Navidad [Christmas]"                 #

        #carnaval lunes y martes
        self[date(year, FEB, 28)] = "Carnaval [carnaval lunes]" 
        self[date(year, MAR, 1)] = "Carnaval [carnaval martes]"

        #Pascua
        self[date(year, APR, 17)] = "Dia de pascua "
        

        #semana santa
        self[date(year, APR, 2)] = "Semana Santa "
        self[date(year, APR, 3)] = "Semana Santa "
        self[date(year, APR, 4)] = "Semana Santa "
        self[date(year, APR, 5)] = "Semana Santa "
        self[date(year, APR, 6)] = "Semana Santa "
        self[date(year, APR, 7)] = "Semana Santa "
        self[date(year, APR, 8)] = "Semana Santa "

        #Dia del trabajo
        self[date(year, MAY, 1)] = "Dia del trabajo "
        self[date(year, MAY, 2)] = "Dia del trabajo "

        #Batalla de pichincha
        self[date(year, MAY, 23)] = "Baalla Pichincha"

        #Dia de simon Bolivar
        self[date(year, JUL, 25)] = "Dia simon Bolivar"

        #Dia de independencia
        self[date(year, AUG, 10)] = "Dia de independencia"

        #Dia de muertos
        self[date(year, NOV, 2)] = "Dia de muertos"

        #cantonizacion santo domingo
        self[date(year, JUL, 3)] = "Cantonizacion santo domingo"

        #provincializacion de santo domingo
        self[date(year, OCT, 6)] = "Provincializacion de sano domingo"
    







class diasFeriado:                
    '''
    Una clase la cual va a refleijar los dias de feriados . '''
    
    #Dias de la semana 
    __days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]

    # Restricciones de las fechas de feriados
    __restrictions = {
            "Monday": [1, 2],
            "Tuesday": [3, 4],
            "Wednesday": [5, 6],
            "Thursday": [7, 8],
            "Friday": [9, 0],
            "Saturday": [],
            "Sunday": []}

    def __init__(self, date, online=False):                
        """
         Construye todos los atributos necesarios para el objeto PicoPlaca.
        
         Parámetros
         ----------
            fecha: calle
                 Fecha en la que el vehículo pretende transitar
                 Sigue el formato ISO 8601 AAAA-MM-DD: por ejemplo, 2020-04-22.  
            en línea: booleano, opcional
                 si en línea == Verdadero, se usará la API de días festivos abstractos (el valor predeterminado es Falso)           
        """                
        self.date = date
        self.online = online
        
        
    @property                   
    def date(self):
        """ Obtiene el valor del atributo de fecha"""
        return self._date

    @date.setter                    
    def date(self, value):
        """
      Establece el valor del atributo de fecha
         Parámetros
         ----------
         valor: cadena
        
         aumenta
         ------
         ValorError
             Si la cadena de valor no tiene el formato AAAA-MM-DD (por ejemplo, 2021-04-02)
        """
        try:
            if len(value) != 10:
                raise ValueError
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                'La fecha debe tener el siguiente formato: AAAA-MM-DD (por ejemplo: 2021-04-02)') from None
        self._date = value

    def __is_holiday(self, date, online):       
        """
         Comprueba si la fecha (en formato ISO 8601 AAAA-MM-DD) es un día festivo en Ecuador
         si en línea == Verdadero, utilizará una API REST, 
         de lo contrario, generará los días festivos del año examinado
        
         Parámetros
         ----------
         fecha: calle
             Está siguiendo el formato ISO 8601 AAAA-MM-DD: 
             por ejemplo, 2020-04-22
         en línea: booleano, opcional
             si en línea == Verdadero, se utilizará la API de días festivos abstractos
         Devoluciones
         -------
         Devuelve True si la fecha marcada (en formato ISO 8601 AAAA-MM-DD) es un día festivo en Ecuador,
          de lo contrario, Falso
        """            
        y, m, d = date.split('-')

        if online:
            # API de vacaciones abstractapi, versión gratuita: 1000 solicitudes por mes
            # 1 solicitud por segundo
            # recuperar la clave API de la variable de entorno
            key = os.environ.get('HOLIDAYS_API_KEY')
            response = requests.get(
                "https://holidays.abstractapi.com/v1/?api_key={}&country=EC&year={}&month={}&day={}".format(key, y, m, d))
            if (response.status_code == 401):
                # Esto significa que falta una clave API
                raise requests.HTTPError(
                    'Falta la clave API. Guarde su clave en la variable de entorno HOLIDAYS API_KEY')
            if response.content == b'[]':  # si no hay vacaciones, obtenemos una matriz vacía
                return False
            # Arreglar el Jueves Santo incorrectamente denotado como feriado
            if json.loads(response.text[1:-1])['name'] == 'Maundy Thursday':
                return False
            return True
        else:
            ecu_holidays = HolidayEcuador(prov='EC-SD')
            return date in ecu_holidays

    def predict(self):         
        """
         -------
         
         Verdadero si fecha  con online
           Es dia festivo
         en la fecha especificadas, de lo contrario Falso
        """
        # Check if date is a holiday
        if self.__is_holiday(self.date, self.online):       
            return True
        return False          




'''CREAMOS LAS LISTAS EN UN AMBITO GLOBAL '''
global lista_Usuario
global lista_Transacciones

lista_Usuario=list()
lista_Transacciones=list()

'''SE CREA LA CLASE USUARIOS'''
class Usuario: 
    '''Clase para hacer el ingreso de Usuario.
        __init__(self) : 
                 Construye todos los atributos necesarios para el objeto Usuario:.
        Registro_Usuario():
                Ingreso de Id,Usuario,Clave,Nombres,Apellidos la cual declaramas una variables donde nso gruardara  los ingresos dde datos_Peronales=Usuario()
                donde permitira guardar todo ingreso en ista_Usuario 
        Mostrar_Usuario():
                Mostrara el registro de los usuarios. 
        Iniciar_Sesion():
                una vez que aya registrado sus datos personales podra iniciar sesion en el banco barrial donde pedira su  usuario y clave ya registrado  tambien utilizamos 
                if 
                else:
                donde se podra observar si los datos del cliente exiteno no.
        menu_Usuario():
                consta de 4 opciones, Registrar, Iniciar sesion, mostrar usuario y salir.
        menu_Bancario():
                consta de 3 opciones, Depositos,Retiros y salir.

        '''     

    def __init__(self):
        self.Id=0
        self.Usuario=""
        self.Clave=""
        self.Nombres=""
        self.Apellidos=""
     
    def Registro_Usuario():
        print("----------------------------------")
        print("****** Registro de Usuarios ******")
        print("----------------------------------")
        datos_Personales=Usuario()
        datos_Personales.Id=input("Ingrese Id: ")
        datos_Personales.Usuario=input("Ingrese Usuario: ")
        datos_Personales.Clave=input("Ingrese Clave: ")
        datos_Personales.Nombres=input("Ingrese Nombres: ")
        datos_Personales.Apellidos=input("Ingrese Apellidos: ")
        #Vamos guardando los diversos datos que toma el objeto dentro de la lista correspondiente.
        lista_Usuario.append(datos_Personales)
    '''SE CREA UN METODO EL CUAL MUESTRE LOS USUARIOS'''
    def Mostrar_Usuarios():
        print("-------------------------------------------")
        print("****** Lista de Usuarios Registrados ******")
        print("-------------------------------------------")
        """USAMOS EL CICLO FOR PARA IMPRIMIR TODOS LOS DATOS ALMACENADOS EN LA LISTA
        lista_Usu"""
        for datos_Personales in lista_Usuario:
            print (datos_Personales.Id, "-",datos_Personales.Usuario, "-",datos_Personales.Nombres, "-",datos_Personales.Apellidos)
    '''SE CREA UN METODO EL CUAL INICIE SESION DE LOS USUARIOS REGISTRADOS'''

    def Iniciar_Sesion():
        print("****** Inicio de Sesión ******")
        Usuario1=input("Ingrese Usuario: ")
        Clave1=input("Ingrese Clave: ")
        '''RECCORRE LA LISTA PARA LOCALIZAR EL USUARIO Y CONTRASEÑA QUE COINCIDA'''
        for datos_Personales in lista_Usuario:
            if datos_Personales.Usuario==Usuario1 and datos_Personales.Clave==Clave1:
                """PASA AL MENU DE LOS SERVICIOS BANCARIOS"""
                print("###### Menu Servicios Bancarios - Usuario: " + Usuario1)
                Usuario.menu_Bancario()
            else:
                """CASO CONTRARIO NOS NIEGA EL ACCESO AL MENU DE LOS SERVICIOS BANCARIOS"""
                print("****** Datos ingresados no existen o son incorrectos ******")

    '''CREAMOS UN METODO EL CUAL ORGANIZA LOS METODOS ANTERIORES EN UN MENU'''
    def menu_Usuario():
        op=0
        Salir=4
        while op != 4:
            #Mostrar Menu
            print("----------------------------")
            print("****** MENU PRINCIPAL ******")
            print("----------------------------")
            print("1.- Registrar")
            print("2.- Iniciar Sesión")
            print("3.- Mostrar Usuarios")
            print("4.- Salir")
            print("----------------------------")

            op = int(input("Digite la opción deseada: "))
            if op == 1:
                Usuario.Registro_Usuario()
                print("---------------------------------")

            elif op == 2:
                Usuario.Iniciar_Sesion()
                print("---------------------------------")

            elif op == 3:
                Usuario.Mostrar_Usuarios()
                print("---------------------------------")

            elif op == 4:
                break

    '''SE CREA EL MENU DE LOS SERVICIOS BANCARIOS UNA VEZ QUE SE HAYA INICIADO SESION CORRECTAMENTE'''
    def menu_Bancario():
        op=0
        Salir=4
        while op != 3:
            #Mostrar Menu
            print("-----------------------------------------")
            print("****** Menu de Servicios Bancarios ******")
            print("-----------------------------------------")
            print("1.- Depositos")
            print("2.- Retiros")
            print("3.- Salir")
            print("-----------------------------------------")
            op = int(input("Digite la opción deseada: "))
            if op == 1:
                """ se llama al metodo depositos"""
                Transacciones.Depositos()
            elif op == 2:
                pass
                """ se llama al metodo retiros"""
                Transacciones.Retiros()
            elif op == 3:
                break

#CREAMOS LA CLASE PARA LAS TRANSACCIONES BANCARIAS'''


class Transacciones():
    '''Clase para hacer el tipo de transaccioes que son dos (Desito y Retiro).
        __init__(self) : 
                 Construye todos los atributos necesarios para el objeto Transacciones:.
        Depositos():
                variable giro_Bancario a cual hace referencia a Transacciones
                tenemos el ingreso de num_Cuenta,Valor,num_Movimienton 
                utilizams un for movimientos in range(giro_Bancario.Valor): la cual permiete que el numero de movimientos sea utomatico al momento de realizar nuestra transaccion de deposito
                utilizamos un il else: para que nos validar  el valor limite que es <500.
                lista_Transacciones nos sirve para guardar los datos ingresados de depositos
        Retiros():
                variable giro_Bancario a cual hace referencia a Transacciones
                tenemos el ingreso de num_Cuenta,Valor,num_Movimienton 
                utilizams un for movimientos in range(giro_Bancario.Valor): la cual permiete que el numero de movimientos sea utomatico al momento de realizar nuestra transaccion de deposito
                giro_Bancario.Fecha=datetime.now() ya que este nos imprime la fecha acual de la realizacion de retiro o deposito 
                utilizamos un il else: para que nos validar  el valor limite que es <500.
                lista_Transacciones nos sirve para guardar los datos ingresados de depositos
        es_numerico(cadena): 
                es un método la cual indica que solo se puede ingresar numeros y no letras si uno ingresa letras nos imprimira que (Valor digitado no es numerico) 
    '''
    def __init__(self):
            self.num_Movimienton=0
            self.num_Cuenta=""
            self.Valor=0
            self.Tipo=""
            self.Fecha=""
            self.Depositante=""
    '''METODOS PARA REALIZAR LAS TRANSACCIONES'''
    def Depositos():
        print("------------------------------------------------")
        print("****** Transacciones Bancarias: DEPOSITOS ******")
        print("------------------------------------------------")
        """ se instancia el objeto giro_Bancario """
        giro_Bancario=Transacciones()
        giro_Bancario.num_Cuenta=input("Ingrese numero de Cuenta: ")
        giro_Bancario.Valor=input("Ingrese Monto a depositar (solo numeros): ")

        while Transacciones.es_numerico(giro_Bancario.Valor):
            print("Valor digitado no es numerico")
            giro_Bancario.Valor= input("Ingrese Monto a depositar (solo numeros): ")
        giro_Bancario.Valor=int(giro_Bancario.Valor)
        giro_Bancario.Tipo="DEPOSITO"
        giro_Bancario.Fecha=datetime.now()
        giro_Bancario.Depositante=input("Ingrese Depositante: ")
        if giro_Bancario.Valor<500:
            lista_Transacciones.append(giro_Bancario)
            print("Deposito realizado: ")
            for movimientos in range(giro_Bancario.Valor):
                giro_Bancario.num_Movimienton=giro_Bancario.Valor-1
            for giro_Bancario in lista_Transacciones:
                print ("Numero de Movimiento: ", giro_Bancario.num_Movimienton, "- Num. Cuenta: ",giro_Bancario.num_Cuenta, "- Valor: ",giro_Bancario.Valor, "$ - Tipo Transaccion: ",giro_Bancario.Tipo, "- Fecha: " ,giro_Bancario.Fecha, "- Depositante: ",giro_Bancario.Depositante)
        else:
            print("----------------------------------------------------------")
            print("Valor Deposito no permitido, ingrese Deposito no mayor a 500")
            print("----------------------------------------------------------")
   
    def Retiros():
        print("----------------------------------------------")
        print("****** Transacciones Bancarias: RETIROS ******")
        print("----------------------------------------------")
        """ se vuelve a instanciar el objeto para la otra clase """
        giro_Bancario=Transacciones()
        giro_Bancario.num_Cuenta=input("Ingrese numero de Cuenta: ")
        giro_Bancario.Valor=input("Ingrese Monto (solo numeros): ")

        while Transacciones.es_numerico(giro_Bancario.Valor):
          print("Valor digitado no es numerico")
          giro_Bancario.Valor= input("Ingrese Monto (solo numeros): ")
        giro_Bancario.Valor=int(giro_Bancario.Valor)
        giro_Bancario.Tipo="RETIRO"
        giro_Bancario.Fecha=datetime.now()
        giro_Bancario.Depositante="Sin depositante por ser retiro"
            
        if giro_Bancario.Valor<500:
            lista_Transacciones.append(giro_Bancario)
            print("Retiros realizado: ")
            for movimientos in range(giro_Bancario.Valor):
                giro_Bancario.num_Movimienton=giro_Bancario.Valor+1
            for giro_Bancario in lista_Transacciones:
                print ("Numero de Movimiento: ", giro_Bancario.num_Movimienton, "- Num. Cuenta: ",giro_Bancario.num_Cuenta, "- Valor: ",giro_Bancario.Valor, "$ - Tipo Transaccion: ",giro_Bancario.Tipo, "- Fecha: " ,giro_Bancario.Fecha, "- Depositante: ",giro_Bancario.Depositante)
        else:
            print("----------------------------------------------------------")
            print("Valor Retiro no permitido, ingrese Retiro no mayor a 500")
            print("----------------------------------------------------------")
    '''Verificar si son numeros en valor'''
    def es_numerico(cadena):
        try:
            int(cadena)
            return False
        except ValueError:
            return True

#no harcorear

if __name__ == '__main__':

    online = False     

    fecha= input('ingrese Fecha: YYYY-MM-DD:')  


    pyp = diasFeriado(fecha , online)       

    if pyp.predict():
        print("----------------------------------------------------------")
        print("No trabajamos en dias festivos, gracias por su comprension")
        print("----------------------------------------------------------")

    else:
       print(">>>>>>>Bienvenido a los Servicios Bancarios <<<<<<<<")
       Usuario.menu_Usuario()
