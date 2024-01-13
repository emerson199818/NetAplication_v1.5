import subprocess
import os
import psutil
from colorama import init, Fore, Style #formato de colores, pip install colorama
import time
import win32com.client

#BLUETOOTH
def check_bluetooth_status():
    output = subprocess.check_output("wmic path win32_networkadapter where \"Name like '%Bluetooth%'\" get NetEnabled", shell=True).decode()
    if "TRUE" in output:
        return f"{Fore.CYAN}ON. {Fore.GREEN}"
    else:
        return f"{Fore.RED}OFF.{Fore.GREEN}"

def clear_netifaces_cache():
    try:
        psutil._psplatform.net_io_counters.cache_clear()
    except AttributeError:
        # Este método solo está disponible en versiones más recientes de psutil
        pass

def get_wifi_interface_status():
    try:
        wifi_interface = None
        interfaces = psutil.net_if_stats().keys()
        
        for interface in interfaces:
            if "Wi-Fi" in interface or "Wireless" in interface:
                wifi_interface = interface
                break

        if wifi_interface:
            if psutil.net_if_stats()[wifi_interface].isup:
                return f"{Fore.CYAN}ON. {Fore.GREEN}"
            else:
                return f"{Fore.RED}OFF.{Fore.GREEN}"
        else:
            return f"{Fore.RED}BAD.{Fore.GREEN}"

    except Exception as e:
        return f"{Fore.RED}Error: {e}.{Fore.GREEN}"

def get_firewall_status():
    try:
        firewall_manager = win32com.client.Dispatch("HNetCfg.FwMgr")
        profile = firewall_manager.LocalPolicy.CurrentProfile
        return f"{Fore.CYAN}ON. {Fore.GREEN}" if profile.FirewallEnabled else f"{Fore.RED}OFF.{Fore.GREEN}"
    except Exception as e:
        return f"Error al obtener el estado del Firewall: {e}"

def check_status():
    while True:
        clear_netifaces_cache()
        w_status = get_wifi_interface_status()
        b_status = check_bluetooth_status()
        f_status = get_firewall_status()
        return w_status, b_status, f_status
        time.sleep(5)
