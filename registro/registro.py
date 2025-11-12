from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.label import Label
from clases.usuario.usuario import Usuario


class RegistroScreen(Screen):
    def validar_registro(self, nombre, correo, dni, contrasena):
        usuario = Usuario(nombre.capitalize(), correo, dni, contrasena)
        if not nombre or not correo or not dni or not contrasena:
            self.ids.datos_cargados.text = 'Por favor, complete todos los campos.'
            self.ids.datos_cargados.disabled = False
            self.ids.datos_cargados.opacity = 1
        elif usuario.nombre_valido(nombre) and usuario.email_valido(correo) and usuario.dni_valido(dni) and usuario.contrasena_valida(contrasena):
            self.ids.datos_cargados.text = '¡Registro exitoso!'
            self.ids.datos_cargados.color = (0,1,0,1)
            self.ids.datos_cargados.disabled = False
            self.ids.datos_cargados.opacity = 1
            usuario.insertar_usuario()
            self.resetear()
            MDApp.get_running_app().ir_a("LoginScreen")
        else:
            self.ids.datos_cargados.disabled = True
            self.ids.datos_cargados.opacity = 0
            if not usuario.nombre_valido(nombre):
                self.ids.nombre_invalido.disabled = False
                self.ids.nombre_invalido.opacity = 1
            else:
                self.ids.nombre_invalido.disabled = True
                self.ids.nombre_invalido.opacity = 0
            if not usuario.email_valido(correo):
                self.ids.correo_invalido.disabled = False
                self.ids.correo_invalido.opacity = 1
            else:
                self.ids.correo_invalido.disabled = True
                self.ids.correo_invalido.opacity = 0
            if not usuario.dni_valido(dni):
                self.ids.dni_invalido.disabled = False
                self.ids.dni_invalido.opacity = 1
            else:
                self.ids.dni_invalido.disabled = True
                self.ids.dni_invalido.opacity = 0
            if not usuario.contrasena_valida(contrasena):
                self.ids.contrasena_invalida.disabled = False
                self.ids.contrasena_invalida.opacity = 1
            else:
                self.ids.contrasena_invalida.disabled = True
                self.ids.contrasena_invalida.opacity = 0

    def resetear(self):
        self.ids.nombre_input.text = ""
        self.ids.correo_input.text = ""
        self.ids.dni_input.text = ""
        self.ids.contrasena_input.text = ""
        self.ids.datos_cargados.text = ""