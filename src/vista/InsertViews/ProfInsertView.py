from tkinter import messagebox

import customtkinter as ctk

from config.settings import RESIZEABLE_H, RESIZEABLE_W

class InsertaProfesor(ctk.CTk):
    def __init__(self, controller, obtener_datos):
        super().__init__()
        self.controller = controller
        self.obtener_datos = obtener_datos
        self.configurar_ventana()
        self.construir_ventana()

    def configurar_ventana(self):
        self.title("Insertar Profesor"),
        self.geometry("300X300")
        self.resizable(RESIZEABLE_W, RESIZEABLE_H)
        self.configure(fg_color="black")

    def construir_ventana(self):
        frame = ctk.CTkFrame(self, width=300, height=300)
        frame.pack_propagate(False)
        frame.pack()

        titulo = ctk.CTkLabel(frame, text="Insertar Profesor", font=("Arial", 20))
        titulo.pack(pady=10)

        self.nombreEntry = ctk.CTkEntry(frame, placeholder_text="Nombre")
        self.nombreEntry.pack(pady=10)

        self.apellidosEntry = ctk.CTkEntry(frame, placeholder_text="Apellidos")
        self.apellidosEntry.pack(pady=10)

        self.cargoEntry = ctk.CTkEntry(frame, placeholder_text="Cargo")
        self.cargoEntry.pack(pady=10)

        self.correoEntry = ctk.CTkEntry(frame, placeholder_text="Correo")
        self.correoEntry.pack(pady=10)

        self.guardarBtn = ctk.CTkButton(frame, text_color="white", text="Guardar", command=self.insertar_profesor)
        self.guardarBtn.pack(pady=10)

    def insertar_profesor(self):
        nombre = self.nombreEntry.get().strip()
        apellidos = self.apellidosEntry.get().strip()
        cargo = self.cargoEntry.get().strip()
        correo = self.correoEntry.get().strip()

        texto = self.controller.agregar_profesor(nombre, apellidos, cargo, correo)
        messagebox.showwarning("Info", texto)
        self.obtener_datos()