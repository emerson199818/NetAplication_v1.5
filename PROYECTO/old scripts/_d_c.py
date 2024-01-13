import os
import shutil
import requests # para solisitudes en linea y ibtener informacion
import geocoder
import socket
import ctypes
import requests
import subprocess
from _w_g import win_banners
import time

def init_archivo_inicio():
    if os.path.exists("lib/init.bat") and os.path.exists("lib/init.py"):
        eliminar_doc("lib/init.bat")
        eliminar_doc("lib/init.py")
    
    doc = "lib/init.bat"
    doc_text = "@echo off"
    doc_text1 = "title NetAplication"
    doc_text2 = "python init.py"
    crear_edit_documento(doc, doc_text, 1)
    crear_edit_documento(doc, doc_text1, 2)
    crear_edit_documento(doc, doc_text2, 3)
    ctypes.windll.kernel32.SetFileAttributesW(doc, 2)

    doc1 = "lib/init.py"
    doc1_text = "import time"
    doc1_text1 = "time.sleep(4)"
    doc1_text2 = "text = 'Iniciando...'"
    doc1_text3 = "print(text)"
    crear_edit_documento(doc1, doc1_text, 1)
    crear_edit_documento(doc1, doc1_text1, 2)
    crear_edit_documento(doc1, doc1_text2, 3)
    crear_edit_documento(doc1, doc1_text3, 4)
    ctypes.windll.kernel32.SetFileAttributesW(doc1, 2)#modo oculto
    
    subprocess.call(doc, shell=True)


def nueva_ventana(title, script):
    cmd = f"start \"{title}\" cmd /K python {script}"
    return subprocess.Popen(cmd, shell=True)

def crear_folder(self): #constructor creador de carpetas
    #crear carpeta
    if not os.path.exists(self):
        os.mkdir(self)

"""
crear documento o neva linea en el
(documento_name, dato a ingresar, linea, carpeta)
"""
def crear_edit_documento(documento, texto, linea=None, ruta=None): 
    if ruta is not None:
        documento = os.path.join(ruta, documento)
    with open(documento, 'a+') as file:
        file.seek(0)
        if linea is not None:
            for i in range(linea - 1):
                file.readline()
            pos = file.tell()
            resto = file.read()
            file.seek(pos)
        else:
            file.read()
        file.write(texto + '\n' + resto)

#editar sobre escribir datos del archivo, "ya los datos deben estar ahi para poder editarlso"
#no puedes editar algo que no esta, para meter dato en linea nueva debes usar crear_edit_documento
def editar_documento(documento, texto, linea=None, ruta=None): 
    if ruta is not None:
        documento = os.path.join(ruta, documento)
    with open(documento, 'r') as f:
        contenido = f.readlines()
    contenido[linea - 1] = texto + '\n'
    with open(documento, 'w') as f:
        f.writelines(contenido)

def uso_documento(self): #para sacar datos del documento y usarlos
    with open(self, 'r') as f:
        for linea in f:
            nombre, valor = linea.strip().split(' = ')
            if valor.lower() == 'true':
                valor = True
            elif valor.lower() == 'false':
                valor = False
            globals()[nombre] = valor

#obtener ubicacion, pais, cuidad
def local_map():
    # Verifica si hay conexión a Internet
    try:
        socket.create_connection(("www.google.com", 80))
        internet = True
    except OSError:
        internet = False

    if internet:
        # Hay conexión a Internet, utiliza la API de ipapi.co
        response = requests.get('https://ipapi.co/json')
        data = response.json()
        ciudad = data.get('city', 'Desconocido')
        region = data.get('region', 'Desconocido')
        pais = data.get('country_name', 'Desconocido')
    else:
        # No hay conexión a Internet, utiliza la biblioteca geocoder
        g = geocoder.ip('me')
        ciudad = g.city if g.city else 'Desconocido'
        region = g.state if g.state else 'Desconocido'
        pais = g.country if g.country else 'Desconocido'

    return ciudad, region, pais


def eliminar_doc(self):
    if os.path.exists(self):
        os.remove(self)

#############ALERTAS####################

def alerta_ok(titulo_ventana, titulo, texto):
    hwnd = ctypes.windll.user32.FindWindowW(None, titulo_ventana)
    resultado = ctypes.windll.user32.MessageBoxW(hwnd, texto, titulo, 64)
    return resultado

def alerta_error(titulo_ventana, titulo, texto):
    hwnd = ctypes.windll.user32.FindWindowW(None, titulo_ventana)
    resultado = ctypes.windll.user32.MessageBoxW(hwnd, texto, titulo, 18)
    return resultado

def alerta_aceptar(titulo_ventana, titulo, texto):
    hwnd = ctypes.windll.user32.FindWindowW(None, titulo_ventana)
    resultado = ctypes.windll.user32.MessageBoxW(hwnd, texto, titulo, 33)
    return resultado

def alerta_cerrar(titulo_ventana, titulo, texto):
    hwnd = ctypes.windll.user32.FindWindowW(None, titulo_ventana)
    resultado = ctypes.windll.user32.MessageBoxW(hwnd, texto, titulo, 52)
    return resultado

def alerta_Amarilla(titulo_ventana, titulo, texto):
    hwnd = ctypes.windll.user32.FindWindowW(None, titulo_ventana)
    resultado = ctypes.windll.user32.MessageBoxW(hwnd, texto, titulo, 48)
    return resultado
def alerta_si_no(titulo_ventana, titulo, texto):
    hwnd = ctypes.windll.user32.FindWindowW(None, titulo_ventana)
    resultado = ctypes.windll.user32.MessageBoxW(hwnd, texto, titulo, 36)
    return resultado

#uso
"""
resultado = mostrar_alerta("Terminos y condiciones", "¿Acepta los terminos y condiciones?")
if resultado == 1:
    print("El usuario presionó Aceptar")
elif resultado == 2:
    print("El usuario presionó Cancelar")
"""


"""
print(f'Ciudad: {ciudad}')
print(f'Región: {region}')
print(f'País: {pais}')
"""
#################################
"""DATOS DOCUMENTO
Nombre = Emerson
Terminos = True
Ciudad = Medellin
Region = Antuioquia
Pais = colombia

ruta = "attemp"
Documento_confis = "configs"
crear_folder(ruta)
crear_edit_documento(Documento_confis, "Edad = 25", 1, ruta)
crear_edit_documento(Documento_confis, "Terminos = True", 2, ruta)
crear_edit_documento(Documento_confis, "Nombre = Emerson", 3, ruta)
crear_edit_documento(Documento_confis, "Ciudad = Medellin", 4, ruta)
crear_edit_documento(Documento_confis, "Pais = colombia", 5, ruta)
print("DONE...")

os.chdir(ruta)
uso_documento(Documento_confis)
print(Ciudad)
print("DONE...")
os.chdir('..')

editar_documento(Documento_confis, "Ciudad = Cartagen", 4, ruta)
os.chdir(ruta)
uso_documento(Documento_confis)
print(Ciudad)
print("DONE...")
"""