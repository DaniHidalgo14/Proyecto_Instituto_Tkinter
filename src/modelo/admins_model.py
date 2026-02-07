from config.settings import *
import sqlite3
from database.queries.admin_queries import CREATE_TABLE_ADMINS, INSERTS_ADMINS, VALIDAR


class AdminModel:

    def iniciar_sesion(self, usuario :str, contrasena : str) -> bool:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(VALIDAR, (usuario, contrasena))
            if cursor.fetchone():
                return True
            else:
                return False