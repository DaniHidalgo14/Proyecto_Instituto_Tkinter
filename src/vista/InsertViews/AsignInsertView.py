from tkinter import messagebox

import customtkinter as ctk

class AsignInsertView(ctk.CTk):
    def __init__(self, controller, obtener_datos_asigns):
        super().__init__()
        self.construir_ventana()
        self.controller = controller
        self.obtener_datos_asigns = obtener_datos_asigns

    def construir_ventana(self):
        self.title("Nueva asignatura")
        self.geometry("300x300")
        titulo = ctk.CTkLabel(self, text="Nueva asignatura", font=("Arial", 20))
        titulo.pack(pady=10)

        self.nombreEntrada = ctk.CTkEntry(self, placeholder_text="Nombre aula")
        self.nombreEntrada.pack(pady=10)

        self.horasEntrada = ctk.CTkEntry(self, placeholder_text="Numero de horas")
        self.horasEntrada.pack(pady=10)

        self.codProfEntrada = ctk.CTkEntry(self, placeholder_text="Codigo de profesor")
        self.codProfEntrada.pack(pady=10)

        self.codCursoEntrada = ctk.CTkEntry(self, placeholder_text="Codigo de curso")
        self.codCursoEntrada.pack(pady=10)

        guardarBtn = ctk.CTkButton(self, text="Guardar", command=self.insertar_asignatura)
        guardarBtn.pack(pady=10)

    def insertar_asignatura(self):
        nombre = self.nombreEntrada.get()
        horas = self.horasEntrada.get()
        cod_prof = self.codProfEntrada.get()
        cod_curso = self.codCursoEntrada.get()

        mensaje = self.controller.insertar_nuevo(nombre, horas, cod_prof, cod_curso)
        messagebox.showinfo("Informacion", mensaje)
        self.obtener_datos_asigns()