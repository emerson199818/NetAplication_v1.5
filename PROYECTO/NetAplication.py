#Funciones para agregar los logs
from _l import configurar_logs, agregar_log
#Funcion ventana mas abajo le paso los parametros
from _w_g import win_banners, win_menu_p, win_login, buscar_ventana_contiene_titulo, cambiar_icono, \
cerrar_win
#Obteniendo fecha, limpiar, generador, banners
from _t_d import limpiar, stop, candado1, candado2, print_banners_1, print_banners_2, \
menu_banner, abrir_archivo_notepad
#Constructores de archivos funciones
from _d_c import init_archivo_inicio, eliminar_doc, alerta_aceptar, \
crear_folder
#Funciones login.
from _l_u import pedir_datos, crear_doc
from _m_f import menu_opciones
import ctypes
import win32gui
import os


def comprobar_login():
	agregar_log("Carga en Stop mientras se inicia session.")
	doc = "lib/temp"
	if os.path.exists(doc):
		agregar_log("La session ya esta iniciada.")
		return

	else:
		#login windows
		stop(1)
		limpiar()
		win_login()#cargar datos ventana
		agregar_log("Iniciando session for first time.")
		stop(1)
		print(" "*9 + "terminos condiciones")
		abrir_archivo_notepad("T_C_App")
		resultado = alerta_aceptar("LOGIN", "Terminos y condiciones", "¿Acepta los terminos y condiciones?")
		if resultado != 1:
			cerrar_win("LOGIN")
		print(candado1) #imprimir candado art ascii
		pedir_datos() #pidiendo datos del login
		crear_doc() #se crea el documento dentro de la ruta con los datos
		stop(2)

		limpiar()
		print(candado2)
		print(" "*9 + "session succefull")
		agregar_log("session succefull.")
		stop(1)
		agregar_log("Cerrando login.")
		print(" "*13 + "Cerrando...")
		stop(1)

def main(): 
	log_doc = "logs"
	configurar_logs(log_doc)
	agregar_log("Aplicacion NetAplication iniciados correctamente")
	init_archivo_inicio()
	crear_folder("lib/binc")
	agregar_log("Archivos de inicio creados.")
	stop(1)
	window_title = "NetAplication"
	windows_admin_title = "Administrador: NetAplication"
	agregar_log("Busqueda ventana iniciada.")
	while True:  
		window_handle = buscar_ventana_contiene_titulo(window_title)
		window_admin_handle = buscar_ventana_contiene_titulo(windows_admin_title)
		if window_handle:
			agregar_log("Ventana encontrada")
			win32gui.MoveWindow(window_handle, 310, 180, 725, 350, True)
			win32gui.SetWindowText(window_handle, "NetAplication")
			icon_path = "lib/data/icono.ico"
			cambiar_icono(window_handle, icon_path)
			agregar_log("Cambios a ventana realizados.")
			break
		elif window_admin_handle:
			agregar_log("Ventana encontrada")
			win32gui.MoveWindow(window_admin_handle, 310, 180, 725, 350, True)
			win32gui.SetWindowText(window_admin_handle, "NetAplication")
			icon_path = "lib/data/icono.ico"
			cambiar_icono(window_admin_handle, icon_path)
			agregar_log("Cambios a ventana realizados.")
			break

	stop(1)
	eliminar_doc("lib/init.bat")
	eliminar_doc("lib/init.py")
	agregar_log("Archivos de inicio Eliminados.")
	#inicio carga banners
	limpiar()
	agregar_log("Sistema iniciado correctamente.")
	print_banners_1() #llamo a funcion que imprimira baners1
	agregar_log("Inicio carga.")
	comprobar_login()

	limpiar()
	win_banners() #configuraciones ventanas para mostar el banner 2
	limpiar()
	agregar_log("Inicio carga reanurando.")
	print_banners_2() #imprimiendo banner 2

	limpiar()
	win_menu_p() #llamado a la funcion aplicar tamaños
	agregar_log("Screen tools iniciados correctamente.")
	menu_opciones()

if __name__ == '__main__':
	main()