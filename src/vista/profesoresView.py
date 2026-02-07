import customtkinter as ctk
from tkinter import ttk, messagebox
from src.vista.InsertViews.ProfInsertView import InsertaProfesor
from src.vista.EditViews.ProfEditView import EditarProfesor
from ..controlador.prof_controller import ProfController

class Profesores(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = ProfController()
        self.construir_contenedor()
        self.obtener_datos()

    def construir_contenedor(self):

        titulo = ctk.CTkLabel(self, text="Direccion", text_color="white", font=("Arial", 20))
        titulo.pack(pady=20)

        botonesCRUD = ctk.CTkFrame(self, width=530, height=50)
        botonesCRUD.configure(fg_color="black")
        botonesCRUD.pack_propagate(False)
        botonesCRUD.pack(padx=10)

        anadirBtn = ctk.CTkButton(botonesCRUD, text_color="white", text="➕ Añadir", fg_color="green", command=self.insertar_profesor)
        anadirBtn.pack(side="left", padx=20)

        modifBtn = ctk.CTkButton(botonesCRUD, text_color="white", text="🔄 Modificar", fg_color="blue", command=self.editar_profesor)
        modifBtn.pack(side="left", padx=20)

        eliminarBtn = ctk.CTkButton(botonesCRUD, text="❌ Eliminar", text_color="white", fg_color="red", command=self.eliminar_profesor)
        eliminarBtn.pack(side="right", padx=20)

        frame_profesores = ctk.CTkFrame(self, width=530, height=250)
        frame_profesores.pack_propagate(False)
        frame_profesores.configure(fg_color="black")
        frame_profesores.pack(pady=10)

        self.datos_profesores = ctk.CTkFrame(frame_profesores, width=530, height=250)
        self.datos_profesores.pack_propagate(False)
        self.datos_profesores.configure(fg_color="white")
        self.datos_profesores.pack(pady=10, side="top", padx=10)

        scrollbar = ttk.Scrollbar(self.datos_profesores)
        scrollbar.pack(side="right", fill="y")

        self.tabla = ttk.Treeview(self.datos_profesores, columns=("Nombre", "Apellidos", "Cargo", "Correo"), show="headings", yscrollcommand=scrollbar.set)

        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellidos", text="Apellidos")
        self.tabla.heading("Cargo", text="Cargo")
        self.tabla.heading("Correo", text="Correo")

        self.tabla.column("Nombre", width=100)
        self.tabla.column("Apellidos", width=100)
        self.tabla.column("Cargo", width=100)
        self.tabla.column("Correo", width=100)

        self.tabla.pack(fill="both", expand=True)

    def obtener_datos(self):
        profesores = self.controller.listar_profesores()

        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for cod_prof, nombre, apellidos, cargo, correo in profesores:
            self.tabla.insert("", "end", iid=cod_prof, values=(nombre, apellidos, cargo, correo))

    def editar_profesor(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un profesor")
            return

        item = seleccion[0]

        vista_editar = EditarProfesor(self.controller, self.obtener_datos, item)
        vista_editar.mainloop()

    def insertar_profesor(self):
        vista_insertar = InsertaProfesor(self.controller, self.obtener_datos)
        vista_insertar.mainloop()

    def eliminar_profesor(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un profesor")
            return

        item = seleccion[0]

        for cod_profesor in seleccion: #recorro los ids seleccionados. tabla.selection devuelve una lista con los iid.
            # Obtener ID del usuario seleccionado
            #id_usuario = seleccion[0] # si solo quiero eliminar de 1 en 1. Asi cogeria el primero de los seleccionados.

            nombre, apellidos, cargo, correo = self.tabla.item(cod_profesor)["values"] #obtengo los valores de la tabla.

            # Confirmar
            confirmar = messagebox.askyesno(
                "Confirmar",
                f"¿Eliminar profesor: {nombre} - {apellidos}?"
            )

            if confirmar:
                self.controller.eliminar_profesor(cod_profesor)
                messagebox.showinfo("Éxito", "Profesor eliminado")
                self.obtener_datos()
