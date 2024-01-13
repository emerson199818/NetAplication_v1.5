import os
import shutil
import requests # para solisitudes en linea y ibtener informacion
import geocoder
import socket
import ctypes
import requests
import subprocess
import time

def init_archivo_inicio():
    if os.path.exists("lib/init.bat") and os.path.exists("lib/init.py"):
        eliminar_doc("lib/init.bat")
        eliminar_doc("lib/init.py")
    
    doc = "lib/init.bat"
    doc_text = "@echo off"
    doc_text1 = "title BEGIN"
    doc_text2 = "python init.py"
    crear_edit_documento(doc, doc_text, 1)
    crear_edit_documento(doc, doc_text1, 2)
    crear_edit_documento(doc, doc_text2, 3)

    doc1 = "lib/init.py"
    doc1_text = "import time"
    doc1_text1 = "time.sleep(4)"
    doc1_text2 = "text = 'Iniciando...'"
    doc1_text3 = "print(text)"
    crear_edit_documento(doc1, doc1_text, 1)
    crear_edit_documento(doc1, doc1_text1, 2)
    crear_edit_documento(doc1, doc1_text2, 3)
    crear_edit_documento(doc1, doc1_text3, 4)
    
    subprocess.call(doc, shell=True)

def eliminar_doc(self):
    if os.path.exists(self):
        os.remove(self)

#############ALERTAS####################

def alerta_ok(titulo_ventana, titulo, texto):
    hwnd = ctypes.windll.user32.FindWindowW(None, titulo_ventana)
    resultado = ctypes.windll.user32.MessageBoxW(hwnd, texto, titulo, 64)
    return resultado

def alerta_Amarilla(titulo_ventana, titulo, texto):
    hwnd = ctypes.windll.user32.FindWindowW(None, titulo_ventana)
    resultado = ctypes.windll.user32.MessageBoxW(hwnd, texto, titulo, 48)
    return resultado

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