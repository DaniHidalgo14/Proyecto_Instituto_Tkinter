from tkinter import messagebox

import customtkinter as ctk

class AulasInsertView(ctk.CTk):
    def __init__(self, controller, obtener_datos_aulas):
        super().__init__()
        self.construir_ventana()
        self.controller = controller
        self.obtener_datos_aulas = obtener_datos_aulas

    def construir_ventana(self):
        self.title("Nueva aula")
        self.geometry("300x300")
        titulo = ctk.CTkLabel(self, text="Nueva aula", font=("Arial", 20))
        titulo.pack(pady=10)

        self.nombreEntrada = ctk.CTkEntry(self, placeholder_text="Nombre aula")
        self.nombreEntrada.pack(pady=10)

        self.cursoEntrada = ctk.CTkEntry(self, placeholder_text="Codigo de curso")
        self.cursoEntrada.pack(pady=10)

        guardarBtn = ctk.CTkButton(self, text="Guardar", command=self.insertar_aula)
        guardarBtn.pack(pady=10)

    def insertar_aula(self):
        nombre = self.nombreEntrada.get()
        cod_curso = self.cursoEntrada.get()

        mensaje = self.controller.insertar_nuevo(nombre, cod_curso)
        messagebox.showinfo("Informacion", mensaje)
        self.obtener_datos_aulas()