from bd.bd import BD
bd = BD()

class Funcionarios:
    def __init__(self):
        self.tabla = 'funcionarios'
        self.cuil=0
        self.apellido_y_nombre="" 
        self.reparticion=""
        self.observaciones=""

    #funciones propias de la clase
    def columnas(self):
        return bd.obtener_columnas(self.tabla)
    #funciones con BD
    def insertar_funcionario(self):
        sql = "INSERT INTO funcionarios (cuil, apellido_y_nombre, reparticion, observaciones) VALUES (%s, %s, %s, %s)"
        valores = (self.cuil, self.apellido_y_nombre, self.reparticion, self.observaciones)
        bd.ejecutar_cambios(sql, valores)

    def obtener_funcionarios(self):
        sql = "SELECT cuil, apellido_y_nombre, reparticion, observaciones FROM funcionarios"
        return bd.consultar_datos(sql)
    
    def actualizar_funcionario(self):
        sql = "UPDATE funcionarios SET apellido_y_nombre=%s, reparticion=%s, observaciones=%s WHERE cuil=%s"
        valores = (self.apellido_y_nombre, self.reparticion, self.observaciones, self.cuil)
        bd.ejecutar_cambios(sql, valores)

    def eliminar_funcionario(self):
        sql = "DELETE FROM funcionarios WHERE cuil=%s"
        valores = (self.cuil,)
        bd.ejecutar_cambios(sql, valores)
    
    def mostrar_tabla(self):
        sql = f"SELECT * FROM {self.tabla}"
        resultados = bd.consultar_datos(sql)
        return resultados    
    def buscar_funcionarios(self, condicion):
        sql = f"SELECT * FROM {self.tabla} WHERE {condicion}"
        resultados = bd.consultar_datos(sql)
        return resultados