import os
import sqlite3

from config.settings import DB_PATH
from database.queries.scripts import CREAR_TABLAS, CARGAS_INICIALES


class BaseDeDatos:
    def __init__(self):
        self.construccion()

    def construccion(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self.crear_tablas()
        print(f"Comprobando / Creando base de datos en {DB_PATH}")


        bd_nueva = not os.path.exists(DB_PATH)
        print(bd_nueva)

        if bd_nueva:
            self.cargas_iniciales()


    def crear_tablas(self):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('pragma foreign_keys = ON;')
                cursor.executescript(CREAR_TABLAS)
                conn.commit()
                print("Base de datos construida correctamente")
        except sqlite3.OperationalError:
            print(f"Error: no se pudo construir la base de datos")


    def cargas_iniciales(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.executescript(CARGAS_INICIALES)
            conn.commit()
            print("Cargas iniciales insertadas correctamente")