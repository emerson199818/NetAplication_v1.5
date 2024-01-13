import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter"],
    "includes": [
    "win32gui", "win32api", "win32con", "datetime", 
    "os", "io", "time", "random", "subprocess", "shutil", 
    "requests", "getpass", "pywinauto", "ctypes", "logging",
    "sys", "reportlab", "psutil", "smtplib", "xhtml2pdf", "geocoder",
    "socket", "progress", "pywifi", "threading"
    ]
}

executables = [
    Executable("_r.py", base=None)
]

setup(
    name="rm",
    version="1.2",
    description="Monitor y generador de alertas de memoria RAM del equipo.",
    options={"build_exe": build_exe_options},
    executables=executables
)


"""
PARA EJECUTAR Y CREAR EL .EXE DEL PROGRAMA EDITAR EL NOMBRE DEL .PY,
Y CORRER EN CMD ESTE COMANDO, python _compilador.py build
"""
