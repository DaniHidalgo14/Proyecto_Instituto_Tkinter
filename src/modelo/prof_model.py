"""
Modelo de Profesor
"""
import sqlite3
from config.settings import DB_PATH
from database.queries.prof_queries import (
    SELECT_ALL_PROFESORES,
    INSERTS_PROFESORES,
    DELETE_PROFESORES,
    SELECT_PROFESOR_BY_ID,
    UPDATE_PROFESORES
)
import os

class ProfModel:

    def obtener_todos(self) -> list:
        """Obtiene todos los profesores"""
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_ALL_PROFESORES)
            usuarios = cursor.fetchall()
            return usuarios

    def crear(self, nombre, apellidos, cargo, correo) -> bool:
        """Crea un nuevo profesor"""
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(INSERTS_PROFESORES, (nombre, apellidos, cargo, correo))
                id_profesor_nuevo = cursor.lastrowid
                conn.commit()
                return True, id_profesor_nuevo
        except sqlite3.IntegrityError:
            return False

    def eliminar(self, id_profesor) -> None:
        """Elimina un profesor por ID"""
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn. cursor()
            cursor.execute(DELETE_PROFESORES, (id_profesor,))
            conn.commit()

    def cargar(self, id_profesor):
        """Carga un profesor por ID"""
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_PROFESOR_BY_ID, (id_profesor,))
            usuario = cursor.fetchone()
            return usuario

    def editar(self, id_profesor, nombre, apellidos, cargo, correo):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(UPDATE_PROFESORES, (nombre, apellidos, cargo, correo, id_profesor))
            conn.commit()