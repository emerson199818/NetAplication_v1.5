import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from _d_c import uso_documento, alerta_ok
import os
from _l import agregar_log
"""
SMTP_HOTMAIL = 'smtp.office365.com'
"""
def uso_documento(self): #para sacar datos del documento y usarlos
    with open(self, 'r') as f:
        for linea in f:
            nombre, valor = linea.strip().split(' = ')
            if valor.lower() == 'true':
                valor = True
            elif valor.lower() == 'false':
                valor = False
            globals()[nombre] = valor
            agregar_log("Desde _mail se accedio al documento bin, se obtuvieron algunos datos")

def enviar_correo_gmail(Subject, mensaje, archivo_adjunto=None):
    agregar_log("Se preapara todo oara enviar un correo")
    uso_documento("lib/temp/bin")
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    destination = user_mail
    gmail_username = 'notificaciones.netaplication@gmail.com'
    gmail_password = 'wfosikbmcxfkexuo'
    # Crear objeto SMTP y establecer conexión
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls()

    # Iniciar sesión en la cuenta de Gmail
    smtp.login(gmail_username, gmail_password)
    agregar_log("Se inicio secion en el host")

    # Crear objeto MIMEMultipart
    msg = MIMEMultipart()

    # Configurar remitente, destinatario y asunto del correo
    msg['From'] = gmail_username
    msg['To'] = destination
    msg['Subject'] = Subject
    agregar_log(f"se inicialiazo un correo desde local, para {destination}, con sujeto {Subject}.")

    # Agregar el cuerpo del mensaje
    #mensaje = 'Hola, este es el contenido del correo.'
    msg.attach(MIMEText(mensaje, 'plain'))
    agregar_log("Se creo el campo del mensaje")
    
    # Adjuntar archivo al correo
    #archivo_adjunto = 'password.txt'  # Ruta completa del archivo que deseas adjuntar

    if archivo_adjunto is not None:
        try:
            with open(archivo_adjunto, 'rb') as adjunto:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(adjunto.read())

            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {archivo_adjunto}')
            msg.attach(part)
        except FileNotFoundError:
            agregar_log(f"No se encontró el archivo: {archivo_adjunto}")

    # Enviar el correo electrónico
    smtp.send_message(msg)
    agregar_log("Mensaje de Notificacion enviado correctamente")

    # Cerrar conexión SMTP
    smtp.quit()
    agregar_log("Saliendo de funcion correo.")
    alerta_ok("NetAplication", "Consulta", "Correo enviado correctamente.")



