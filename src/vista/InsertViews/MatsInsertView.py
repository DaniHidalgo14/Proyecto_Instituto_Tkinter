from tkinter import messagebox

import customtkinter as ctk

class MatsInsertView(ctk.CTk):
    def __init__(self, controller, obtener_datos_materiales):
        super().__init__()
        self.construir_ventana()
        self.controller = controller
        self.obtener_datos_materiales = obtener_datos_materiales

    def construir_ventana(self):
        self.title("Nuevo material")
        self.geometry("300x300")
        titulo = ctk.CTkLabel(self, text="Nuevo material", font=("Arial", 20))
        titulo.pack(pady=10)

        self.nombreEntrada = ctk.CTkEntry(self, placeholder_text="Nombre material")
        self.nombreEntrada.pack(pady=10)

        self.costeEntrada = ctk.CTkEntry(self, placeholder_text="Coste €")
        self.costeEntrada.pack(pady=10)

        self.aulaEntrada = ctk.CTkEntry(self, placeholder_text="Codigo de aula")
        self.aulaEntrada.pack(pady=10)

        guardarBtn = ctk.CTkButton(self, text="Guardar", command=self.insertar_material)
        guardarBtn.pack(pady=10)

    def insertar_material(self):
        nombre = self.nombreEntrada.get()
        coste = self.costeEntrada.get()
        cod_aula = self.aulaEntrada.get()

        mensaje = self.controller.insertar_nuevo(nombre, coste, cod_aula)
        messagebox.showinfo("Informacion", mensaje)
        self.obtener_datos_materiales()