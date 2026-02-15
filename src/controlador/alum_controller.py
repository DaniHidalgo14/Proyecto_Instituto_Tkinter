"""
Controlador de Alumno - Intermediario entre Vista y Modelo
"""
from src.modelo.alum_model import AlumModel
class AlumController:
    def __init__(self):
        self.model = AlumModel()

    def listar_alumnos(self):
        """Obtiene lista de alumnos"""
        return self.model.obtener_todos()

    def agregar_alumno(self, nombre, edad, telefono, direccion, cod_curso) -> str:
        """Agrega un nuevo alumno"""
        id_alumno_nuevo = -1
        if not nombre or not edad or not telefono or not direccion or not cod_curso:
            return False, "Todos los campos son obligatorios", id_alumno_nuevo

        exito, id_alumno_nuevo = self.model.insertar_alumno(nombre, edad, telefono, direccion, cod_curso)

        if exito:
            return True, "Alumno insertado exitosamente", id_alumno_nuevo
        else:
            return False, "El id ya existe", id_alumno_nuevo

    def eliminar_alumno(self, id_alumno):
        """Elimina un alumno"""
        self.model.eliminar(id_alumno)
        return True, "Alumno eliminado"

    def carga_alumno(self, id_alumno):
        """Carga un alumno por ID"""
        return self.model.cargar(id_alumno)

    def edita_alumno(self, item,  nombre, edad, telefono, direccion, cod_curso):
        """Edita un alumno por ID"""
        self.model.editar(item,  nombre, edad, telefono, direccion, cod_curso)
        return True, "Alumno editado"

    def comprobar_curso(self, cod_curso) -> bool:
        return self.model.comprobar_cod_curso(cod_curso)

    def obtener_ids_alumnos(self):
        return self.model.obtener_ids_alumnos()