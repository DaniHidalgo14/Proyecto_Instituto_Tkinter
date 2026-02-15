import sqlite3

from config.settings import DB_PATH
from database.queries.mats_queries import *


class MaterialesModel:
    def insertar_material(self, nombre, coste, cod_aula):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(INSERT_MATERIALES, (nombre, coste, cod_aula, ))
            conn.commit()
            return "Material insertado correctamente"

    def editar_material(self, cod, nombre, coste, cod_aula):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(UPDATE_MATERIALES, (nombre, coste, cod_aula, cod))
            conn.commit()
            return f"Material actualizado: {cod}"

    def eliminar_material(self, cod):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(DELETE_MATERIALES, (cod,))
            conn.commit()
            return f"Material eliminado: {cod}"

    def obtener_todos(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_ALL_MATERIALES)
            materiales = cursor.fetchall()
            return materiales

    def obtener_material(self, cod):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_MATERIAL, (cod, ))
            material = cursor.fetchone()
            return material