from kivymd.app import MDApp
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from clases.salarios.salarios import Salarios
from main import salario1
class ListaScreen(MDScreen):
    data_table = None

    def on_pre_enter(self, *args):
        app = MDApp.get_running_app()
        columnas = Salarios.columnas(salario1) 
        filas = Salarios.mostrar_tabla(salario1)

        # Columnas
        column_data = []
        for col in columnas:
            w = 35 if col.lower() in ("id",) else 80
            column_data.append((col.capitalize(), dp(w)))

        # Filas
        row_data = [tuple("" if v is None else str(v) for v in fila) for fila in filas]

        cont = self.ids.contenedor_tabla
        cont.clear_widgets()
        self.data_table = MDDataTable(
            size_hint=(1, 1),
            column_data=column_data,
            row_data=row_data,
            use_pagination=True,
            rows_num=10,
        )
        cont.add_widget(self.data_table)

