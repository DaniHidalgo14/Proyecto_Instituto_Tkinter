from tkinter import messagebox

import customtkinter as ctk
from config.settings import FONDO_FRAME, alumnos
from src.controlador.alum_controller import AlumController
#➕❌🔄⬅️➡️

class Alumnos(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = AlumController()
        self.construir_contenedor()
        self.id_alumno = 1
        self.obtener_datos()

    def construir_contenedor(self):

        titulo = ctk.CTkLabel(self, text="Alumnos", text_color="white", font=("Arial", 20))
        titulo.pack(pady=20)

        botonesCRUD = ctk.CTkFrame(self, width=530, height=50)
        botonesCRUD.configure(fg_color="black")
        botonesCRUD.pack_propagate(False)
        botonesCRUD.pack(padx=10)

        anadirBtn = ctk.CTkButton(botonesCRUD, text_color="white", text="➕ Añadir", fg_color="green")
        anadirBtn.pack(side="left", padx=20)

        modifBtn = ctk.CTkButton(botonesCRUD, text_color="white", text="🔄 Modificar", fg_color="blue")
        modifBtn.pack(side="left", padx=20)

        eliminarBtn = ctk.CTkButton(botonesCRUD, text="❌ Eliminar", text_color="white", fg_color="red", command=self.eliminar_alumno)
        eliminarBtn.pack(side="right", padx=20)

        frame_alumno = ctk.CTkFrame(self, width=530, height=250)
        frame_alumno.pack_propagate(False)
        frame_alumno.configure(fg_color="black")
        frame_alumno.pack(pady=10)

        frame_botones = ctk.CTkFrame(frame_alumno, width=530, height=50)
        frame_botones.pack_propagate(False)
        frame_botones.configure(fg_color="black")
        frame_botones.pack(pady=10, padx=10)


        self.anteriorBtn = ctk.CTkButton(frame_botones, text="⬅️ Anterior", text_color="white", hover_color="blue", command=self.anterior)
        self.anteriorBtn.pack(side="left")

        self.siguienteBtn = ctk.CTkButton(frame_botones, text="Siguiente ➡️", text_color="white", hover_color="blue", command=self.siguiente)
        self.siguienteBtn.pack(side="right")

        self.datos_alumno = ctk.CTkFrame(frame_alumno, width=530, height=200)
        self.datos_alumno.pack_propagate(False)
        self.datos_alumno.configure(fg_color="white")
        self.datos_alumno.pack(pady=10, side="top", padx=10)

    def clear(self):
        for widget in self.datos_alumno.winfo_children():
            widget.destroy()

    def obtener_datos(self):
        alumno = self.controller.carga_alumno(self.id_alumno)

        nombreLabel = ctk.CTkLabel(self.datos_alumno, text=alumno[1], text_color="black")
        nombreLabel.pack()

        edadLabel = ctk.CTkLabel(self.datos_alumno, text=str(alumno[2]), text_color="black")
        edadLabel.pack()

        telLabel = ctk.CTkLabel(self.datos_alumno, text=str(alumno[3]), text_color="black")
        telLabel.pack()

        dirLabel = ctk.CTkLabel(self.datos_alumno, text=alumno[4], text_color="black")
        dirLabel.pack()

        cursoLabel = ctk.CTkLabel(self.datos_alumno, text=f"Curso nº:{str(alumno[5])}", text_color="black")
        cursoLabel.pack()

    def siguiente(self):
        self.clear()
        self.id_alumno += 1
        exito = self.controller.comprobar_alumno(self.id_alumno)
        if exito:
            self.obtener_datos()
            self.anteriorBtn.configure(state="normal")
        else:
            self.siguienteBtn.configure(state="disabled")


    def anterior(self):
        self.clear()
        self.id_alumno -= 1
        exito = self.controller.comprobar_alumno(self.id_alumno)
        if exito:
            self.obtener_datos()
            self.siguienteBtn.configure(state="normal")
        else:
            self.anteriorBtn.configure(state="disabled")

    def eliminar_alumno(self):
        exito = self.controller.comprobar_alumno(self.id_alumno)
        if exito:
            respuesta = messagebox.askyesno("Confirmar", f"Desea eliminar el alumno {self.id_alumno}")

            if respuesta:
                self.controller.eliminar_alumno(self.id_alumno)
                messagebox.showinfo("Informacion", f"Alumno {self.id_alumno} eliminado")

        else:
            messagebox.showinfo("Advertencia", f"Alumno {self.id_alumno} no se encuentra en la tabla")