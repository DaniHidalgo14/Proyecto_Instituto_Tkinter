import sqlite3

from config.settings import DB_PATH
from database.base_de_datos import BaseDeDatos
from src.vista.mainView import Mainview

base_de_datos = BaseDeDatos()

app = Mainview()
app.mainloop()

'''with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute("""
                        SELECT a.nombre, c.trimestre1, c.trimestre2, c.trimestre3
                        FROM calificaciones c
                        JOIN asignaturas a ON c.cod_asign = a.cod_asign
                        WHERE c.cod_alum = ?
                    """, (1,))
    todos = cursor.fetchall()
    print(todos)'''

#TODO: CORREGIR ERROR DE ACTUALIZAR CALIFICACIONES