import sqlite3

from config.settings import DB_PATH
from database.queries.aulas_queries import *


class AulasModel:
    def insertar_aula(self, nombre, cod_curso):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(INSERT_AULA, (nombre, cod_curso))
            conn.commit()
            return "Aula insertada correctamente"

    def editar_aula(self, cod_aula, nombre, cod_curso):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(UPDATE_AULA, (nombre, cod_curso, cod_aula))
            conn.commit()
            return f"Aula actualizada: {cod_aula}"

    def eliminar_aula(self, cod):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(DELETE_AULA, (cod,))
            conn.commit()
            return f"Aula eliminada: {cod}"

    def obtener_todos(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_ALL_AULAS)
            aulas = cursor.fetchall()
            return aulas

    def obtener_aula(self, cod):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_AULA, (cod, ))
            aula = cursor.fetchone()
            return aula