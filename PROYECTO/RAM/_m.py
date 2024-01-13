import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from _d_c import alerta_ok
import os
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

def enviar_correo_gmail(Subject, mensaje, archivo_adjunto=None):
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

    # Crear objeto MIMEMultipart
    msg = MIMEMultipart()

    # Configurar remitente, destinatario y asunto del correo
    msg['From'] = gmail_username
    msg['To'] = destination
    msg['Subject'] = Subject

    # Agregar el cuerpo del mensaje
    #mensaje = 'Hola, este es el contenido del correo.'
    msg.attach(MIMEText(mensaje, 'plain'))
    
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
        except:
            pass
    # Enviar el correo electrónico
    smtp.send_message(msg)

    # Cerrar conexión SMTP
    smtp.quit()
    alerta_ok("NetAplication", "Consulta", "Correo enviado correctamente.")
