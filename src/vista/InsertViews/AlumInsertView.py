from tkinter import messagebox

import customtkinter as ctk

from config.settings import RESIZEABLE_H, RESIZEABLE_W

class InsertaAlumno(ctk.CTk):
    def __init__(self, controller, obtener_datos):
        super().__init__()
        self.controller = controller
        self.obtener_datos = obtener_datos
        self.configurar_ventana()
        self.construir_ventana()

    def configurar_ventana(self):
        self.title("Insertar Alumno"),
        self.geometry("400x400")
        self.resizable(RESIZEABLE_W, RESIZEABLE_H)
        self.configure(fg_color="black")

    def construir_ventana(self):
        frame = ctk.CTkFrame(self, width=400, height=400)
        frame.pack_propagate(False)
        frame.pack()

        titulo = ctk.CTkLabel(frame, text="Insertar Alumno", font=("Arial", 20))
        titulo.pack(pady=10)

        self.nombreEntry = ctk.CTkEntry(frame, placeholder_text="Nombre Completo")
        self.nombreEntry.pack(pady=10)

        self.edadEntry = ctk.CTkEntry(frame, placeholder_text="Edad")
        self.edadEntry.pack(pady=10)

        self.telefonoEntry = ctk.CTkEntry(frame, placeholder_text="Telefono")
        self.telefonoEntry.pack(pady=10)

        self.direccionEntry = ctk.CTkEntry(frame, placeholder_text="Direccion")
        self.direccionEntry.pack(pady=10)

        self.cursoEntry = ctk.CTkEntry(frame, placeholder_text="Codigo de curso")
        self.cursoEntry.pack(pady=10)

        self.guardarBtn = ctk.CTkButton(frame, text_color="white", text="Guardar", command=self.insertar_alumno)
        self.guardarBtn.pack(pady=10)

    def insertar_alumno(self):
        nombre = self.nombreEntry.get().strip()
        edad = int(self.edadEntry.get().strip())
        telefono = int(self.telefonoEntry.get().strip())
        direccion = self.direccionEntry.get().strip()
        curso = int(self.cursoEntry.get().strip())

        texto = self.controller.agregar_alumno(nombre, edad, telefono, direccion, curso)
        messagebox.showwarning("Info", texto)
        self.obtener_datos()