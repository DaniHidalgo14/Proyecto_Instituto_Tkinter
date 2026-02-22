from src.modelo.aulas_model import AulasModel


class AulasController:
    def __init__(self):
        self.model = AulasModel()

    def listar_aulas(self):
        aulas = self.model.obtener_todos()
        return aulas

    def obtener_aula(self, cod):
        material = self.model.obtener_aula(cod)
        return material

    def insertar_nuevo(self, nombre, coste):
        mensj = self.model.insertar_aula(nombre, coste)
        return mensj

    def actualizar_aula(self, cod, nombre, cod_aula):
        mensj = self.model.editar_aula(cod, nombre, cod_aula)
        return mensj

    def eliminar(self, cod):
        mensj = self.model.eliminar_aula(cod)
        return mensj