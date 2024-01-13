import os

ruta = "__pycache__"  # Cambia esto a la ruta de la carpeta donde se encuentran los archivos

for nombre_archivo in os.listdir(ruta):
    if nombre_archivo.endswith(".cpython-310.pyc"):
        nuevo_nombre = nombre_archivo.replace(".cpython-310", "")
        vieja_ruta = os.path.join(ruta, nombre_archivo)
        nueva_ruta = os.path.join(ruta, nuevo_nombre)
        os.rename(vieja_ruta, nueva_ruta)
        print(f"Archivo renombrado: {nombre_archivo} -> {nuevo_nombre}")
