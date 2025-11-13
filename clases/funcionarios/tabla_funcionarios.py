from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from clases.funcionarios.funcionarios import Funcionarios

class ListaFuncionariosScreen(MDScreen):
    data_table = None

    def on_pre_enter(self, *args):
        fun = Funcionarios()
        columnas = fun.columnas()
        filas = fun.mostrar_tabla()

        # Columnas
        column_data = []
        for col in columnas:
            w = 35 if col.lower() == "id" else 80
            column_data.append((col.capitalize(), dp(w)))

        # Filas
        row_data = [tuple("" if v is None else str(v) for v in fila) for fila in filas]

        cont = self.ids.contenedor_tabla
        cont.clear_widgets()

        # Crear tabla (MDDataTable ya tiene scroll)
        self.data_table = MDDataTable(
            size_hint=(1, 0.9),  # altura relativa a su contenedor
            use_pagination=True,
            rows_num=10,
            column_data=column_data,
            row_data=row_data,
        )

        cont.add_widget(self.data_table)
