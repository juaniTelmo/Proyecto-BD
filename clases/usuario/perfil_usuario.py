from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

class PerfilScreen(Screen):
    def on_pre_enter(self, *args):
        app = MDApp.get_running_app()
        usuario = app.usuario_actual
        self.ids.nombre_usuario.text = f"NOMBRE: {usuario[1]}"
        self.ids.email_usuario.text  = f"EMAIL: {usuario[2]}"
        self.ids.dni_usuario.text    = f"DNI: {usuario[3]}"