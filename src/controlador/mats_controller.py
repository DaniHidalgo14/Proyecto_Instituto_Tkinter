from src.modelo.mats_model import MaterialesModel


class MatsController:
    def __init__(self):
        self.model = MaterialesModel()

    def listar_materiales(self):
        materiales = self.model.obtener_todos()
        return materiales

    def obtener_material(self, cod):
        material = self.model.obtener_material(cod)
        return material

    def insertar_nuevo(self, nombre, coste, cod_aula):
        mensj = self.model.insertar_material(nombre, coste, cod_aula)
        return mensj

    def actualizar_mat(self, cod, nombre, coste, cod_aula):
        mensj = self.model.editar_material(cod, nombre, coste, cod_aula)
        return mensj

    def eliminar(self, cod):
        mensj = self.model.eliminar_material(cod)
        return mensj