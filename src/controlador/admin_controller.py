"""
Controlador de Usuario - Intermediario entre Vista y Modelo
"""
from src.modelo.admins_model import AdminModel

class AdminController:
    def __init__(self):
        self.model = AdminModel()

    def inicio_sesion(self, usuario : str, password :str) -> str:
        valido = self.model.iniciar_sesion(usuario, password)
        if valido:
            return f"Cargando datos usuario {usuario}", True
        else:
            return f"Error: usuario {usuario} no encontrado", False