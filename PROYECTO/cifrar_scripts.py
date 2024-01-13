import os
import shutil
import subprocess

ruta_1 = "Scripts"
ruta_origen = "Scripts/__pycache__"  # Ruta de la carpeta donde se encuentran los archivos
ruta_destino = "Scripts/tls"       # Ruta de la carpeta donde deseas mover los archivos

subprocess.run(["python", "-m", "compileall", ruta_1])

for nombre_archivo in os.listdir(ruta_origen):
    if nombre_archivo.endswith(".cpython-310.pyc"):
        nuevo_nombre = nombre_archivo.replace(".cpython-310", "")
        vieja_ruta = os.path.join(ruta_origen, nombre_archivo)
        nueva_ruta = os.path.join(ruta_origen, nuevo_nombre)
        os.rename(vieja_ruta, nueva_ruta)
        print(f"Archivo renombrado: {nombre_archivo} -> {nuevo_nombre}")

        # Mover el archivo renombrado a la nueva carpeta
        nueva_ruta_destino = os.path.join(ruta_destino, nuevo_nombre)
        shutil.copy(nueva_ruta, nueva_ruta_destino)
        print(f"Archivo copiados a {nueva_ruta_destino}")

"""
ESTE SCRIPT ME COJE TODOS LOS ARCHVIOS DE LA RUTA_1, 
Y LOS CIFRA DEJA LOS SCRIPT CON UN NOMRE AL FINAL .CPYTHON-310.PYC,
LUEGO LOS MANDA A LA CARPETA __pycache__, LUEGO DE ESA CARPETA SE LE BORRAN LOS NOMBRES Y SE JETAN,
CON EL NOMBRE POR DEFECTO + EL .PYC, Y SE COPIAN A TLS.
"""