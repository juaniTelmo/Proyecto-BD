# buscar_salarios.py
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.app import MDApp
from clases.salarios.salarios import Salarios


class BuscarSalariosScreen(MDScreen):
    data_table = None

    def buscar(self, columna, valor):
        cont = self.ids.contenedor_tabla
        cont.clear_widgets()
        self.ids.mensaje.text = ""

        col = columna.strip().lower()
        val = valor.strip()

        if col not in ["id_salario", "cuil"]:
            self.ids.mensaje.text = "Columna inválida (use id_salario o cuil)"
            return

        if not val:
            self.ids.mensaje.text = "Ingrese un valor para buscar"
            return

        resultados = []
        try:
            todos = Salarios().mostrar_tabla()
            columnas = Salarios().columnas()
            idx = [c.lower() for c in columnas].index(col)

            for fila in todos:
                if str(fila[idx]) == val:
                    resultados.append(fila)

        except Exception as e:
            self.ids.mensaje.text = f"Error: {e}"
            return

        if not resultados:
            self.ids.mensaje.text = "No se encontraron resultados"
            return

        columnas = Salarios().columnas()
        columnas_dt = [(c, dp(80)) for c in columnas]

        filas_dt = [tuple("" if v is None else str(v) for v in fila) for fila in resultados]

        self.data_table = MDDataTable(
            size_hint=(1, 1),
            column_data=columnas_dt,
            row_data=filas_dt,
            rows_num=10,
            use_pagination=True,
        )

        self.data_table.bind(on_row_press=self.on_row_press)
        cont.add_widget(self.data_table)

    def on_row_press(self, table, row):
        datos = row.text.split() if hasattr(row, "text") else []
        columnas = Salarios().columnas()

        if len(datos) != len(columnas):
            return

        app = MDApp.get_running_app()
        pantalla = app.root.get_screen("EditarSalariosScreen")
        pantalla.cargar_datos(columnas, datos)
        app.ir_a("EditarSalariosScreen")
