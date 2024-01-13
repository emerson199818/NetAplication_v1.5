import os

ruta_exe = os.path.join(os.path.dirname(__file__), "lib", "r", "_r.exe")
print("Ruta completa al exe:", ruta_exe)
input() 


"""
from _procesosActivos import check_status

b,w,f = check_status()
print(b)
print(w)
print(f)
input()
"""

"""
import subprocess

def obtener_aplicaciones_instaladas():
    cmd = 'powershell "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize"'
    resultado = subprocess.check_output(cmd, shell=True)
    resultado = resultado.decode('cp1252')
    print(resultado)

obtener_aplicaciones_instaladas()
"""
"""abrir nueva ventana cmd
import subprocess

title = "Ram Monitor"
subprocess.Popen(f"start \"{title}\" cmd /K", shell=True)
"""

""" ventana normal no cmd facil de implementar
import tkinter as tk

root = tk.Tk()
root.title("Mi Ventana")

label = tk.Label(root, text="Hola, esta es mi nueva ventana!")
label.pack()

root.mainloop()
"""

"""mensaje alerta simple
import ctypes

def mostrar_alerta(titulo, texto):
    ctypes.windll.user32.MessageBoxW(0, texto, titulo, 0)

mostrar_alerta("Alerta", "Este es un mensaje de alerta")
"""

"""
Para mostrar un icono en el cuadro de mensaje, puedes utilizar diferentes valores para el cuarto argumento de la función `MessageBoxW()`. Los valores que puedes utilizar para mostrar diferentes iconos son los siguientes:

- `0`: No se muestra ningún icono.
- `16`: Se muestra un icono de error (un círculo rojo con una X blanca).
- `32`: Se muestra un icono de interrogación (un círculo azul con un signo de interrogación blanco).
- `48`: Se muestra un icono de advertencia (un triángulo amarillo con un signo de exclamación negro).
- `64`: Se muestra un icono de información (un círculo azul con una i blanca).

Aquí tienes un ejemplo de cómo puedes mostrar un cuadro de mensaje con un icono de error:

```python
import ctypes

def mostrar_alerta(titulo, texto):
    resultado = ctypes.windll.user32.MessageBoxW(0, texto, titulo, 16)
    return resultado

resultado = mostrar_alerta("Error", "Se ha producido un error")
```

En este ejemplo, la función `mostrar_alerta()` muestra un cuadro de mensaje con un icono de error. Puedes cambiar el valor del cuarto argumento para mostrar diferentes iconos en el cuadro de mensaje.

Espero que esto te ayude a solucionar el problema. ¿Hay algo más en lo que pueda ayudarte?
####################################3
Sí, puedes cambiar el cuarto argumento de la función `MessageBoxW()` para mostrar diferentes iconos y botones en el cuadro de mensaje y aún así capturar la respuesta del usuario. El valor devuelto por la función `MessageBoxW()` indica qué botón presionó el usuario, independientemente del icono y los botones que se muestren en el cuadro de mensaje.

Para mostrar diferentes combinaciones de iconos y botones, puedes utilizar diferentes valores para el cuarto argumento de la función `MessageBoxW()`. Los valores que puedes utilizar son los siguientes:

- `0`: Muestra un cuadro de mensaje con un solo botón "OK" y sin icono.
- `1`: Muestra un cuadro de mensaje con botones "Aceptar" y "Cancelar" y sin icono.
- `2`: Muestra un cuadro de mensaje con botones "Abortar", "Reintentar" e "Ignorar" y sin icono.
- `3`: Muestra un cuadro de mensaje con botones "Sí", "No" y "Cancelar" y sin icono.
- `4`: Muestra un cuadro de mensaje con botones "Sí" y "No" y sin icono.
- `5`: Muestra un cuadro de mensaje con botones "Reintentar" y "Cancelar" y sin icono.

Puedes combinar estos valores con los valores que te mencioné en mi respuesta anterior para mostrar diferentes iconos. Por ejemplo, si quieres mostrar un cuadro de mensaje con un icono de error y botones "Aceptar" y "Cancelar", puedes utilizar el valor `16 + 1 = 17` como cuarto argumento de la función `MessageBoxW()`. Aquí tienes un ejemplo de cómo puedes hacer esto:

```python
import ctypes

def mostrar_alerta(titulo, texto):
    resultado = ctypes.windll.user32.MessageBoxW(0, texto, titulo, 17)
    return resultado

resultado = mostrar_alerta("Error", "Se ha producido un error")
if resultado == 1:
    print("El usuario presionó Aceptar")
elif resultado == 2:
    print("El usuario presionó Cancelar")
```

En este ejemplo, la función `mostrar_alerta()` muestra un cuadro de mensaje con un icono de error y botones "Aceptar" y "Cancelar". Después de llamar a la función `mostrar_alerta()`, puedes verificar el valor devuelto para determinar qué botón presionó el usuario.

Espero que esto aclare tus dudas. ¿Hay algo más en lo que pueda ayudarte?

"""



########################################
"""#crear folder
import os

os.mkdir('mi_carpeta')
"""
#os.chdir('/ruta/a/mi_carpeta') mover por rutas
"""#crear documentos
# Reemplaza esto con la ruta del archivo que deseas crear
file_path = "ruta/del/archivo.txt"

# Crear el archivo y escribir contenido en él
with open(file_path, 'w') as file:
    file.write("Contenido del archivo")
"""
"""#comprimir folder
import os
import shutil

# Reemplaza esto con la ruta de la carpeta que deseas comprimir
folder_path = "ruta/de/la/carpeta"

# Reemplaza esto con la ruta del archivo zip que deseas crear
zip_path = "ruta/del/archivo.zip"

if os.path.exists(folder_path):
    shutil.make_archive(zip_path, 'zip', folder_path)

"""
#file.write(texto)
"""
#codigo para tmar fotos desde python
    import cv2

    # Acceder a la cámara de la PC (el índice 0 suele ser la cámara integrada)
    camara = cv2.VideoCapture(0)

    # Tomar una foto
    ret, imagen = camara.read()

    # Guardar la foto en un archivo
    if ret:
        cv2.imwrite("test/foto.jpg", imagen)

    # Liberar la cámara
    camara.release()
"""
##################
""" codigo para comprimir la carpeta.
import os
import shutil

# Reemplaza esto con la ruta de la carpeta que deseas comprimir
folder_path = "ruta/de/la/carpeta"

# Reemplaza esto con la ruta del archivo zip que deseas crear
zip_path = "ruta/del/archivo.zip"

if os.path.exists(folder_path):
    shutil.make_archive(zip_path, 'zip', folder_path)

"""

""" Eliminar aecgivos
file_path = "ruta/al/archivo.txt"

if os.path.exists(file_path):
    os.remove(file_path)
"""
