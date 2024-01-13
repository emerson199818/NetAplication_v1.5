import subprocess 
from _d_c import alerta_ok
from _l import agregar_log
from _t_d import limpiar, stop
from _w_g import cambiar_icono, cerrar_win
import win32gui
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def buscar_ventana(title):#bsuavr ventana cuyo titulo inicie por el titlo proporcionado
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd).startswith(title):
            hwnds.append(hwnd)
        return True
    
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0] if hwnds else None

def ventana(titulo):
    window_title = titulo
    agregar_log("Busqueda ventana iniciada.")
    while True: 
        window_handle = buscar_ventana(window_title)
        if window_handle:
            agregar_log("Ventana encontrada")
            win32gui.MoveWindow(window_handle, 310, 180, 500, 400, True)
            win32gui.SetWindowText(window_handle, "Reparador Archivos corruptos")
            icon_path = "lib/data/icono.ico"
            cambiar_icono(window_handle, icon_path)
            agregar_log("Cambios a ventana realizados.")
            break

def fix_files():
    agregar_log("Se inicio el reparador de archivos corruptos")
    alerta_ok("Fix Files", "Aviso, Leer antes de continuar.", "Esto puede tardar varios minutos, no cerrar la ventana hasta que finalize el proceso, si le pide permisos administrador aceptelos.")
    if is_admin():
        subprocess.run("DISM /Online /Cleanup-Image /CheckHealth", shell=True)
        subprocess.run("DISM /Online /Cleanup-Image /ScanHealth", shell=True)
        subprocess.run("DISM /Online /Cleanup-Image /RestoreHealth", shell=True)
        subprocess.run("sfc /scannow", shell=True)
        alerta_ok("Fix Files", "Fix Files", "Los archivos se repararon correctamente, reinicie el ordenador")
        cerrar_win("Fix Files")

def main():
	stop(1)
	limpiar()
	ventana("Fix Files")
	fix_files()


main()