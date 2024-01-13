#importando librerias y funciones
from colorama import init, Fore, Style #formato de colores, pip install colorama

init() #inicializando colorama

colores = [
    Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW,
    Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

print("SIN ESTILO")
for i in colores:
    nombre_color = i + "Texto en " + i + "color" + Style.RESET_ALL
    print(nombre_color)

print("\nCON MIN ESTILO")
print(Fore.BLACK + Style.DIM + "Texto en color")
print(Fore.RED + Style.DIM + "Texto en color")
print(Fore.GREEN + Style.DIM + "Texto en color")
print(Fore.YELLOW + Style.DIM + "Texto en color")
print(Fore.BLUE + Style.DIM + "Texto en color")
print(Fore.MAGENTA + Style.DIM + "Texto en color")
print(Fore.CYAN + Style.DIM + "Texto en color")
print(Fore.WHITE + Style.DIM + "Texto en color")


print("\nCON BRIGHT ESTILO")
print(Fore.BLACK + Style.BRIGHT + "Texto en color")
print(Fore.RED + Style.BRIGHT + "Texto en color")
print(Fore.GREEN + Style.BRIGHT + "Texto en color")
print(Fore.YELLOW + Style.BRIGHT + "Texto en color")
print(Fore.BLUE + Style.BRIGHT + "Texto en color")
print(Fore.MAGENTA + Style.BRIGHT + "Texto en color")
print(Fore.CYAN + Style.BRIGHT + "Texto en color")
print(Fore.WHITE + Style.BRIGHT + "Texto en color")

input("Presiona Enter para salir...")
