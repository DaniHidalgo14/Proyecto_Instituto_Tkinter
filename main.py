from database.base_de_datos import BaseDeDatos
from src.vista.mainView import Mainview

base_de_datos = BaseDeDatos()

app = Mainview()
app.mainloop()