from kivy.uix.actionbar import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from clases.funcionarios.funcionarios import Funcionarios #MODIFICAR IMPORTACION POR LA DE SU CLASE

class BuscarFuncionariosScreen(Screen):
    def buscar(self, columna, dato_a_buscar):

        cont = self.ids.contenedor_tabla
        cont.clear_widgets()

        salida = self.ids.mensaje
        salida.text = ""

        col = columna.strip().lower()
        dato = dato_a_buscar.strip()

        columnas_permitidas = ["cuil", "apellido", "nombre", "reparticion"]

        if col not in columnas_permitidas:
            salida.text = f"Columna inválida: {col}. Editables: {columnas_permitidas}"
            return

        if not dato:
            salida.text = "Faltan datos."
            return

        # Crear objeto vacío
        func = Funcionarios("", "", "", "", "")

        condicion_busqueda = f"{col} = '{dato}'"

        # Metodo REAL de búsqueda
        encontrados = Funcionarios.buscar_funcionarios(condicion_busqueda)

        if not encontrados:
            salida.text = "No se encontraron registros."
            return

        columnas = func.columnas()
        filas = encontrados

        column_data = []
        for col in columnas:
            w = 35 if col.lower() in ("cuil",) else 80
            column_data.append((col.capitalize(), dp(w)))

        row_data = [tuple("" if v is None else str(v) for v in fila) for fila in filas]

        cont.clear_widgets()
        self.data_table = MDDataTable(
            size_hint=(1, 1),
            column_data=column_data,
            row_data=row_data,
            use_pagination=True,
            rows_num=10,
        )

        cont.add_widget(self.data_table)
