from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from clases.funcionarios.funcionarios import Funcionarios
func=Funcionarios()
class BuscarFuncionariosScreen(Screen):
    def on_pre_enter(self):
        app = MDApp.get_running_app()
        columnas_disponibles = func.columnas() 
        
        self.ids.spinner_columnas.values = columnas_disponibles
        self.ids.spinner_columnas.text = columnas_disponibles[0] if columnas_disponibles else "Sin datos"

    def registrar_consulta(self):
        app = MDApp.get_running_app()
        columna = self.ids.spinner_columnas.text
        comparador = self.ids.spinner_operador.text
        valor = self.ids.input_valor.text

        if not comparador=="=" and columna in ("cuil, apellido_y_nombre, reparticion, observaciones"):
            self.ids.texto.disabled = False
            self.ids.texto.opacity = 1
            self.ids.texto.text='comparador no valido para esa columna'
            self.ids.texto.color=(1,0,0,1)
        else:
            Funcionarios.condicion=f"{columna} {comparador} '{valor}'"
            self.ids.texto.disabled = True
            self.ids.texto.opacity = 0


    def reset(self):
        app = MDApp.get_running_app()
        Funcionarios.condicion=""
        self.ids.texto.disabled = False
        self.ids.texto.opacity = 1
        self.ids.texto.text="reseteado correctamente"
        self.ids.texto.color=(0,1,0,1)



