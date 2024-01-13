from _t_d import limpiar, pc_user_name, hora, fecha_dia, stop
from colorama import init, Fore, Style #formato de colores, pip install colorama
import os
from _d_c import crear_edit_documento, crear_folder, local_map, alerta_ok
import ctypes

#pedir datos
user_mail = ""
user_pass = ""
Hora = hora()
Fecha, Dia = fecha_dia()

def pedir_datos():
	global user_mail, user_pass
	print(" "*9 + "Inicio de session")
	stop(1)
	alerta_ok("LOGIN", "Introduce correo GMAIL", "Favor introducir correo real, sera usado para la recepcion de correos de NOTIFICACIONES posteriores, si introduce un correo y contraseña erroneos, al usar una funcion de alerta por correo habra un error, no se enviara ningun correo ya que no existe")
	print(" "*13 + "E-mail:")
	user_mail = input(" "*7) 
	print(" "*13 + "Password:")
	user_pass = input(" "*7)


def crear_doc():
	global Hora, Fecha, Dia
	ruta = "lib/temp"
	crear_folder(ruta)
	ciudad, region, pais = local_map()
	pc_nickname = pc_user_name()
	doc = "bin"
	mail_final = "user_mail = " + str(user_mail)
	pass_final = "user_pass = " + str(user_pass)
	ciudad_final = "Cuidad = " + str(ciudad)
	region_final = "Region = " + str(region)
	pais_final = "Pais = " + str(pais)
	pc_nickname_final = "Windows User = " + str(pc_nickname)
	Hora_Inicial = "Hora Inicial = " + str(Hora)
	Fecha_Inicial = "Fecha Inicial = " + str(Fecha)
	Dia_Inicial = "Dia = " + str(Dia)
	crear_edit_documento(doc, mail_final, 1, ruta) 
	crear_edit_documento(doc, pass_final, 2, ruta)
	crear_edit_documento(doc, ciudad_final, 3, ruta)
	crear_edit_documento(doc, region_final, 4, ruta)
	crear_edit_documento(doc, pais_final, 5, ruta)
	crear_edit_documento(doc, pc_nickname_final, 6, ruta)
	crear_edit_documento(doc, Hora_Inicial, 7, ruta)
	crear_edit_documento(doc, Fecha_Inicial, 8, ruta)
	crear_edit_documento(doc, Dia_Inicial, 9, ruta)
	ctypes.windll.kernel32.SetFileAttributesW(doc, 2)

 