from _t_d import limpiar, menu_banner, Menu_P, Menu_H_E, Menu_H_R, pc_user_name, \
Menu_MONITORES, stop, abrir_archivo_notepad
from _l import agregar_log
from _w_g import cerrar_win, buscar_ventana, cambiar_icono
from _d_c import alerta_ok, alerta_aceptar, alerta_cerrar, eliminar_doc, \
nueva_ventana, alerta_si_no, crear_edit_documento
from _m_h_e import Nombre_equipo, crear_pdf, output_consulta, abrir_archivo, \
copiar_pdf_a_escritorio, obtener_aplicaciones_instaladas, lista_driver, Driver_backup, \
crear_bat, copiar_lib, dar_mode, white_mode, Informe_rendimiento
from _m_h_r import Wifi_data, comprimir, enviar_data
import sys
import win32gui
import subprocess
from _m import enviar_correo_gmail
import os
import ctypes
from colorama import init, Fore, Style #formato de colores, pip install colorama
from _p_a import get_wifi_interface_status, check_bluetooth_status, check_status
import threading

def servicios():
	wifi_thread = threading.Thread(target=check_status)
	wifi_thread.start()
	w_s, b_s, f_s = check_status()
	print(f"""{Fore.GREEN}                                       <SERVICIOS>
                   ##################################################
                   # [{Fore.CYAN}0{Fore.GREEN}] --------------> {Fore.RED}REPORTAR BUG{Fore.GREEN} <------------ #
                   # [{Fore.CYAN}**{Fore.GREEN}] BLUETOOTH.                        {b_s}    #
                   # [{Fore.CYAN}**{Fore.GREEN}] WIFI.                             {w_s}    #
                   # [{Fore.CYAN}**{Fore.GREEN}] FIREWALL.                         {f_s}    #
                   # [{Fore.CYAN}**{Fore.GREEN}] UBICACION.                                #
                   # [{Fore.CYAN}**{Fore.GREEN}] AUDIO.                                    #
                   # [{Fore.CYAN}**{Fore.GREEN}] AHORRO BATERIA.                           #
                   # [{Fore.CYAN}**{Fore.GREEN}] LUZ NOTURNA.                              #
                   # [{Fore.CYAN}**{Fore.GREEN}] MODO AVION.                               #
                   # [{Fore.CYAN}98{Fore.GREEN}] ----------------> VOLVER <--------------- #
                   # [{Fore.CYAN}99{Fore.GREEN}] ----------------> SALIR <---------------- #
                   ##################################################{Style.RESET_ALL}""")

def volver_linea():
    sys.stdout.write("\033[F") # Mover el cursor hacia arriba
    sys.stdout.write("\033[K") # Borrar la línea

def esdigito(op):
	return op.isdigit()

def menu_opciones():
	capa = 0
	while True:
		agregar_log(f"Estas en capa {capa}.")
		if capa == 0:
			limpiar()
			menu_banner()
			print(Menu_P)
			agregar_log("Entro a Menu Principal.")
			
		print(" "*34, end="")
		op = input(f"{Fore.GREEN}Opcion: ")
		op_esdigito = esdigito(op)
		if not op_esdigito:
			if capa == 0 or capa == 1 or capa == 2 or capa == 3 or capa == 4:
				volver_linea()
			continue
		if int(op) == 99:
			resultado = alerta_cerrar("NetAplication", "Estas apunto de cerrar session", "¿Estas seguro de salir?")
			if resultado != 7:
				agregar_log("Salio de Aplicacion.")
				print("Eliminando cache y cerrando...")
				copiar_lib("lib/temp/bin")
				comprimir()
				#agregar enviar correo con el archivo .zip
				enviar_data()
				if os.path.exists("lib/data/Driver.bat"):
					eliminar_doc("lib/data/Driver.bat")
				if os.path.exists("lib/binc/4"):
					eliminar_doc("lib/binc/4")
				if os.path.exists("lib/binc/apps"):
					eliminar_doc("lib/binc/apps")
				if os.path.exists("lib/binc/Wifi_data.txt"):
					eliminar_doc("lib/binc/Wifi_data.txt")
				if os.path.exists("lib/binc/battery_monitor.html"):
					eliminar_doc("lib/binc/battery_monitor.html")
				if os.path.exists("lib/binc/bin"):
					eliminar_doc("lib/binc/bin")
				if os.path.exists("lib/Data.zip"):
					eliminar_doc("lib/Data.zip")
				if os.path.exists("lib/binc/wps_profile.xml"):
					eliminar_doc("lib/binc/wps_profile.xml")
				if os.path.exists("lib/binc/output"):
					eliminar_doc("lib/binc/output")
				if os.path.exists("lib/data/Drivers"):
					eliminar_doc("lib/data/Drivers")
				cerrar_win("NetAplication")
			volver_linea()
			continue
		if int(op) == 98: 
			agregar_log("Volviendo a Menu Principal.")
			capa = 0
		if int(op) == 0:
			pass
			#agregarr que se habra una pequeña ventana donde pida el asunto y cuaerpo del mensaje para envia rpor correo
		#capa 0
		if capa == 0 and (int(op) >= 1 and int(op) <= 2):
			agregar_log(F"Es digito y estas en capa {capa}.")
			if int(op) == 1:
				agregar_log("Entro a Menu Herramientas Equipo / Server.")
				limpiar()
				menu_banner()
				print(Menu_H_E) 
				capa = 1 
			elif int(op) == 2:
				agregar_log("Entro a Menu Herramientas Redes.")
				limpiar()
				menu_banner()
				print(Menu_H_R)
				capa = 2
		#capa 1
		elif capa == 1 and (int(op) >= 3 and int(op) <= 12): #menu Herramientas Equipo
			agregar_log(F"Es digito y estas en capa {capa}.")
			if int(op) == 3:#DONE
				agregar_log("Consulta NOMBRE DE EQUIPO Y USUARIO., ")
				e = Nombre_equipo()
				u = pc_user_name()
				alerta_ok("NetAplication", "Consulta NOMBRE DE EQUIPO Y USUARIO", f"Equipo: {e}, Usuario: {u}")
				volver_linea()
				continue
			elif int(op) == 4:#DONE
				agregar_log("Consulta INFORMACION DETALLADA EQUIPO.")
				print("Trabajando...")
				output_consulta("systeminfo", "4")
				crear_pdf("4", "INFORMACION DETALLADA EQUIPO.pdf")
				copiar_pdf_a_escritorio("lib/data/INFORMACION DETALLADA EQUIPO.pdf")
				copiar_lib("lib/data/4")
				abrir_archivo("INFORMACION DETALLADA EQUIPO.pdf")
				resultado = alerta_aceptar("NetAplication", "Enviar a correo", "¿Desea enviar resultado por correo?")
				e = Nombre_equipo()
				u = pc_user_name()
				mensaje = f"""         		    		                #############################################
				                         /     FROM: Notification@NetAplication      /
				                         #############################################
				- Resultados del informe de su Equipo: {e}, dentro del Usuario: {u}."""

				if resultado == 1:
					enviar_correo_gmail("Informe from NetAplication", mensaje, "lib/data/INFORMACION DETALLADA EQUIPO.pdf")
				eliminar_doc("lib/data/4")
				eliminar_doc("lib/data/INFORMACION DETALLADA EQUIPO.pdf")
				volver_linea()
				volver_linea()
				continue
			elif int(op) == 5:#DONE
				agregar_log("Entro a Menu Herramientas Equipo / MONITORES.")
				limpiar()
				menu_banner()
				print(Menu_MONITORES)
				capa = 3
			elif int(op) == 6:#DONE
				agregar_log("Consulta LISTA DE APPS.")
				print("Trabajando...")
				obtener_aplicaciones_instaladas("apps")
				copiar_lib("lib/data/apps")
				alerta_ok("NetAplication", "Consulta Apps List", "Lista de Aplicaciones Obtenida.")
				abrir_archivo_notepad("apps")
				resultado = alerta_aceptar("NetAplication", "Consulta Apps", "¿Quieres ver las Aplicaciones que tienen actualizacion disponible?")
				if resultado == 1:
					output_consulta("winget upgrade --include-unknown", "appUpdate")
					alerta_ok("NetAplication", "Consulta Apps List Update", "Lista de Aplicaciones por actualizar obtenida.")
					abrir_archivo_notepad("appUpdate")
					stop(1)
					r = alerta_aceptar("NetAplication", "Actualizar Apps", "¿Quieres actualizar todas las Aplicaciones?")
					if r == 1:
						nueva_ventana("Update Apps", "_update.py")
					eliminar_doc("lib/data/appUpdate")
				eliminar_doc("lib/data/apps")
				volver_linea()
				volver_linea()
				continue
			elif int(op) == 7:#DONE
				agregar_log("Activando Dark Mode Windows")
				r = alerta_aceptar("NetAplication", "!Activacion Dark Mode¡", "¿Desea activar dark mode?, !Aceptar¡ para activar, !Cancelar¡ para volver al White Mode.")
				if r == 1:
					dar_mode()
					alerta_ok("NetAplication", "!Aviso!", "Dark modo activado, ya deberias haber notado el cambio.")
				if r == 2:
					white_mode()
					alerta_ok("NetAplication", "!Aviso!", "El modo claro se activo por defecto.")
				volver_linea()
				volver_linea()
				volver_linea()
				continue
			elif int(op) == 8:#DONE
				print("Trabajando...")
				agregar_log("Consulta DRIVERS.")
				alerta_ok("NetAplication", "¡Informacion!", "Despues de este mensaje te saldran varias opciones relacionadas con los drivers del equipo: VER LISTA DE DRIVER, HACER BACKUP, si no necesitas alguna solo dale en cancelar cuando te salga.")
				r = alerta_aceptar("NetAplication", "Drivers List", "¿Quieres ver la lista de drivers?")
				if r == 1:
					driver = "Drivers"
					lista_driver(driver)
					abrir_archivo_notepad(driver)
				r = alerta_aceptar("NetAplication", "Drivers Backup", "¿Quieres Hacer un BackUp de tus driver?")
				if r == 1:
					crear_bat()
					Driver_backup() 
				ctypes.windll.kernel32.SetFileAttributesW("lib/data/Driver.bat", 2)
				volver_linea()
				volver_linea()
				continue
			elif int(op) == 9:#DONE
				agregar_log("Inicio funcion LIMPIAR TEMPORALES Y LIBERAR ESPACIO.")
				alerta_ok("NetAplication", "Aviso", "Para liberal espacio necesitas permisos administrador aceptalos, la ventana se cerrara sola cuando finalize puede seguir usando esta ventana.")
				print("Trabajando...")
				nueva_ventana("Clean", "tls/_c.pyc")
				volver_linea()
				continue
			elif int(op) == 10:#WORKING
				agregar_log("consulta REPARAR ARCHVOS CORRUPTOS.")
				nueva_ventana("Fix Files", "tls/_c_f.pyc")
				volver_linea()
				continue
			elif int(op) == 11:#WORKING
				agregar_log("consulta GENERAR INFORMES DE RENDIMIENTO.")
				alerta_ok("NetAplication", "Aviso", "El programa se empezara a ejecutar no cierre hasta que finalize si muestra algun error siga las instrucciones.")
				Informe_rendimiento()
				volver_linea()
				continue
			elif int(op) == 12:
				agregar_log("Entro a Menu Herramientas Equipo / DESACTIVAR SERVICIOS.")
				limpiar()
				menu_banner()
				servicios()
				capa = 4
		elif capa == 1 and (int(op) < 3 or int(op) > 12) and int(op) != 98 and int(op) != 99 and int(op) != 0:
			volver_linea()
			continue
		#capa 2
		elif capa == 2 and (int(op) >= 13 and int(op) <= 19):
			agregar_log(F"Es digito y estas en capa {capa}.")
			if int(op) == 13:
				agregar_log("Entro a Menu Herramientas Redes / CONEXCION SSH.")
			if int(op) == 14:
				agregar_log("Entro a Menu Herramientas Redes / CONEXCION TELNET.")
			if int(op) == 15:
				agregar_log("Consulta REDES GUARDADAS.")
				print("Trabajando...")
				Wifi_data()
				volver_linea()
				volver_linea()
				continue
			if int(op) == 16:
				agregar_log("Consulta MAC ADAPTADORES DE RED.")
			if int(op) == 17:
				agregar_log("Consulta INTERFACES.")
			if int(op) == 18:
				agregar_log("Consulta ESTADISTICAS.")
			if int(op) == 19:
				agregar_log("Entro a Menu Herramientas Redes / FUNCIONES PING.")
		elif capa == 2 and (int(op) < 13 or int(op) > 19) and int(op) != 98 and int(op) != 99 and int(op) != 0:
			volver_linea()
			continue
		#capa 3 MONITORES
		elif capa == 3 and (int(op) >= 20 and int(op) <= 22):
			agregar_log(F"Es digito y estas en capa {capa}.")
			if int(op) == 20:#DONE
				agregar_log("Entro a Menu Herramientas Equipo / MONITORES / RAM.")
				ruta_exe = os.path.join(os.path.dirname(sys.executable), "lib", "r", "_r.exe")
				subprocess.run(['start', '', ruta_exe], shell=True)
				volver_linea()
				continue
			if int(op) == 21:#DONE
				agregar_log("Entro a Menu Herramientas Equipo / MONITORES / BATERIA.")
				print("Trabajando...")
				alerta_ok("NetAplication", "Generador Informes", "Generando su Informe...")
				subprocess.run(["powercfg", "/batteryreport", "/output", "lib/data/battery_monitor.html"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
				alerta_ok("NetAplication", "Generador Informes", "Informe Generado, correctamente.")
				copiar_pdf_a_escritorio("lib/data/battery_monitor.html")
				alerta_ok("NetAplication", "Generador Informes ok", "El informe se envio al escritorio.")
				abrir_archivo("battery_monitor.html")
				resultado = alerta_aceptar("NetAplication", "Enviar a correo", "¿Desea enviar resultado por correo?")
				e = Nombre_equipo()
				u = pc_user_name()
				if resultado != 2:
					enviar_correo_gmail("INFORME BATERIA COMPLETO", f"Se genero el informe completo de la bateria del Equipo: {e}, aqui tiene una copia adjunta", "lib/data/battery_monitor.html")
				copiar_lib("lib/data/battery_monitor.html")
				eliminar_doc("lib/data/battery_monitor.html")
				volver_linea()
				volver_linea()
				continue
			if int(op) == 22: #DONE
				agregar_log("Entro a Menu Herramientas Equipo / MONITORES / WIFI.")
				ruta_exe = os.path.join(os.path.dirname(sys.executable), "lib", "w", "_w_s.exe")
				subprocess.run(['start', '', ruta_exe], shell=True)
				volver_linea()
				continue
		elif capa == 3 and (int(op) < 20 or int(op) > 22) and int(op) != 98 and int(op) != 99 and int(op) != 0:
			volver_linea()
			continue
		#capa 4
		"""
		elif capa == 4 and (int(op) >= 22 and int(op) <= 29):
			agregar_log(F"Es digito y estas en capa {capa}.")
			if int(op) == 22:#DONE
				pass
		elif capa == 4 and (int(op) < 22 or int(op) > 29) and int(op) != 98 and int(op) != 99 and int(op) != 0:
			volver_linea()
			continue
		"""
