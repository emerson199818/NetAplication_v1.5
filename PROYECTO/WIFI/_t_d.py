import os #usar funciones o comandos del sistema tanto widnows como linux
import random #para generador ramdon
import time #para generador ramdon
import datetime #para sacar informacion de fecha y hora
from colorama import init, Fore, Style #formato de colores, pip install colorama
import getpass
import subprocess
import shutil

def limpiar():
    if os.name == 'nt':  # Verificar si el sistema operativo es Windows
        _ = os.system('cls')
    else:  # Para sistemas operativos Unix/Linux/Mac
        _ = os.system('clear')

def stop(self):
    time.sleep(self)
