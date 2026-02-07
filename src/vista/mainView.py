import customtkinter as ctk
from PIL.ImageOps import expand

from config.settings import (APP_NAME, APP_VERSION, WINDOW_SIZE, RESIZEABLE_H,
                             RESIZEABLE_W, ICON_PATH, FONDO_FRAME, usuarios)
from ..vista.loginView import Login
from ..vista.alumnosView import Alumnos
from ..vista.profesoresView import Profesores
from ..vista.recursosView import RecursosView
from ..modelo.admins_model import AdminModel


class Mainview(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.crear_interfaz()
        self.mostrar_login()

    def configurar_ventana(self):
        self.title(APP_NAME),
        self.geometry(WINDOW_SIZE)
        self.resizable(RESIZEABLE_W, RESIZEABLE_H)
        self.iconbitmap(ICON_PATH)
        self.configure(fg_color="black")

    def crear_interfaz(self):

        menu = ctk.CTkFrame(self, width=145, height=420)
        menu.configure(fg_color=FONDO_FRAME)
        menu.pack_propagate(False)
        menu.pack(side="left")

        self.contentPane = ctk.CTkFrame(self, width=550, height=420)
        self.contentPane.configure(fg_color=FONDO_FRAME)
        self.contentPane.pack_propagate(False)
        self.contentPane.pack(side="right")

        tituloMn = ctk.CTkLabel(menu, text_color="white", text="Menu", font=("Arial", 20))
        tituloMn.pack(pady=25, padx=5)

        self.boton2 = (ctk.CTkButton(menu, text="👨‍🎓 Alumnos", fg_color=FONDO_FRAME, height=60, hover_color="grey", command=self.mostrar_alumnos))
        self.boton2.pack()

        self.boton3 = (ctk.CTkButton(menu, text="👨‍🏫 Profesores", fg_color=FONDO_FRAME, height=60, hover_color="grey", command=self.mostrar_profesores))
        self.boton3.pack()

        self.boton4 = (ctk.CTkButton(menu, text="🏢 Recursos", fg_color=FONDO_FRAME, height=60, hover_color="grey", command=self.mostrar_recursos))
        self.boton4.pack()

        self.boton5 = (ctk.CTkButton(menu, text="❌Log Out", fg_color=FONDO_FRAME, height=60, hover_color="grey", command=self.mostrar_login))
        self.boton5.pack()

    def clear(self):
        for widget in self.contentPane.winfo_children():
            widget.destroy()

    def mostrar_login(self):
        self.clear()
        login = Login(self.contentPane, self.habilitar_botones)
        login.configure(fg_color=FONDO_FRAME)
        login.pack_propagate(False)
        login.pack(fill="both", expand=True, pady=30)
        self.deshabilitar_botones()

    def mostrar_alumnos(self):
        self.clear()
        panelAlumnos = Alumnos(self.contentPane)
        panelAlumnos.configure(fg_color=FONDO_FRAME)
        panelAlumnos.pack_propagate(False)
        panelAlumnos.pack(fill="both", expand=True)

    def mostrar_profesores(self):
        self.clear()
        panelProfesores = Profesores(self.contentPane)
        panelProfesores.configure(fg_color=FONDO_FRAME)
        panelProfesores.pack_propagate(False)
        panelProfesores.pack(fill="both", expand=True)

    def mostrar_recursos(self):
        self.clear()
        panelRecursos = RecursosView(self.contentPane)
        panelRecursos.pack_propagate(False)
        panelRecursos.configure(fg_color=FONDO_FRAME)
        panelRecursos.pack(fill="both", expand=True)

    def habilitar_botones(self):
        self.boton2.configure(state="normal")
        self.boton3.configure(state="normal")
        self.boton4.configure(state="normal")
        self.boton5.configure(state="normal")

    def deshabilitar_botones(self):
        self.boton2.configure(state="disabled")
        self.boton3.configure(state="disabled")
        self.boton4.configure(state="disabled")
        self.boton5.configure(state="disabled")