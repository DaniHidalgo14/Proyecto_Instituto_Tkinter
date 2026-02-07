import customtkinter as ctk

from config.settings import FONDO_FRAME, usuarios
from ..controlador.admin_controller import AdminModel, AdminController


class Login(ctk.CTkFrame):
    def __init__(self, parent, habilitar_botones):
        super().__init__(parent)
        self.admin = AdminController()
        self.habilitar_botones = habilitar_botones
        self.construir_contenedor()

    def construir_contenedor(self):

        frame = ctk.CTkFrame(self)
        frame.configure(fg_color="black")
        frame.pack(pady=20)

        titulo_label = ctk.CTkLabel(frame, text="Iniciar sesion", font=("Arial", 20), text_color="white")
        titulo_label.pack(pady=20)


        self.nombreInput = ctk.CTkEntry(frame)
        self.nombreInput.configure(fg_color="black", text_color="white", placeholder_text_color="white",
                              placeholder_text="👤 Usuario")
        self.nombreInput.pack(pady=10, padx=10)

        self.apellidoInput = ctk.CTkEntry(frame)
        self.apellidoInput.configure(fg_color="black", text_color="white", placeholder_text_color="white",
                                placeholder_text="🔒 Contraseña")
        self.apellidoInput.pack(pady=10, padx=10)

        self.boton = (ctk.CTkButton(frame, text="Pulsar", hover_color="blue", command=self.acceder)
                 .pack(pady=10, padx=10))

        self.label = (ctk.CTkLabel(frame, text="", text_color="white"))
        self.label.pack(pady=10, padx=10)

    def acceder(self):
        user = self.nombreInput.get()
        password = self.apellidoInput.get()
        frase, login = self.admin.inicio_sesion(user, password)
        if login:
            self.label.configure(text=frase, text_color="green")
            self.habilitar_botones()
        else:
            self.label.configure(text=frase, text_color="red")