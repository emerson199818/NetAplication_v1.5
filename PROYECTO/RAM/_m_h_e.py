import os
import os.path
import io
import shutil
import psutil
import subprocess 
from reportlab.lib.pagesizes import letter #funciones para la creacion de pdf
from reportlab.platypus import SimpleDocTemplate, Preformatted, Image #funciones para la creacion de pdf
from reportlab.lib.styles import getSampleStyleSheet #funciones para la creacion de pdf
from _d_c import alerta_ok, eliminar_doc
import getpass
import ctypes
import sys
import getpass

#Consulta NOMBRE DE EQUIPO
def Nombre_equipo():
	nombre_equipo = os.environ.get('COMPUTERNAME') or os.environ.get('HOSTNAME')
	return nombre_equipo
