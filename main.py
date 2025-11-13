from clases.funcionarios.funcionarios import Funcionarios
from clases.salarios.salarios import Salarios
from clases.usuario.usuario import Usuarios
from bd.bd import BD

# Para instalar KivyMD y Kivy, descomenta las siguientes líneas y ejecútalas en la terminal:
# py -m pip install kivymd
# py -m pip install kivy
# Importo las librerías necesarias de Kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
# Importo la clase Usuario
from clases.usuario.usuario import Usuarios
# Importo las pantallas
from login.login import LoginScreen
from clases.funcionarios.tabla_funcionarios import ListaFuncionariosScreen
from clases.salarios.tabla_salarios import ListaSalariosScreen
from inicio.inicio import HomeScreen
from registro.registro import RegistroScreen
from clases.usuario.perfil_usuario import PerfilScreen
from programadores.programadores import ProgramadoresScreen
from buscar_funcionarios.buscar_funcionarios import BuscarFuncionariosScreen


# Defino la clase principal de la aplicación

class MiApp(MDApp):
    
    # Método build para construir la aplicación
    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        # Cargo los archivos .kv de cada pantalla
        self.usuario_actual = None
        Builder.load_file("inicio/inicio.kv")
        Builder.load_file("login/login.kv")
        Builder.load_file("registro/registro.kv")
        Builder.load_file("clases/salarios/tabla_salarios.kv")
        Builder.load_file("clases/funcionarios/tabla_funcionarios.kv")
        Builder.load_file("clases/usuario/perfil_usuario.kv")
        Builder.load_file("programadores/programadores.kv")
        Builder.load_file("buscar_funcionarios/buscar_funcionarios.kv")


        sm = ScreenManager()
        # Agrego las pantallas al ScreenManager
        sm.add_widget(HomeScreen(name="HomeScreen"))
        sm.add_widget(LoginScreen(name="LoginScreen"))
        sm.add_widget(RegistroScreen(name="RegistroScreen"))
        sm.add_widget(PerfilScreen(name="PerfilScreen"))
        sm.add_widget(ListaFuncionariosScreen(name="ListaFuncionariosScreen"))
        sm.add_widget(ListaSalariosScreen(name="ListaSalariosScreen"))
        sm.add_widget(ProgramadoresScreen(name="ProgramadoresScreen"))
        sm.add_widget(BuscarFuncionariosScreen(name="BuscarFuncionariosScreen"))
        
        # Establezco la pantalla inicial
        sm.current = "HomeScreen"
        return sm
    # Método para cambiar de pantalla
    def ir_a(self, nombre_pantalla: str):
        # Cambia a la pantalla especificada sin animación
        self.root.current = nombre_pantalla

#Corro la aplicación
if __name__ == "__main__":
    MiApp().run()