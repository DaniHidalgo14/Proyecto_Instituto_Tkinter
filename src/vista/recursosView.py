import customtkinter as ctk
from tkinter import ttk, messagebox
from config.settings import materiales, aulas, asignaturas
from src.controlador.asign_controller import AsignsController
from src.controlador.aulas_controller import AulasController
from src.controlador.mats_controller import MatsController
from src.vista.EditViews.AulasEditView import AulasEditView
from src.vista.EditViews.MatEditView import MatEditView
from src.vista.InsertViews.AulasInsertView import AulasInsertView
from src.vista.InsertViews.MatsInsertView import MatsInsertView


class RecursosView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.matcontroller = MatsController()
        self.aulas_controller = AulasController()
        self.asings_controller = AsignsController()
        self.construir_contenedor()

    def construir_contenedor(self):
        titulo = ctk.CTkLabel(self, text_color="white", text="Recursos", font=("Arial", 20))
        titulo.pack(pady=10)

        recursos_frames = ctk.CTkTabview(self, width=530, height=300)
        recursos_frames.configure(fg_color="black")
        recursos_frames.pack(padx=10, pady=10)

        recursos_frames.add("Materiales")
        recursos_frames.add("Aulas")
        recursos_frames.add("Asignaturas")

        tab1 = recursos_frames.tab("Materiales")
        tab2 = recursos_frames.tab("Aulas")
        tab3 = recursos_frames.tab("Asignaturas")

        materiales_frame = self.construir_frame_materiales(tab1)
        aulas_frame = self.construir_frame_aulas(tab2)
        asignaturas_frame = self.construir_frame_asignaturas(tab3)

    #FRAME MATERIALES
    #BOTONES AÑADIR, MODIFICAR Y ELIMINAR PARA OPERACIONES CRUD
    #TREEVIEW PARA MOSTRAR LOS DATOS DE LOS MATERIALES DE CADA AULA
    def construir_frame_materiales(self, parent):
        botonesCRUD = ctk.CTkFrame(parent, width=530, height=50)
        botonesCRUD.configure(fg_color="black")
        botonesCRUD.pack_propagate(False)
        botonesCRUD.pack(padx=10, pady=10)

        anadirBtn = ctk.CTkButton(botonesCRUD, text_color="white", text="➕ Añadir", fg_color="green", command=self.insertar_nuevo)
        anadirBtn.pack(side="left", padx=10)

        modifBtn = ctk.CTkButton(botonesCRUD, text_color="white", text="🔄 Modificar", fg_color="blue", command=self.editar_material)
        modifBtn.pack(side="left", padx=20)

        eliminarBtn = ctk.CTkButton(botonesCRUD, text="❌ Eliminar", text_color="white", fg_color="red", command=self.eliminar_material)
        eliminarBtn.pack(side="right", padx=10)

        frame_materiales = ctk.CTkFrame(parent, width=530, height=250)
        frame_materiales.pack_propagate(False)
        frame_materiales.configure(fg_color="black")
        frame_materiales.pack(pady=10)

        self.datos_materiales = ctk.CTkFrame(frame_materiales, width=530, height=250)
        self.datos_materiales.pack_propagate(False)
        self.datos_materiales.configure(fg_color="white")
        self.datos_materiales.pack(pady=10, side="top", padx=10)

        scrollbar = ttk.Scrollbar(self.datos_materiales)
        scrollbar.pack(side="right", fill="y")

        self.tabla_materiales = ttk.Treeview(self.datos_materiales, columns=("Nombre", "Costo", "Aula"),
                                  show="headings", yscrollcommand=scrollbar.set)

        self.tabla_materiales.heading("Nombre", text="Nombre")
        self.tabla_materiales.heading("Costo", text="Costo")
        self.tabla_materiales.heading("Aula", text="Aula")

        self.tabla_materiales.column("Nombre", width=100)
        self.tabla_materiales.column("Costo", width=100)
        self.tabla_materiales.column("Aula", width=100)

        self.tabla_materiales.pack(fill="both", expand=True)

        self.obtener_datos_materiales()

    #FRAME AULAS
    #BOTONES AÑADIR, MODIFICAR Y ELIMINAR PARA OPERACIONES CRUD
    #TREEVIEW PARA MOSTRAR LOS DATOS DE LA TABLA AULAS
    def construir_frame_aulas(self, parent):
        botonesCRUD = ctk.CTkFrame(parent, width=530, height=50)
        botonesCRUD.configure(fg_color="black")
        botonesCRUD.pack_propagate(False)
        botonesCRUD.pack(padx=10, pady=10)

        anadirBtn = ctk.CTkButton(botonesCRUD, text_color="white", text="➕ Añadir", fg_color="green", command=self.insertar_nueva_aula)
        anadirBtn.pack(side="left", padx=10)

        modifBtn = ctk.CTkButton(botonesCRUD, text_color="white", text="🔄 Modificar", fg_color="blue", command=self.actualizar_aula)
        modifBtn.pack(side="left", padx=20)

        eliminarBtn = ctk.CTkButton(botonesCRUD, text="❌ Eliminar", text_color="white", fg_color="red", command=self.eliminar_aula)
        eliminarBtn.pack(side="right", padx=10)

        frame_aulas = ctk.CTkFrame(parent, width=530, height=250)
        frame_aulas.pack_propagate(False)
        frame_aulas.configure(fg_color="black")
        frame_aulas.pack(pady=10)

        self.datos_aulas = ctk.CTkFrame(frame_aulas, width=530, height=250)
        self.datos_aulas.pack_propagate(False)
        self.datos_aulas.configure(fg_color="white")
        self.datos_aulas.pack(pady=10, side="top", padx=10)

        scrollbar = ttk.Scrollbar(self.datos_aulas)
        scrollbar.pack(side="right", fill="y")

        self.tabla_aulas = ttk.Treeview(self.datos_aulas, columns=("Nombre", "Curso"),
                                  show="headings", yscrollcommand=scrollbar.set)

        self.tabla_aulas.heading("Nombre", text="Nombre")
        self.tabla_aulas.heading("Curso", text="Curso")

        self.tabla_aulas.column("Nombre", width=100)
        self.tabla_aulas.column("Curso", width=100)
        self.tabla_aulas.pack(fill="both", expand=True)

        self.obtener_datos_aulas()

    #FRAME ASIGNATURAS
    #BOTONES AÑADIR, MODIFICAR Y ELIMINAR PARA OPERACIONES CRUD
    #TREEVIEW PARA MOSTRAR DATOS DE LA TABLA ASIGNATURAS
    def construir_frame_asignaturas(self, parent):
        botonesCRUD = ctk.CTkFrame(parent, width=530, height=50)
        botonesCRUD.configure(fg_color="black")
        botonesCRUD.pack_propagate(False)
        botonesCRUD.pack(padx=10, pady=10)

        anadirBtn = ctk.CTkButton(botonesCRUD, text_color="white", text="➕ Añadir", fg_color="green")
        anadirBtn.pack(side="left", padx=10)

        modifBtn = ctk.CTkButton(botonesCRUD, text_color="white", text="🔄 Modificar", fg_color="blue")
        modifBtn.pack(side="left", padx=20)

        eliminarBtn = ctk.CTkButton(botonesCRUD, text="❌ Eliminar", text_color="white", fg_color="red")
        eliminarBtn.pack(side="right", padx=10)

        frame_asignaturas = ctk.CTkFrame(parent, width=530, height=250)
        frame_asignaturas.pack_propagate(False)
        frame_asignaturas.configure(fg_color="black")
        frame_asignaturas.pack(pady=10)

        self.datos_asignaturas = ctk.CTkFrame(frame_asignaturas, width=530, height=250)
        self.datos_asignaturas.pack_propagate(False)
        self.datos_asignaturas.configure(fg_color="white")
        self.datos_asignaturas.pack(pady=10, side="top", padx=10)

        scrollbar = ttk.Scrollbar(self.datos_asignaturas)
        scrollbar.pack(side="right", fill="y")

        self.tabla_asignaturas = ttk.Treeview(self.datos_asignaturas, columns=("Nombre", "Horas", "Profesor", "Curso"),
                                        show="headings", yscrollcommand=scrollbar.set)

        self.tabla_asignaturas.heading("Nombre", text="Nombre")
        self.tabla_asignaturas.heading("Horas", text="Horas")
        self.tabla_asignaturas.heading("Curso", text="Curso")
        self.tabla_asignaturas.heading("Profesor", text="Profesor")

        self.tabla_asignaturas.column("Nombre", width=200)
        self.tabla_asignaturas.column("Horas", width=100)
        self.tabla_asignaturas.column("Curso", width=50)
        self.tabla_asignaturas.column("Profesor", width=50)
        self.tabla_asignaturas.pack(fill="both", expand=True)

        self.obtener_datos_asignaturas()

    #FUNCIONES PARA MOSTRAR, ACTUALIZAR, INSERTAR Y BORRAR MATERIALES
    def obtener_datos_materiales(self):

        for item in self.tabla_materiales.get_children():
            self.tabla_materiales.delete(item)

        for id, nombre, coste, cod_aula in self.matcontroller.listar_materiales():
            self.tabla_materiales.insert("", "end", iid=id, values=(nombre, coste, cod_aula))

    def insertar_nuevo(self):
        vista = MatsInsertView(self.matcontroller, self.obtener_datos_materiales)
        vista.mainloop()

    def editar_material(self):
        seleccion = self.tabla_materiales.selection()

        if not seleccion: messagebox.showwarning("Error", "Seleccione un item")
        else:

            cod_mat = seleccion[0]
            vista = MatEditView(self.matcontroller, self.obtener_datos_materiales, cod_mat)
            vista.mainloop()

    def eliminar_material(self):
        seleccion = self.tabla_materiales.selection()

        if not seleccion: messagebox.showwarning("Error", "Selecciona un objeto")
        else:
            cod_mat = seleccion[0]

            mensaje = self.matcontroller.eliminar(cod_mat)
            messagebox.showinfo("Informacion", mensaje)
            self.obtener_datos_materiales()

    def obtener_datos_aulas(self):
        for item in self.tabla_aulas.get_children():
            self.tabla_aulas.delete(item)

        for aula in self.aulas_controller.listar_aulas():
            self.tabla_aulas.insert("", "end", iid=aula[0], values=(aula[1], aula[2]))

    def insertar_nueva_aula(self):
        vista = AulasInsertView(self.aulas_controller, self.obtener_datos_aulas)
        vista.mainloop()

    def actualizar_aula(self):
        seleccion = self.tabla_aulas.selection()

        if not seleccion:
            messagebox.showerror("Error", "Seleccione un item")
        else:
            codigo = seleccion[0]

            vista = AulasEditView(self.aulas_controller, self.obtener_datos_aulas, codigo)
            vista.mainloop()

    def eliminar_aula(self):
        seleccion = self.tabla_aulas.selection()

        if not seleccion:
            messagebox.showerror("Error", "Seleccione un item")
        else:
            codigo = seleccion[0]

            mensaje = self.aulas_controller.eliminar(codigo)
            messagebox.showinfo("Informacion", mensaje)
            self.obtener_datos_aulas()

    def obtener_datos_asignaturas(self):
        for asignatura in self.asings_controller.listar_asignaturas():
            self.tabla_asignaturas.insert("", "end", iid=asignatura[0], values=(asignatura[1], asignatura[2], asignatura[3], asignatura[4]))

    def eliminar_asignatura(self):
        seleccion = self.tabla_asignaturas.selection()

        if not seleccion:
            messagebox.showerror("Error", "Seleccione un item")
        else:
