"""
Controlador de Usuario - Intermediario entre Vista y Modelo
"""
from src.modelo.prof_model import ProfModel
class ProfController:
    def __init__(self):
        self.model = ProfModel()

    def listar_profesores(self):
        """Obtiene lista de usuarios"""
        return self.model.obtener_todos()

    def agregar_profesor(self, nombre, apellidos, cargo, correo) -> str:
        """Agrega un nuevo usuario"""
        id_profesor_nuevo = -1
        if not nombre or not apellidos or not correo or not cargo:
            return False, "Todos los campos son obligatorios", id_profesor_nuevo

        exito, id_profesor_nuevo = self.model.crear(nombre, apellidos, cargo, correo)

        if exito:
            return True, "Profesor insertado exitosamente", id_profesor_nuevo
        else:
            return False, "El id ya existe", id_profesor_nuevo

    def eliminar_profesor(self, id_profesor):
        """Elimina un usuario"""
        self.model.eliminar(id_profesor)
        return True, "Usuario eliminado"

    def carga_profesor(self, id_profesor):
        """Carga un usuario por ID"""
        return self.model.cargar(id_profesor)

    def edita_profesor(self, item, nombre, apellidos, cargo, correo):
        """Edita un usuario por ID"""
        self.model.editar(item, nombre, apellidos, cargo, correo)
        return True, "Usuario editado"
