import sqlite3

from config.settings import DB_PATH
from database.base_de_datos import BaseDeDatos
from src.vista.mainView import Mainview

base_de_datos = BaseDeDatos()

app = Mainview()
app.mainloop()

'''with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute('select * from asignaturas')
    materiales = cursor.fetchall()
    print(materiales)'''

#TODO: TERMINAR CRUD DE ASIGNATURAS(FUNCIONES EN LA VISTA Y VENTANAS DE INSERCION Y EDICION)