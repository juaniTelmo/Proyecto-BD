from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp #Agregar
from kivy.clock import Clock #Agregar
from bd.bd import BD
from clases.usuario.usuario import Usuarios #Agregar
bd = BD()
usu = Usuarios("", "", "", "") #Agregar
class LoginScreen(Screen): 
    def validar_datos(self): #Agregar método
        usuarioIngresado = self.ids.txt_usuario.text
        passIngresada = self.ids.txt_pass.text
        if not usuarioIngresado or not passIngresada:
            self.ids.mensaje.text = "Por favor, complete todos los campos."
            return
        else:
            credenciales = usu.buscar_usuario(f"email = '{usuarioIngresado}' and pass = '{passIngresada}'")
            if credenciales and len(credenciales) > 0:
                app = MDApp.get_running_app()
                app.usuario_actual = credenciales[0]
                self.ids.txt_usuario.text = ""
                self.ids.txt_pass.text = ""
                app.ir_a("PerfilScreen")
            else:
                self.ids.mensaje.text = "Usuario o contraseña incorrectos"