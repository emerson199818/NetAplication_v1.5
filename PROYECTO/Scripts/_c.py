import os
import getpass
from _d_c import alerta_ok
from _t_d import stop, limpiar
from _l import agregar_log
from _w_g import cambiar_icono, cerrar_win
import win32gui
import sys
import ctypes

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
            win32gui.SetWindowText(window_handle, "Clean")
            icon_path = "lib/data/icono.ico"
            cambiar_icono(window_handle, icon_path)
            agregar_log("Cambios a ventana realizados.")
            break

def clean():
    if is_admin():
        # Aquí va el código que requiere permisos de administrador
        os.chdir("C:\Windows")
        for filename in os.listdir("temp"):
            file_path = os.path.join("temp", filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                pass
        username = getpass.getuser()
        os.chdir(rf"C:\Users\{username}\AppData\Local")
        for filename in os.listdir("temp"):
            file_path = os.path.join("temp", filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                pass
        alerta_ok("Clean", "Clean temps", "Archivos temprales eliminados correctamente.")
        cerrar_win("Clean")
                
        
    else:
        # Si no somos administradores, volvemos a ejecutar el script con privilegios de administrador
        script = sys.argv[0]
        params = ' '.join([script] + sys.argv[1:])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)


def main():
    stop(1)
    limpiar()
    ventana("Clean")
    clean()


main()