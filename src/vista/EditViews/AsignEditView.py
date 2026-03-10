from tkinter import messagebox

import customtkinter as ctk

class AsignEditView(ctk.CTk):
    def __init__(self, controller, obtener_datos_asignaturas, cod_asign):
        super().__init__()
        self.construir_ventana()
        self.controller = controller
        self.obtener_datos_asignaturas = obtener_datos_asignaturas
        self.cod_asign = cod_asign

    def construir_ventana(self):
        self.title("Editar asignatura")
        self.geometry("300x300")
        titulo = ctk.CTkLabel(self, text="Editar asignatura", font=("Arial", 20))
        titulo.pack(pady=10)

        self.nombreEntrada = ctk.CTkEntry(self, placeholder_text="Nombre asignatura")
        self.nombreEntrada.pack(pady=10)

        self.horasEntrada = ctk.CTkEntry(self, placeholder_text="Numero de horas")
        self.horasEntrada.pack(pady=10)

        self.codCursoEntrada = ctk.CTkEntry(self, placeholder_text="Codigo de profesor")
        self.codCursoEntrada.pack(pady=10)

        self.codProfEntrada = ctk.CTkEntry(self, placeholder_text="Codigo de curso")
        self.codProfEntrada.pack(pady=10)

        guardarBtn = ctk.CTkButton(self, text="Guardar", command=self.actualizar_asignatura)
        guardarBtn.pack(pady=10)

    def actualizar_asignatura(self):
        nombre = self.nombreEntrada.get()
        horas = self.horasEntrada.get()
        cod_curso = self.codCursoEntrada.get()
        cod_prof = self.codProfEntrada.get()

        mensaje = self.controller.actualizar_asignatura(self.cod_asign, nombre, horas, cod_curso, cod_prof)
        messagebox.showinfo("Informacion", mensaje)
        self.obtener_datos_asignaturas()
        self.destroy()