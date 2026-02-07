import sqlite3

from config.settings import DB_PATH
from database.base_de_datos import BaseDeDatos
from src.vista.mainView import Mainview

base_de_datos = BaseDeDatos()

app = Mainview()
app.mainloop()

'''with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute('select * from alumnos')
    usuarios = cursor.fetchall()
    print(usuarios)'''