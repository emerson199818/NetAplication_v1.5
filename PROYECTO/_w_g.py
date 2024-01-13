from pywinauto import Desktop
import win32gui
import win32api
import win32con
import os

def cambiar_icono(hwnd, icon_path):
    # Cargar el archivo de icono
    icono = win32gui.LoadImage(0, icon_path, win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)

    # Establecer el nuevo icono para la ventana
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_SMALL, icono)
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_BIG, icono)

def buscar_ventana_contiene_titulo(titulo):
    def enum_ventanas(hwnd, ventanas):
        if win32gui.IsWindowVisible(hwnd) and len(win32gui.GetWindowText(hwnd)) > 0:
            ventanas.append((hwnd, win32gui.GetWindowText(hwnd)))

    ventanas = []
    win32gui.EnumWindows(enum_ventanas, ventanas)

    for ventana in ventanas:
        hwnd, ventana_titulo = ventana
        if titulo in ventana_titulo:
            return hwnd

    return None

def buscar_ventana(self):
    while True:
        window_handle = win32gui.FindWindow(None, self)
        if window_handle != 0:
            return window_handle


def win_menu_p(): #ventana menu principal (horizontal, vertical, ancho, largo)
    #ventana
    window_title = "NetAplication"
    window_handle = buscar_ventana_contiene_titulo(window_title)

    if window_handle: #si, aplicar camvios
        win32gui.MoveWindow(window_handle, 200, 100, 725, 605, True)
        win32gui.SetWindowText(window_handle, "NetAplication")
        # Ruta del archivo de icono
        icon_path = "lib/data/icono.ico"
        # Cambiar el icono de la ventana
        cambiar_icono(window_handle, icon_path)
    else:
        print(f"No se encontró una ventana con el título '{window_title}'")

def win_banners():
    #ventana
    windows_select = "Seleccionar NetAplication"
    windows_select1 = "Seleccionar LOGIN"
    window_title = "LOGIN" #ventana con este titulo
    window_title1 = "NetAplication"
    window_handle = win32gui.FindWindow(None, window_title) #se detecte la ventana con el titulo
    
    window_handle1 = win32gui.FindWindow(None, window_title1) #se detecte la ventana con el titulo

    console_window = win32gui.GetForegroundWindow()

    if window_handle: #si, aplicar cambios
        win32gui.MoveWindow(window_handle, 310, 180, 725, 350, True)
        win32gui.SetWindowText(window_handle, "NetAplication")
        # Ruta del archivo de icono
        icon_path = "lib/data/icono.ico"
        # Cambiar el icono de la ventana
        cambiar_icono(window_handle, icon_path)
    elif window_handle1:
        win32gui.MoveWindow(window_handle1, 310, 180, 725, 350, True)
        win32gui.SetWindowText(window_handle1, "NetAplication")
        # Ruta del archivo de icono
        icon_path = "lib/data/icono.ico"
        # Cambiar el icono de la ventana
        cambiar_icono(window_handle1, icon_path)
    elif windows_select:
        win32gui.MoveWindow(windows_select, 310, 180, 725, 350, True)
        win32gui.SetWindowText(windows_select, "NetAplication")
        # Ruta del archivo de icono
        icon_path = "lib/data/icono.ico"
        # Cambiar el icono de la ventana
        cambiar_icono(windows_select, icon_path)
    elif windows_select1:
        win32gui.MoveWindow(windows_select1, 310, 180, 725, 350, True)
        win32gui.SetWindowText(windows_select1, "NetAplication")
        # Ruta del archivo de icono
        icon_path = "lib/data/icono.ico"
        # Cambiar el icono de la ventana
        cambiar_icono(windows_select1, icon_path)
    else:
        win32gui.MoveWindow(console_window, 310, 180, 725, 350, True)
        win32gui.SetWindowText(console_window, "NetAplication")
        # Ruta del archivo de icono
        icon_path = "lib/data/icono.ico"
        # Cambiar el icono de la ventana
        cambiar_icono(console_window, icon_path)
        

    
def win_login(): #ventana menu principal (horizontal, vertical, ancho, largo)
    #ventana
    window_title = "NetAplication" #ventana con este titulo
    window_handle = win32gui.FindWindow(None, window_title) #se detecte la ventana con el titulo

    if window_handle: #si, aplicar cambios
        win32gui.MoveWindow(window_handle, 520, 210, 300, 300, True)
        win32gui.SetWindowText(window_handle, "LOGIN")
        # Ruta del archivo de icono
        icon_path = "lib/data/icono.ico"
        # Cambiar el icono de la ventana
        cambiar_icono(window_handle, icon_path)
    else:
        print(f"No se encontró una ventana con el título '{window_title}'")

def cerrar_win(title):
    windows = Desktop(backend="uia").windows()
    for window in windows:
        if title in window.window_text():
            window.close()
            break
