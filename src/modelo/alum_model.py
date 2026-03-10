"""
Modelo de Alumno
"""
import csv
import os
import sqlite3
from tkinter import messagebox

from config.settings import DB_PATH
from database.queries.alum_queries import (
    SELECT_ALL_ALUMNOS,
    INSERT_ALUMNOS,
    DELETE_ALUMNO,
    SELECT_ALUMNO,
    UPDATE_ALUMNO, OBTENER_CALIFICACIONES
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

    def obtener_calificaciones(self, cod_alum):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(OBTENER_CALIFICACIONES, (cod_alum, ))
            notas = cursor.fetchall()
            return notas

    def exportar_notas_alumno_csv(self, cod_alum):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Obtener nombre del alumno
            cursor.execute("SELECT nombreCompleto FROM alumnos WHERE cod_alum = ?", (cod_alum,))
            alumno = cursor.fetchone()

            if not alumno:
                print("Alumno no encontrado")
                return

            nombre_alumno = alumno[0]
            nombre_archivo = f"{nombre_alumno.strip()}.csv"
            escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
            ruta_csv = os.path.join(escritorio, nombre_archivo)

            # Obtener todas las asignaturas con sus notas
            cursor.execute(OBTENER_CALIFICACIONES, (cod_alum,))
            registros = cursor.fetchall()

            # Crear CSV
            with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:
                writer = csv.writer(archivo)

                # Cabeceras
                writer.writerow(["Asignatura", "1º Trimestre", "2º Trimestre", "3º Trimestre"])

                # Escribir cada asignatura con sus notas
                for asignatura, t1, t2, t3 in registros:
                    writer.writerow([asignatura, t1, t2, t3])

            print(f"CSV generado correctamente: {ruta_csv}")

    def importar_notas_alumno_csv(self, ruta_csv):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Obtener nombre del archivo sin extensión
            nombre_archivo = os.path.basename(ruta_csv)
            nombre_alumno = os.path.splitext(nombre_archivo)[0]

            # Buscar el código del alumno
            cursor.execute("SELECT cod_alum FROM alumnos WHERE nombreCompleto = ?", (nombre_alumno,))
            alumno = cursor.fetchone()

            if not alumno:
                messagebox.showerror("Error", f"Alumno '{nombre_alumno}' no encontrado en la base de datos")
                return

            cod_alum = alumno[0]

            # Leer CSV
            with open(ruta_csv, "r") as archivo:
                reader = csv.reader(archivo)
                next(reader)  # Saltar cabecera

                for fila in reader:
                    asignatura, t1, t2, t3 = fila

                    # Buscar código de asignatura
                    cursor.execute("SELECT cod_asign FROM asignaturas WHERE nombre = ?", (asignatura,))
                    asign = cursor.fetchone()

                    if not asign:
                        messagebox.showerror("Error", f"Asignatura '{asignatura}' no encontrada, saltando...")
                        continue

                    cod_asign = asign[0]

                    # Insertar o actualizar notas
                    cursor.execute("""
                        INSERT OR REPLACE INTO calificaciones
                        (trimestre1, trimestre2, trimestre3, cod_alum, cod_asign)
                        VALUES (?, ?, ?, ?, ?)
                    """, (t1, t2, t3, cod_alum, cod_asign))

            conn.commit()
            messagebox.showinfo("Informacion", f"Notas importadas correctamente para {nombre_alumno}")
