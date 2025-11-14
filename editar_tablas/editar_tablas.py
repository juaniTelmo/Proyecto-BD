from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp
from bd.bd import BD

class EdicionScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.tabla = None
        self.columnas = []
        self.row_original = []
        self.origen = "HomeScreen"

    def configurar(self, tabla, columnas, fila, origen="HomeScreen"):
        """
        tabla: nombre de la tabla (str)
        columnas: lista con nombres de columnas
        fila: tupla con valores del registro
        origen: pantalla a la que vuelve el botón atrás
        """
        self.tabla = tabla
        self.columnas = columnas
        self.row_original = list(fila)
        self.origen = origen

        self.ids.titulo_appbar.title = f"Editar {tabla.capitalize()}"
        self.ids.msg_info.text = ""

        cont = self.ids.contenedor_inputs
        cont.clear_widgets()

        # Generar dinámicamente los campos
        self.inputs = {}

        for i, col in enumerate(columnas):
            campo = MDTextField(
                hint_text=col.capitalize(),
                text=str(fila[i]) if fila[i] is not None else "",
                mode="rectangle",
                size_hint_x=0.95,
                pos_hint={"center_x": 0.5},
                readonly=(i == 0)  # la PK no editable
            )
            cont.add_widget(campo)
            self.inputs[col] = campo

    def guardar_cambios(self):
        bd = BD()

        nuevos_valores = []
        sets_sql = []

        # Comparar lo modificado
        for i, col in enumerate(self.columnas):
            nuevo_valor = self.inputs[col].text
            viejo_valor = "" if self.row_original[i] is None else str(self.row_original[i])

            if nuevo_valor != viejo_valor:
                sets_sql.append(f"{col}=%s")
                nuevos_valores.append(nuevo_valor)

        if not sets_sql:
            self.ids.msg_info.text = "No hay cambios para guardar."
            return

        # Usar columna 0 como clave primaria
        pk_col = self.columnas[0]
        pk_val = self.row_original[0]

        sql = f"UPDATE {self.tabla} SET {', '.join(sets_sql)} WHERE {pk_col}=%s"
        nuevos_valores.append(pk_val)

        try:
            bd.ejecutar_cambios(sql, nuevos_valores)
            self.ids.msg_info.text = "Cambios guardados exitosamente."
        except Exception as e:
            self.ids.msg_info.text = f"Error: {e}"

    def eliminar_registro(self):
        bd = BD()
        pk_col = self.columnas[0]
        pk_val = self.row_original[0]

        sql = f"DELETE FROM {self.tabla} WHERE {pk_col}=%s"

        try:
            bd.ejecutar_cambios(sql, (pk_val,))
            self.ids.msg_info.text = "Registro eliminado."
            MDApp.get_running_app().ir_a(self.origen)
        except Exception as e:
            self.ids.msg_info.text = f"Error: {e}"
