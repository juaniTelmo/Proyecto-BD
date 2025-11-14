from clases.funcionarios.funcionarios import Funcionarios
from clases.salarios.salarios import Salarios
from clases.usuario.usuario import Usuarios
from bd.bd import BD

# Kivy / KivyMD
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

# Pantallas existentes
from login.login import LoginScreen
from clases.funcionarios.tabla_funcionarios import ListaFuncionariosScreen
from clases.salarios.tabla_salarios import ListaSalariosScreen
from inicio.inicio import HomeScreen
from registro.registro import RegistroScreen
from clases.usuario.perfil_usuario import PerfilScreen
from programadores.programadores import ProgramadoresScreen
from buscador.buscar_funcionarios import BuscarFuncionariosScreen
from editar_tablas.editar_funcionarios import EditarFuncionariosScreen

# ⬇️ NUEVAS PANTALLAS DE SALARIOS
from buscador.buscar_salarios import BuscarSalariosScreen
from editar_tablas.editar_salarios import EditarSalariosScreen


class MiApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        self.usuario_actual = None

        # CARGA DE KV
        Builder.load_file("inicio/inicio.kv")
        Builder.load_file("login/login.kv")
        Builder.load_file("registro/registro.kv")
        Builder.load_file("clases/salarios/tabla_salarios.kv")
        Builder.load_file("clases/funcionarios/tabla_funcionarios.kv")
        Builder.load_file("clases/usuario/perfil_usuario.kv")
        Builder.load_file("programadores/programadores.kv")
        Builder.load_file("buscador/buscar_funcionarios.kv")
        Builder.load_file("editar_tablas/editar_funcionarios.kv")

        Builder.load_file("buscador/buscar_salarios.kv")
        Builder.load_file("editar_tablas/editar_salarios.kv")

        sm = ScreenManager()

        # PANTALLAS PRINCIPALES
        sm.add_widget(HomeScreen(name="HomeScreen"))
        sm.add_widget(LoginScreen(name="LoginScreen"))
        sm.add_widget(RegistroScreen(name="RegistroScreen"))
        sm.add_widget(PerfilScreen(name="PerfilScreen"))

        # FUNCIONARIOS
        sm.add_widget(ListaFuncionariosScreen(name="ListaFuncionariosScreen"))
        sm.add_widget(BuscarFuncionariosScreen(name="BuscarFuncionariosScreen"))
        sm.add_widget(EditarFuncionariosScreen(name="EditarFuncionariosScreen"))

        # SALARIOS
        sm.add_widget(ListaSalariosScreen(name="ListaSalariosScreen"))
        sm.add_widget(BuscarSalariosScreen(name="BuscarSalariosScreen"))
        sm.add_widget(EditarSalariosScreen(name="EditarSalariosScreen"))

        # OTROS
        sm.add_widget(ProgramadoresScreen(name="ProgramadoresScreen"))

        # PANTALLA INICIAL
        sm.current = "HomeScreen"
        return sm

    def ir_a(self, pantalla):
        self.root.current = pantalla


if __name__ == "__main__":
    MiApp().run()
