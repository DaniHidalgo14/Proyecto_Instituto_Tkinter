import customtkinter as ctk

from config.settings import RESIZEABLE_H, RESIZEABLE_W

class EditarProfesor(ctk.CTk):
    def __init__(self, controller, obtener_datos, item):
        super().__init__()
        self.controller = controller
        self.obtener_datos = obtener_datos
        self.item = item
        self.configurar_ventana()
        self.construir_ventana()

    def configurar_ventana(self):
        self.title("Editar Profesor"),
        self.geometry("300X300")
        self.resizable(RESIZEABLE_W, RESIZEABLE_H)
        self.configure(fg_color="black")

    def construir_ventana(self):
        frame = ctk.CTkFrame(self, width=300, height=300)
        frame.pack_propagate(False)
        frame.pack()

        titulo = ctk.CTkLabel(frame, text="Editar Profesor", font=("Arial", 20))
        titulo.pack(pady=10)

        self.nombreEntry = ctk.CTkEntry(frame, placeholder_text="Nombre")
        self.nombreEntry.pack(pady=10)

        self.apellidosEntry = ctk.CTkEntry(frame, placeholder_text="Apellidos")
        self.apellidosEntry.pack(pady=10)

        self.cargoEntry = ctk.CTkEntry(frame, placeholder_text="Cargo")
        self.cargoEntry.pack(pady=10)

        self.correoEntry = ctk.CTkEntry(frame, placeholder_text="Correo")
        self.correoEntry.pack(pady=10)

        self.guardarBtn = ctk.CTkButton(frame, text_color="white", text="Guardar", command=self.editar_profesor)
        self.guardarBtn.pack(pady=10)

    def editar_profesor(self):
        nombre = self.nombreEntry.get().strip()
        apellidos = self.apellidosEntry.get().strip()
        cargo = self.cargoEntry.get().strip()
        correo = self.correoEntry.get().strip()

        self.controller.edita_profesor(self.item, nombre, apellidos, cargo, correo)
        self.obtener_datos()
        self.destroy()