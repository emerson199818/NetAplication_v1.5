import sys
from cx_Freeze import setup, Executable

base = None

build_exe_options = {
    "packages": ["tkinter"],
    "includes": [
    "win32gui", "win32api", "win32con", "datetime", 
    "os", "io", "time", "random", "subprocess", "shutil", 
    "requests", "getpass", "pywinauto", "ctypes", "logging",
    "sys", "reportlab", "psutil", "smtplib", "xhtml2pdf", "geocoder",
    "socket", "progress", "pywifi", "threading"
    ],
    "include_files": [
        ("lib/data", "lib/data"),
        ("Scripts/tls", "tls"),
        ("lib/r/_r.exe", "_r.exe"),
        ("lib/w/_w_s.exe", "_w_s.exe")
    ]
}

executables = [
    Executable("NetAplication.py", base=base, icon="lib/data/icono.ico")
]

setup(
    name="NetAplication",
    version="1.2",
    description="Herramientas para redes e ingenieros de sistemas.",
    options={"build_exe": build_exe_options},
    executables=executables
)


"""
PARA EJECUTAR Y CREAR EL .EXE DEL PROGRAMA EDITAR EL NOMBRE DEL .PY,
Y CORRER EN CMD ESTE COMANDO, python _compilador.py build
"""
