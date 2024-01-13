import os #usar funciones o comandos del sistema tanto widnows como linux
import random #para generador ramdon
import time #para generador ramdon
import datetime #para sacar informacion de fecha y hora
from colorama import init, Fore, Style #formato de colores, pip install colorama
import getpass
from _m_h_e import Nombre_equipo
import subprocess
import shutil

def fecha_dia(): #se obtiene la fecha y dia de la sema
    
    fecha_actual = datetime.date.today()
    dia_semana = fecha_actual.weekday()

    #convirtiendo numero de dia en nombre
    dias_semana = ['lunes....', 'martes...', 'miércoles', 'jueves...', 'viernes..', 'sábado...', 'domingo..']
    nombre_dia = dias_semana[dia_semana]

    return fecha_actual, nombre_dia

def hora():
    hora = datetime.datetime.now() #obtener hora
    hora_new = hora.strftime("%H:%M:%S")
    return hora_new

def limpiar():
    if os.name == 'nt':  # Verificar si el sistema operativo es Windows
        _ = os.system('cls')
    else:  # Para sistemas operativos Unix/Linux/Mac
        _ = os.system('clear')

#usernmae pc
def pc_user_name():
    return getpass.getuser()

def stop(self):
    time.sleep(self)
