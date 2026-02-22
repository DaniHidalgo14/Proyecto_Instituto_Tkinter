import sqlite3

from config.settings import DB_PATH
from database.queries.asign_queries import *


class AsignsModel:
    def insertar_asignatura(self, nombre, horas, cod_curso, cod_prof):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(INSERT_ASIGN, (nombre, horas, cod_curso, cod_prof))
            conn.commit()
            return "Asignatura insertada correctamente"

    def editar_asignatura(self, cod_asign, nombre, horas, cod_curso, cod_prof):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(UPDATE_ASIGN, (nombre, horas, cod_curso, cod_prof, cod_asign))
            conn.commit()
            return f"Asignatura actualizada: {cod_asign}"

    def eliminar_asignatura(self, cod):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(DELETE_ASIGN, (cod,))
            conn.commit()
            return f"Asignatura eliminada: {cod}"

    def obtener_todos(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_ALL_ASIGNS)
            asignaturas = cursor.fetchall()
            return asignaturas

    def obtener_asignatura(self, cod):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_ASIGN, (cod, ))
            asignaturas = cursor.fetchone()
            return asignaturas