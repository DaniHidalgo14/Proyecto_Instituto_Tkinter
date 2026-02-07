"""
Configuración de la aplicación
"""

# Tema CustomTkinter
THEME_MODE = "dark"
COLOR_THEME = "blue"
FONDO_FRAME = "#121212"

#Propiedades de Ventanas
APP_NAME = "Gestion de Instituto"
WINDOW_SIZE = "1000X700"
APP_VERSION = "3.0.0"
RESIZEABLE_W = False
RESIZEABLE_H = False

#BASE DE DATOS PROVISIONAL
usuarios = {"danibnk14" : "12345", "juanmiS" : "98765"}
alumnos = {"1": {"Nombre Completo" : "Jose Lopez Vargas", "Edad" : 19, "Telefono" : 47667454, "Direccion" : "Calle Domingo 21"},
           "2": {"Nombre Completo" : "Angel Lopez Ruiz", "Edad" : 19, "Telefono" : 6734745, "Direccion" :  "Calle Benedicto 13"}}
materiales = {
    "1" : {"Nombre" : "Pizarra digital", "Costo" : 3500, "Aula" : "Iris"},
    "2" : {"Nombre" : "Ordenador", "Costo" : 275, "Aula" : "Iris"},
    "3" : {"Nombre" : "Servidor", "Costo" : 1200, "Aula" : "Iris"},
}
aulas = {
    "1" : {"Nombre" : "Iris", "Curso" : "1º DAM"},
    "2" : {"Nombre" : "Hermes", "Curso" : "2º DAM"},
    "3" : {"Nombre" : "Jupiter", "Curso" : "1º DAW"},
    "4" : {"Nombre" : "Zeus", "Curso" : "1º DAW"}
}
asignaturas = {
    "1" : {"Nombre" : "Sistemas de gestion empresarial", "Horas" : 40, "Profesor" : "Jorge"},
    "2" : {"Nombre" : "Programacion de Servicios", "Horas" : 35, "Profesor" : "Tomas"},
    "3" : {"Nombre" : "Acceso a Datos", "Horas" : 28, "Profesor" : "Carmen"},
    "4" : {"Nombre" : "Desarrollo Web en Servidor", "Horas" : 42, "Profesor" : "Monica"},
    "5" : {"Nombre" : "Despliegue de apps Web", "Horas" : 50, "Profesor" : "Tomas"},
    "6" : {"Nombre" : "Diseño de interfaces Web", "Horas" : 40, "Profesor" : "Monica"}
}


# ruta para Configurar icono de la ventana (se configura en el main)
from resources import resource_path
try:
    ICON_PATH = resource_path("resources\iconos\icono.ico")
except Exception as e:
    print(f"Error al cargar icono:  {e}")


##### 3ª version del proyecto
import os
import sys
def get_db_path() -> bytes:
    #Poner la ubicacion de la BD en una carpeta escribible donde se
    # guardan los datos de la aplicacion según el propio sistema.

    if getattr(sys, 'frozen', False):
        # .exe:  Guardar en AppData
        appdata = os.getenv('APPDATA')
        db_dir = os.path.join(appdata, APP_NAME)
    else:
        # Desarrollo
        db_dir = os.path.join(os.path.abspath("."), "database")

    os.makedirs(db_dir, exist_ok=True)
    return os.path.join(db_dir, "instituto.db")

DB_PATH = get_db_path()

# Debug: Ver dónde está la BD
if __name__ == "__main__":
    print(f"BD en: {DB_PATH}")
