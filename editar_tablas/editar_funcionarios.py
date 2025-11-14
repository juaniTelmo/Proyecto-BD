from kivy.uix.actionbar import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from clases.funcionarios.funcionarios import Funcionarios #MODIFICAR IMPORTACION POR LA DE SU CLASE

#MODIFICAR NOMBRE
class EditarFuncionariosScreen(Screen):
    def buscar(self, columna, dato_a_buscar):
        #Elimina la tabla (si había una anterior)
        cont = self.ids.contenedor_tabla #ID BoxLayout de la tabla
        cont.clear_widgets()

        app = MDApp.get_running_app()
        salida = self.ids.mensaje
        salida.text = ""
        #Toma los valores ingresados
        col = columna.strip().lower()
        dato = dato_a_buscar.strip()

        #MODIFICAR COLUMNAS POR LAS DE SU CLASE
        columnas_permitidas = ["cuil", "apellido, nombre", "reparticion", "observaciones"]

        # Validaciones
        if col not in columnas_permitidas:
            salida.text = f"Columna inválida: {col}. Editables: {columnas_permitidas}"
            return

        if not dato:
            salida.text = "Faltan datos."
            return
        
        #MODIFICAR LA CREACION DE UN OBJETO DE SU CLASE
        func= Funcionarios("", "", "", "", "")

        # Guardamos la condicion para pasarla por parametro correctamente
        condicion_busqueda = f"{col} = '{dato}'"
        
        #MODIFICAR METODO DE BUSQUEDA POR EL DE SU CLASE
        encontrados = func.buscar_funcionarios(condicion_busqueda)

        if not encontrados:  # lista vacía
            salida.text = "No se encontraron registros."
            return
        
        #MODIFICAR OBJETO POR EL DE SU CLASE
        columnas = func.columnas()
        filas = encontrados

        # Columnas
        column_data = []
        for col in columnas:
            w = 35 if col.lower() in ("cuil",) else 80
            column_data.append((col.capitalize(), dp(w)))

        # Filas
        row_data = [tuple("" if v is None else str(v) for v in fila) for fila in filas]

        cont.clear_widgets()
        self.data_table = MDDataTable(
            size_hint=(1, 1),
            column_data=column_data,
            row_data=row_data,
            use_pagination=True,
            rows_num=10,
        )
        #AGREGA LA TABLA A LA PANTALLA
        cont.add_widget(self.data_table)

