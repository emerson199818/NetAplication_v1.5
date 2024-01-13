import psutil
import time
from _d_c import alerta_Amarilla, alerta_ok, init_archivo_inicio, eliminar_doc
from _m_h_e import Nombre_equipo
from _m import enviar_correo_gmail
from _t_d import fecha_dia, hora, stop, pc_user_name, limpiar
import ctypes
import win32gui
import win32api
import win32con
from colorama import init, Fore, Style
import os

mini_banner = f"""{Fore.GREEN}{Style.DIM}#############################################
/             MONITOR MEMORIA RAM           /
#############################################{Style.RESET_ALL}"""

mini_banner1 = f"""{Fore.GREEN}{Style.DIM}
#############################################{Style.RESET_ALL}"""

def cambiar_icono(hwnd, icon_path):
    # Cargar el archivo de icono
    icono = win32gui.LoadImage(0, icon_path, win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)

    # Establecer el nuevo icono para la ventana
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_SMALL, icono)
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_BIG, icono)



def uso_documento(self): #para sacar datos del documento y usarlos
    with open(self, 'r') as f:
        for linea in f:
            nombre, valor = linea.strip().split(' = ')
            if valor.lower() == 'true':
                valor = True
            elif valor.lower() == 'false':
                valor = False 
            globals()[nombre] = valor
            #agregar_log("Desde _mail se accedio al documento bin, se obtuvieron algunos datos")


uso_documento("lib/temp/bin")
correo = user_mail

e = Nombre_equipo()
u = pc_user_name()
Fecha, Dia = fecha_dia()
Hora = hora()
window_handle = win32gui.GetForegroundWindow()

def ram(threshold):
     while True:
        memory = psutil.virtual_memory()
        elevador = pow(1024, 3)
        porcentaje_uso = memory.percent
        total_ram_instalada = round(memory.total / elevador)
        total_ram_usable = round(memory.total / elevador, 1)
        used_ram = round(memory.used / elevador, 1)
        available_ram = round(memory.available / elevador, 1)
        reserved_ram = round((total_ram_instalada - total_ram_usable), 1)
        limpiar()
        print(mini_banner)
        print(f"{Fore.GREEN}{Style.DIM}#    TOTAL RAM INSTALADA: {Fore.CYAN}{total_ram_instalada} GB{Fore.GREEN}              #")
        print(f"#    TOTAL RAM USABLE: {Fore.CYAN}{total_ram_usable} GB{Fore.GREEN}               #")
        print(f"#    TOTAL RAM USADA: {Fore.YELLOW}{used_ram} GB{Fore.GREEN}                #")
        print(f"#    TOTAL RAM DISPONIBLE: {Fore.YELLOW}{available_ram} GB{Fore.GREEN}           #")
        print(f"#    TOTAL RAM RESERVADA: {reserved_ram} GB  (System)  #")
        print(f"#    Alerta: ON {Fore.RED}{threshold}%{Fore.GREEN}   Rango Actual: {Fore.YELLOW}{porcentaje_uso}%{Fore.GREEN}   #")
        print(f"#    Accion: Notificacion a E-mail          #",end="")
        print(mini_banner1, end="")
        print(f"    Si el texto desaparece presione ENTER.{Style.RESET_ALL}")
        if porcentaje_uso > threshold:
            alerta_Amarilla("Ram Monitor", "Notificacion-Alerta", f"El uso de la RAM ha superado el {threshold}%, Porcentaje actual de uso es de {porcentaje_uso}%, se envio un correo con la informacion.")
            enviar_correo_gmail(f"Porcentaje {threshold}% superado", f"El uso de la MEMORIA RAM del EQUIPO: {e}, Usuario: {u}, supero el lumbral activado, el Dia: {Dia} - {Fecha}, a las {Hora} Horas, con una subida maxima de {porcentaje_uso}%, tome las medidas necesarias, es posible que su equipo no trabaje con normalidad, este correo es solo de uso informativo, no devolver respuesta.", "data/img.png")
        time.sleep(1.5)

def main():
    limpiar()
    win32gui.MoveWindow(window_handle, 310, 180, 400, 270, True)
    win32gui.SetWindowText(window_handle, "NetAplication - Ram Monitor")
    icon_path = "lib/data/icono.ico"
    cambiar_icono(window_handle, icon_path)
    print(mini_banner)
    print(f"{Fore.GREEN}            Equipo: {Fore.CYAN}{e}{Fore.GREEN}.")
    print(f" Introduzca el parametro de '{Fore.YELLOW}%{Fore.GREEN}' en el que se")
    print(f" generara una alerta y se enviara a {Fore.YELLOW}E-mail{Fore.GREEN}.")
    n = int(input(f"            Ingrese numero:{Fore.CYAN} "))
    print("Espere...")
    alerta_ok("Ram Monitor", "Alerta Generada", f"Se activo la alerta de {n}%, se enviara un correo de notificacion a {correo} cuando se supere ese rango")
    enviar_correo_gmail("Alerta activada", f"Se genero una alerta de {n}% en nuestra aplicacion de MONITOR RAM, el Dia: {Dia} - {Fecha} a las {Hora} Horas, seras notificado cuando el limite supere {n}%.", "data/img.png")
    ram(n)

main()

