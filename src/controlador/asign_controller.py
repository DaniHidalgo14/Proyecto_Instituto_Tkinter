from src.modelo.asign_model import AsignsModel


class AsignsController:
    def __init__(self):
        self.model = AsignsModel()

    def listar_asignaturas(self):
        asignaturas = self.model.obtener_todos()
        return asignaturas

    def obtener_asignatura(self, cod):
        asignatura = self.model.obtener_asignatura(cod)
        return asignatura

    def insertar_nuevo(self, nombre, horas, cod_curso, cod_prof):
        mensj = self.model.insertar_asignatura(nombre, horas, cod_curso, cod_prof)
        return mensj

    def actualizar_asignatura(self, cod, nombre, horas, cod_curso, cod_prof):
        mensj = self.model.editar_asignatura(nombre, horas, cod_curso, cod_prof, cod)
        return mensj

    def eliminar(self, cod):
        mensj = self.model.eliminar_asignatura(cod)
        return mensj