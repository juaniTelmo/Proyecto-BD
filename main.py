from clases.funcionarios.funcionarios import Funcionarios
from clases.salarios.salarios import Salarios
from clases.usuario.usuario import Usuarios
from bd.bd import BD
persona1= Usuarios
salario1= Salarios()
funcionarios1= Funcionarios()
bd=BD()

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
# Importo la clase Usuario
from clases.usuario.usuario import Usuarios
# Importo las pantallas
from login.login import LoginScreen
from clases.funcionarios.tabla_funcionarios import ListaScreen
from clases.salarios.tabla_salarios import ListaScreen
from inicio.inicio import HomeScreen
from registro.registro import RegistroScreen

# Defino la clase principal de la aplicación
class MiApp(MDApp):
    # Método build para construir la aplicación
    def build(self):
        # Cargo los archivos .kv de cada pantalla
        Builder.load_file("inicio/inicio.kv")
        Builder.load_file("login/login.kv")
        Builder.load_file("registro/registro.kv")
        Builder.load_file("clases/salarios/tabla_salarios.kv")
        Builder.load_file("clases/funcionarios/tabla_funcionarios.kv")
        sm = ScreenManager()
        # Agrego las pantallas al ScreenManager
        sm.add_widget(HomeScreen(name="HomeScreen"))
        sm.add_widget(LoginScreen(name="LoginScreen"))
        sm.add_widget(RegistroScreen(name="RegistroScreen"))
        sm.add_widget(ListaScreen(name="ListaScreen"))
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