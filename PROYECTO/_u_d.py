import subprocess 
from _d_c import alerta_ok
from _l import agregar_log
from _t_d import limpiar, stop
from _w_g import cambiar_icono
import win32gui
import os

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
            win32gui.SetWindowText(window_handle, "Update Apps")
            icon_path = "lib/data/icono.ico"
            cambiar_icono(window_handle, icon_path)
            agregar_log("Cambios a ventana realizados.")
            break

def update_app():
	agregar_log("Se inicio la actualizacion de las Aplicaciones instaladas en el equipo")
	alerta_ok("Update Apps", "Aviso, Leer antes de continuar.", "Esto puede tardar varios minutos, no cerrar la ventana de actualizacion hasta que finalize el proceso si al inicio sale un mensaje de 'Error al intentar actualizar el origen: winget!', ignorelo y espere a que el proceso termine, cada que una app este lista le puede pedir permisos Administrador para hacer la instalacion del paquete, siempre presione 'aceptar' cuando esto pase, si no quiere actualizar dicho paquete presione 'cancelar' y el programa continuara con otro.")
	subprocess.run("winget upgrade --all --include-unknown", shell=True)
	alerta_ok("Update Apps", "Actualizacion Done", "Las Aplicaciones se actualizaron correctamente ya puedes cerrar esta ventana")

def main():
	stop(1)
	limpiar()
	ventana("Update Apps")
	update_app()


main()