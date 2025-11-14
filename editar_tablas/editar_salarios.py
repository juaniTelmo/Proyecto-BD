# editar_salarios.py
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp
from clases.salarios.salarios import Salarios
from bd.bd import BD


class EditarSalariosScreen(MDScreen):
    columnas = []
    datos_originales = []
    inputs = {}

    def cargar_datos(self, columnas, datos):
        self.columnas = columnas
        self.datos_originales = datos
        self.ids.contenedor_inputs.clear_widgets()
        self.ids.mensaje.text = ""

        self.inputs = {}

        for i, col in enumerate(columnas):
            val = datos[i]

            campo = MDTextField(
                hint_text=col,
                text=val,
                mode="rectangle",
                size_hint_x=0.95,
                pos_hint={"center_x": 0.5},
                readonly=(col.lower() == "id_salario")
            )

            self.ids.contenedor_inputs.add_widget(campo)
            self.inputs[col] = campo

    def guardar(self):
        try:
            s = Salarios()

            for col in self.columnas:
                valor = self.inputs[col].text
                setattr(s, col.lower(), valor)

            s.id_salario = int(self.inputs["id_salario"].text)
            s.actualizar_salario()

            self.ids.mensaje.text = "Cambios guardados correctamente."

        except Exception as e:
            self.ids.mensaje.text = f"Error: {e}"

    def eliminar(self):
        try:
            bd = BD()
            id_sal = int(self.inputs["id_salario"].text)
            bd.ejecutar_cambios("DELETE FROM salarios WHERE id_salario = %s", (id_sal,))
            self.ids.mensaje.text = "Registro eliminado."
            MDApp.get_running_app().ir_a("BuscarSalariosScreen")

        except Exception as e:
            self.ids.mensaje.text = f"Error: {e}"
