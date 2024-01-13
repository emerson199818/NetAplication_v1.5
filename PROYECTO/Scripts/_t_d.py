import os #usar funciones o comandos del sistema tanto widnows como linux
import random #para generador ramdon
import time #para generador ramdon
import datetime #para sacar informacion de fecha y hora
from colorama import init, Fore, Style #formato de colores, pip install colorama
import getpass
from _d_c import crear_edit_documento
from _m_h_e import Nombre_equipo
import subprocess
import shutil

def abrir_archivo_notepad(archivo):
    ruta = "lib/data"
    ruta_archivo = os.path.join(ruta, archivo)
    subprocess.Popen(["notepad.exe", ruta_archivo])

def fecha_dia(): #se obtiene la fecha y dia de la sema
    
    fecha_actual = datetime.date.today()
    dia_semana = fecha_actual.weekday()

    #convirtiendo numero de dia en nombre
    dias_semana = ['lunes....', 'martes...', 'miércoles', 'jueves...', 'viernes..', 'sábado...', 'domingo..']
    nombre_dia = dias_semana[dia_semana]

    return fecha_actual, nombre_dia

def hora():
    hora = datetime.datetime.now() #obtener hora
    hora_new = hora.strftime("%H:%M:%S")
    return hora_new

def limpiar():
    if os.name == 'nt':  # Verificar si el sistema operativo es Windows
        _ = os.system('cls')
    else:  # Para sistemas operativos Unix/Linux/Mac
        _ = os.system('clear')

#usernmae pc
def pc_user_name():
    return getpass.getuser()

def stop(self):
    time.sleep(self)

def generador_aleatorio(n1, n2): #generar un numero aleatorio para usar el time.sleep
    random.seed(time.time())
    return random.randint(n1, n2)

tb = generador_aleatorio(1,2)

def print_banners_1():
    print(bannerR1)
    stop(tb)
    limpiar()
    print(bannerR2)
    stop(tb)
    limpiar()
    print(bannerR3)
    stop(tb)
    limpiar()
    print(bannerA1)
    stop(tb)
    limpiar()
    print(bannerA2)
    stop(tb)
    limpiar()
    print(bannerA3)
    stop(tb)
    limpiar()
    print(bannerV1)
    stop(tb)

def print_banners_2():
    limpiar()
    print(bannerV2)
    stop(1.2)
    limpiar()
    print(bannerV3)
    stop(1.2)
    limpiar()
    print(bannerV4)
    stop(1.5)
    limpiar()
    print(bannerV5)
    stop(1.2)
    limpiar()
    print(bannerV6)
    stop(1)
    limpiar()

#mensaje correo
#candado funcion login
candado1 = f"""{Fore.RED}{Style.DIM}
       ####################
       #  .--.            #
       # /.-. '----------.#
       # \\' .--"--""-"-'  #
       #  '--'            #
       ####################
{Style.RESET_ALL}"""

candado2 = f"""{Fore.GREEN}{Style.DIM}
       ####################
       #  .--.            #
       # /.-. '----------.#
       # \\' .--"--""-"-'  #
       #  '--'            #
       ####################
{Style.RESET_ALL}"""

#inicio de banner de carga
#ROJAS
bannerR1 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.RED}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.RED}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.RED}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.RED}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.RED}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.RED}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.RED}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.RED}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.RED}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██{Fore.GREEN}                                  █=====
===={Fore.RED}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██{Fore.GREEN}                                  █=====
======{Fore.RED}▀▀▀{Fore.GREEN}=={Fore.RED}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.RED}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

bannerR2 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.RED}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.RED}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.RED}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.RED}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.RED}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.RED}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.RED}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.RED}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.RED}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██{Fore.GREEN}                               █=====
===={Fore.RED}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██{Fore.GREEN}                               █=====
======{Fore.RED}▀▀▀{Fore.GREEN}=={Fore.RED}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.RED}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

bannerR3 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.RED}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.RED}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.RED}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.RED}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.RED}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.RED}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.RED}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.RED}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.RED}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██ ██{Fore.GREEN}                            █=====
===={Fore.RED}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██ ██{Fore.GREEN}                            █=====
======{Fore.RED}▀▀▀{Fore.GREEN}=={Fore.RED}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.RED}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

#AMARILLAS
bannerA1 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.YELLOW}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.YELLOW}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.YELLOW}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.YELLOW}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.YELLOW}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.YELLOW}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.YELLOW}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.YELLOW}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.YELLOW}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██{Fore.GREEN}                         █=====
===={Fore.YELLOW}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██{Fore.GREEN}                         █=====
======{Fore.YELLOW}▀▀▀{Fore.GREEN}=={Fore.YELLOW}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.YELLOW}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

bannerA2 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.YELLOW}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.YELLOW}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.YELLOW}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.YELLOW}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.YELLOW}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.YELLOW}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.YELLOW}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.YELLOW}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.YELLOW}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██{Fore.GREEN}                      █=====
===={Fore.YELLOW}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██{Fore.GREEN}                      █=====
======{Fore.YELLOW}▀▀▀{Fore.GREEN}=={Fore.YELLOW}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.YELLOW}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

bannerA3 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.YELLOW}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.YELLOW}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.YELLOW}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.YELLOW}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.YELLOW}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.YELLOW}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.YELLOW}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.YELLOW}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.YELLOW}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN}                   █=====
===={Fore.YELLOW}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN}                   █=====
======{Fore.YELLOW}▀▀▀{Fore.GREEN}=={Fore.YELLOW}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.YELLOW}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

#VERDES
bannerV1 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.GREEN}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.GREEN}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.GREEN}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.GREEN}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.GREEN}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.GREEN}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.GREEN}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.GREEN}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.GREEN}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██                █=====
===={Fore.GREEN}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██                █=====
======{Fore.GREEN}▀▀▀{Fore.GREEN}=={Fore.GREEN}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.GREEN}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

bannerV2 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.GREEN}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.GREEN}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.GREEN}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.GREEN}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.GREEN}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.GREEN}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.GREEN}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.GREEN}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.GREEN}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██ ██             █=====
===={Fore.GREEN}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██ ██             █=====
======{Fore.GREEN}▀▀▀{Fore.GREEN}=={Fore.GREEN}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.GREEN}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

bannerV3 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.GREEN}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.GREEN}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.GREEN}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.GREEN}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.GREEN}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.GREEN}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.GREEN}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.GREEN}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.GREEN}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██ ██ ██          █=====
===={Fore.GREEN}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██ ██ ██          █=====
======{Fore.GREEN}▀▀▀{Fore.GREEN}=={Fore.GREEN}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.GREEN}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

bannerV4 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.GREEN}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.GREEN}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.GREEN}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.GREEN}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.GREEN}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.GREEN}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.GREEN}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.GREEN}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.GREEN}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██ ██ ██ ██       █=====
===={Fore.GREEN}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██ ██ ██ ██       █=====
======{Fore.GREEN}▀▀▀{Fore.GREEN}=={Fore.GREEN}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.GREEN}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

bannerV5 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.GREEN}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.GREEN}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.GREEN}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.GREEN}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.GREEN}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.GREEN}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.GREEN}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.GREEN}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.GREEN}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██ ██ ██ ██ ██    █=====
===={Fore.GREEN}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██ ██ ██ ██ ██    █=====
======{Fore.GREEN}▀▀▀{Fore.GREEN}=={Fore.GREEN}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.GREEN}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

bannerV6 = f"""{Fore.GREEN}{Style.DIM}======================================================================================
==========={Fore.GREEN}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___=========
========{Fore.GREEN}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)========
====={Fore.GREEN}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __====
===={Fore.GREEN}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \===
==={Fore.GREEN}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
==={Fore.GREEN}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/===
==={Fore.GREEN}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}====================================================| |======
==={Fore.GREEN}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}=================█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█=====
==={Fore.GREEN}▐████████████▀▀██████{Fore.GREEN}==================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██ ██ ██ ██ ██ ██ █=====
===={Fore.GREEN}▐████▀██████  █████{Fore.GREEN}===================█ {Fore.RED}██ ██ ██ {Fore.YELLOW}██ ██ ██{Fore.GREEN} ██ ██ ██ ██ ██ ██ █=====
======{Fore.GREEN}▀▀▀{Fore.GREEN}=={Fore.GREEN}█████▌ ████▀{Fore.GREEN}===================█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█=====
============{Fore.GREEN}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
======================================================================================
{Style.RESET_ALL}"""

#banner home
def menu_banner():
    fecha, dia = fecha_dia()
    pc_name = pc_user_name()
    print(f"""{Fore.GREEN}{Style.DIM}=====================================================================================
=========={Fore.CYAN}▄██▄      ▄▄{Fore.GREEN}================== ______                  __      ___       ==
======={Fore.CYAN}  ▐███▀     ▄███▌{Fore.GREEN}================|  ____|                 \ \    / (_)      ==
===={Fore.CYAN}▄▀ ▄█▀▀        ▀██ {Fore.GREEN}=================| |__   _ __ ___   ___ _ _\ \  / / _ _ __  ==
==={Fore.CYAN}█   ██               {Fore.GREEN}================|  __| | '_ ` _ \ / _ \ '__\ \/ / | | '_ \ ==
=={Fore.CYAN}█▌  ▐██  ▄██▌  ▄▄▄   ▄{Fore.GREEN}================| |____| | | | | |  __/ |   \  /  | | |_) |==
=={Fore.CYAN}██  ▐██▄ ▀█▀   ▀██  ▐▌{Fore.GREEN}================|______|_| |_| |_|\___|_|    \/   |_| .__/ ==
=={Fore.CYAN}██▄ ▐███▄▄  ▄▄▄ ▀▀ ▄██{Fore.GREEN}================                                    | |    ==
=={Fore.CYAN}▐███▄██████▄ ▀ ▄█████▌{Fore.GREEN}================ █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ====
=={Fore.CYAN}▐████████████▀▀██████{Fore.GREEN}================= █ ██ ██ ██ ██ ██ ██ ██ ██{Fore.CYAN}  {dia}{Fore.GREEN}  █ ====
==={Fore.CYAN}▐████▀██████  █████{Fore.GREEN}================== █ ██ ██ ██ ██ ██ ██ ██ ██{Fore.CYAN} {fecha}{Fore.GREEN}  █ ====
====={Fore.CYAN}▀▀▀{Fore.GREEN}=={Fore.CYAN}█████▌ ████▀{Fore.GREEN}================== █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ ====
==========={Fore.CYAN}▀▀███ ▀▀▀{Fore.GREEN}=================================================================
=====================================================================================\n       HOLA : {Fore.CYAN}{pc_name}{Fore.GREEN}.                           ¿Como va tu {dia}?
=====================================================================================
<-------------El USO DE ESTAS HERRAMIENTAS QUEDA BAJO TU RESPONSABILIDAD------------>
====================================================================================={Style.RESET_ALL}""")


#capa 0
Menu_P = f"""{Fore.GREEN}                                    <MENU PRINCIPAL>
                   ##################################################
                   # [{Fore.CYAN}0{Fore.GREEN}] --------------> {Fore.RED}REPORTAR BUG{Fore.GREEN} <------------ #
                   # [{Fore.CYAN}1{Fore.GREEN}] HERRAMIENTAS EQUIPO / SERVIDOR.            #
                   # [{Fore.CYAN}2{Fore.GREEN}] HERRAMIENTAS REDES.                        #
                   # [{Fore.CYAN}99{Fore.GREEN}] ----------------> SALIR <---------------- #
                   ##################################################{Style.RESET_ALL}"""

#capa 1
Menu_H_E = f"""{Fore.GREEN}                            <HERRAMINETAS EQUIPO / SERVIDOR>
                   ##################################################
                   # [{Fore.CYAN}0{Fore.GREEN}] --------------> {Fore.RED}REPORTAR BUG{Fore.GREEN} <------------ #
                   # [{Fore.CYAN}3{Fore.GREEN}] NOMBRE DE EQUIPO Y USUARIO.                #
                   # [{Fore.CYAN}4{Fore.GREEN}] INFORMACION DETALLADA EQUIPO.              #
                   # [{Fore.CYAN}5{Fore.GREEN}] MONITORES.                                 #
                   # [{Fore.CYAN}6{Fore.GREEN}] LISTA DE APPS.                             #
                   # [{Fore.CYAN}7{Fore.GREEN}] DARK OR WHITE WINDOWS MODE.                #
                   # [{Fore.CYAN}8{Fore.GREEN}] DRIVERS.                                   #
                   # [{Fore.CYAN}9{Fore.GREEN}] LIMPIAR TEMPORALES Y LIBERAR ESPACIO.      #
                   # [{Fore.CYAN}10{Fore.GREEN}] REPARAR ARCHIVOS CORRUPTOS.               #
                   # [{Fore.CYAN}11{Fore.GREEN}] GENERAR INFORMES DE RENDIMIENTO.          #
                   # [{Fore.CYAN}12{Fore.GREEN}] DESACTIVAR SERVICIOS.                     #
                   # [{Fore.CYAN}98{Fore.GREEN}] ----------------> VOLVER <--------------- #
                   # [{Fore.CYAN}99{Fore.GREEN}] ----------------> SALIR <---------------- #
                   ##################################################{Style.RESET_ALL}"""

#capa 2
Menu_H_R = f"""{Fore.GREEN}                                  <HERRAMINETAS REDES>
                   ##################################################
                   # [{Fore.CYAN}0{Fore.GREEN}] --------------> {Fore.RED}REPORTAR BUG{Fore.GREEN} <------------ #
                   # [{Fore.CYAN}13{Fore.GREEN}] CONEXION SSH.                             #
                   # [{Fore.CYAN}14{Fore.GREEN}] CONEXION TELNET.                          #
                   # [{Fore.CYAN}15{Fore.GREEN}] REDES GUARDADAS.                          #
                   # [{Fore.CYAN}16{Fore.GREEN}] MAC ADAPTADORES DE RED.                   #
                   # [{Fore.CYAN}17{Fore.GREEN}] INTERFACES.                               #
                   # [{Fore.CYAN}18{Fore.GREEN}] ESTADISTICAS TCP/IP.                      #
                   # [{Fore.CYAN}19{Fore.GREEN}] FUNCIONES PING.                           #
                   # [{Fore.CYAN}98{Fore.GREEN}] ----------------> VOLVER <--------------- #
                   # [{Fore.CYAN}99{Fore.GREEN}] ----------------> SALIR <---------------- #
                   ##################################################{Style.RESET_ALL}"""

#capa 3
Menu_MONITORES = f"""{Fore.GREEN}                                       <MONITORES>
                   ##################################################
                   # [{Fore.CYAN}0{Fore.GREEN}] --------------> {Fore.RED}REPORTAR BUG{Fore.GREEN} <------------ #
                   # [{Fore.CYAN}20{Fore.GREEN}] RAM.                                      #
                   # [{Fore.CYAN}21{Fore.GREEN}] BATERIA.                                  #
                   # [{Fore.CYAN}22{Fore.GREEN}] WIRELESS (wifi).                          #
                   # [{Fore.CYAN}98{Fore.GREEN}] ----------------> VOLVER <--------------- #
                   # [{Fore.CYAN}99{Fore.GREEN}] ----------------> SALIR <---------------- #
                   ##################################################{Style.RESET_ALL}"""

