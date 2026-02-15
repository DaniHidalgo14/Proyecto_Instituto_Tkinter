"""
Modelo de Alumno
"""
import sqlite3
from config.settings import DB_PATH
from database.queries.alum_queries import (
    SELECT_ALL_ALUMNOS,
    INSERT_ALUMNOS,
    DELETE_ALUMNO,
    SELECT_ALUMNO,
    UPDATE_ALUMNO
)

class AlumModel:

    def obtener_todos(self) -> list:
        """Obtiene todos los alumnos"""
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_ALL_ALUMNOS)
            usuarios = cursor.fetchall()
            return usuarios

    def insertar_alumno(self, nombre, edad, telefono, direccion, cod_curso) -> bool:
        """Crea un nuevo alumno"""
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(INSERT_ALUMNOS, (nombre, edad, telefono, direccion, cod_curso))
                id_alumno_nuevo = cursor.lastrowid
                conn.commit()
                return True, id_alumno_nuevo
        except sqlite3.IntegrityError:
            return False

    def eliminar(self, id_alumno) -> None:
        """Elimina un alumno por ID"""
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(DELETE_ALUMNO, (id_alumno,))
            conn.commit()

    def cargar(self, id_alumno):
        """Carga un alumno por ID"""
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_ALUMNO, (id_alumno,))
            usuario = cursor.fetchone()
            return usuario

    def editar(self, id_alumno, nombre, edad, telefono, direccion, cod_curso):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(UPDATE_ALUMNO, (nombre, edad, telefono, direccion, cod_curso, id_alumno))
            conn.commit()

    def comprobar_cod_curso(self, cod_curso) -> bool:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('select nombre from cursos where cod_curso = ?', (cod_curso,))
            curso = cursor.fetchone()
            if curso is None:
                return False
            else:
                return True

    def obtener_ids_alumnos(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT cod_alum FROM alumnos ORDER BY cod_alum")
            return [fila[0] for fila in cursor.fetchall()]
