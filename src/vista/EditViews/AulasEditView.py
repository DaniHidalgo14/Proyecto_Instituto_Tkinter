from tkinter import messagebox

import customtkinter as ctk

class AulasEditView(ctk.CTk):
    def __init__(self, controller, obtener_datos_aula, cod_aula):
        super().__init__()
        self.construir_ventana()
        self.controller = controller
        self.obtener_datos_aula = obtener_datos_aula
        self.cod_aula = cod_aula

    def construir_ventana(self):
        self.title("Editar aula")
        self.geometry("300x300")
        titulo = ctk.CTkLabel(self, text="Editar aula", font=("Arial", 20))
        titulo.pack(pady=10)

        self.nombreEntrada = ctk.CTkEntry(self, placeholder_text="Nombre aula")
        self.nombreEntrada.pack(pady=10)

        self.cursoEntrada = ctk.CTkEntry(self, placeholder_text="Codigo de curso")
        self.cursoEntrada.pack(pady=10)

        guardarBtn = ctk.CTkButton(self, text="Guardar", command=self.editar_aula)
        guardarBtn.pack(pady=10)

    def editar_aula(self):
        nombre = self.nombreEntrada.get()
        cod_aula = self.cursoEntrada.get()

        mensaje = self.controller.actualizar_aula(self.cod_aula, nombre, cod_aula)
        messagebox.showinfo("Informacion", mensaje)
        self.obtener_datos_aula()
        self.destroy()