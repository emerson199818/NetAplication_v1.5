import os
import os.path
import io
import shutil
import psutil
import subprocess 
from reportlab.lib.pagesizes import letter #funciones para la creacion de pdf
from reportlab.platypus import SimpleDocTemplate, Preformatted, Image #funciones para la creacion de pdf
from reportlab.lib.styles import getSampleStyleSheet #funciones para la creacion de pdf
from _d_c import alerta_ok, eliminar_doc, crear_edit_documento
import getpass
import ctypes
import sys
import getpass
#funciones para liberal espacio

def Informe_rendimiento():
    if is_admin():
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        process = subprocess.Popen("perfmon /report", startupinfo=startupinfo, shell=True)
        alerta_ok("NetAplication", "Alerta", "Debes aceptar permisos administrador para poder ejecutar esta funcion, puedes volver a intentar.")
        alerta_ok("NetAplication", "Aviso", "El proceso se continuara ejecutando si despues de 1 minuto no ves el archivo generado en tu escritorio, o te sale un error en ese caso ejecute el codigo '10' para reparar archivos dañados, reinice y vuelva a intentar.")
    else:
        alerta_ok("NetAplication", "Alerta", "Debes aceptar permisos administrador para poder ejecutar esta funcion, puedes volver a intentar.")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



def dar_mode():
    dark_app_mode = ['reg.exe', 'add', 'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize', 
           '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '0', '/f']
    dark_windows_mode = ['reg.exe', 'add', 'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize', 
               '/v', 'SystemUsesLightTheme', '/t', 'REG_DWORD', '/d', '0', '/f']

    subprocess.run(dark_app_mode)
    subprocess.run(dark_windows_mode)

def white_mode():
    light_app_mode = ['reg.exe', 'add', 'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize', 
           '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '1', '/f']
    light_windows_mode = ['reg.exe', 'add', 'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize', 
               '/v', 'SystemUsesLightTheme', '/t', 'REG_DWORD', '/d', '1', '/f']

    subprocess.run(light_app_mode)
    subprocess.run(light_windows_mode)


#Consulta NOMBRE DE EQUIPO
def Nombre_equipo():
	nombre_equipo = os.environ.get('COMPUTERNAME') or os.environ.get('HOSTNAME')
	return nombre_equipo

def output_consulta(comando, nombre_archivo): #obtener output de un comando en archivo
	ruta = "lib/data"
	output = subprocess.check_output(comando, shell=True, text=True)
	archivo = os.path.join(ruta, nombre_archivo)
	with open(archivo, "w") as f:
		f.write(output)

def crear_pdf(archivo_texto, nombre_pdf):
    imagen_pdf = "lib/data/img.png"
    ruta = "lib/data"
    # Leer el contenido del archivo de texto
    archivo_texto = os.path.join(ruta, archivo_texto)
    with open(archivo_texto, "r") as f:
        contenido = f.read()

    # Crear un documento PDF
    archivo_pdf = os.path.join(ruta, nombre_pdf)
    doc = SimpleDocTemplate(archivo_pdf, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Agregar el banner
    banner = Image(imagen_pdf, width=400, height=100)
    story.append(banner)

    # Agregar el contenido del archivo de texto
    story.append(Preformatted(contenido, styles["Code"]))
    # Guardar el documento PDF
    doc.build(story)

def abrir_archivo(archivo):
    ruta_escritorio = os.path.join(os.environ["USERPROFILE"], "Desktop")
    ruta_archivo = os.path.join(ruta_escritorio, archivo)
    os.startfile(ruta_archivo)

def copiar_pdf_a_escritorio(archivo_pdf):
    ruta_escritorio = os.path.join(os.environ["USERPROFILE"], "Desktop")
    shutil.copy2(archivo_pdf, ruta_escritorio)
    alerta_ok("NetAplication", "Consulta", "Terminado, el archivo se creo en escritorio.")

def copiar_lib(archivo):
    ruta_lib = os.path.join("lib/binc")
    shutil.copy2(archivo, ruta_lib)

def obtener_aplicaciones_instaladas(archivo_salida):
    ruta = "lib/data"
    archivo_salida = os.path.join(ruta, archivo_salida)
    cmd1 = 'powershell "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize"'
    resultado1 = subprocess.check_output(cmd1, shell=True)
    resultado1 = resultado1.decode('cp1252')
    with open(archivo_salida, 'w') as f:
        f.write("############################\n")
        f.write("#    Lista Aplicaciones    #\n")
        f.write("############################\n\n")
        f.write(resultado1)

def Driver_backup():
    ruta_bat = crear_bat()
    user = getpass.getuser()
    alerta_ok("NetAplication", "Drivers Backup", f"{user} Para crear el backup necesitas permisos de administrador deberas proporcinar al contraseña")
    password = getpass.getpass()
    ruta = "temp"
    doc = "bin"
    pc_pass_final = "Pc_Pass = " + str(password)
    crear_edit_documento(doc, pc_pass_final, 10, ruta)
    copiar_lib("lib/temp/bin")
    alerta_ok("NetAplication", "Drivers Backup", "Iniciando, este proceso puede tardar no cerrar la ventana hasta que no finalize, si te pide permisos administrador aceptalos para continuar sin errores, presiona aceptar para continuar")
    subprocess.run(['cmd', '/c', ruta_bat])
    alerta_ok("NetAplication", "Drivers Backup", "Copia de seguridad Iniciada, cuando termine se creara en el Escritorio/Drivers Backup, espere hasta que el proceso finalize")

def crear_bat():
    nombre_bat = "Driver.bat"
    ruta = "lib/data"
    # Crear la ruta del archivo .bat en la carpeta actual
    ruta_bat = os.path.join(ruta, nombre_bat)
    # Verificar si el archivo .bat ya existe o no
    if not os.path.exists(ruta_bat):
        # Si no existe, crear un archivo vacío con ese nombre y ruta
        os.open(ruta_bat, os.O_CREAT)
    # Abrir el archivo .bat en modo escritura y codificación utf-8
    archivo = io.open(ruta_bat, "w", encoding="utf-8")
    # Escribir el código del archivo .bat en el archivo
    archivo.write("@echo off\n")
    archivo.write("REM Usa la variable %USERPROFILE% para crear la ruta de la carpeta del backup en el escritorio del usuario actual\n")
    archivo.write("set driver_folder=\"%USERPROFILE%\\Desktop\\Drivers Backup\"\n")
    archivo.write("REM Comprueba si el script se está ejecutando como administrador\n")
    archivo.write("net session >nul 2>&1\n")
    archivo.write("if %errorLevel% == 0 (\n")
    archivo.write("    REM Si es así, comprueba si la carpeta del backup existe o no\n")
    archivo.write("    if exist %driver_folder% (\n")
    archivo.write("        REM Si existe, continúa con el proceso\n")
    archivo.write("        echo La carpeta del backup ya existe\n")
    archivo.write("    ) else (\n")
    archivo.write("        REM Si no existe, crea la carpeta\n")
    archivo.write("        echo La carpeta del backup no existe, creándola...\n")
    archivo.write("        mkdir %driver_folder%\n")
    archivo.write("    )\n")
    archivo.write("    REM Ejecuta el comando para hacer el backup de drivers\n")
    archivo.write("    dism /online /export-driver /destination:%driver_folder%\n")
    archivo.write(") else (\n")
    archivo.write("    REM Si no, eleva el script a administrador y vuelve a ejecutarlo\n")
    archivo.write("    powershell -Command \"Start-Process -Verb RunAs -FilePath '%0'\"\n")
    archivo.write("    exit /b\n")
    archivo.write(")\n")
    archivo.write("pause\n")
    # Cerrar el archivo
    archivo.close()
    # Retornar la ruta del archivo .bat creado
    return ruta_bat

def lista_driver(archivo_salida):
    ruta = "lib/data"
    archivo_salida = os.path.join(ruta, archivo_salida)
    cmd1 = 'wmic path win32_pnpsigneddriver get devicename, driverversion, driverdate'
    resultado1 = subprocess.check_output(cmd1, shell=True)
    resultado1 = resultado1.decode('cp1252')
     # Verificar si el archivo de salida existe o no
    if not os.path.exists(archivo_salida):
        # Si no existe, crear un archivo vacío con ese nombre y ruta
        os.open(archivo_salida, os.O_CREAT)
    # Abrir el archivo de salida en modo escritura
    with open(archivo_salida, 'w') as f:
        f.write("############################\n")
        f.write("#      Lista Drivers       #\n")
        f.write("############################\n\n")
        f.write(resultado1)
