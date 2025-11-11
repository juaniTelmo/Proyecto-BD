from bd.bd import BD
bd = BD()
class Salarios:
    def __init__(self):
        self.tabla = 'salarios'
        self.id_salario=0 
        self.año=0
        self.mes=0
        self.asignacion_en_pesos=0
        self.aguinaldo_en_pesos=0
        self.total_salario_bruto_en_pesos=0
        self.cuil=""

    #funciones propias de la clase
    def columnas(self):
        return bd.obtener_columnas(self.tabla)
    #funciones con BD
    def insertar_salario(self):
        sql = "INSERT INTO salarios (año, mes, asignacion_en_pesos, aguinaldo_en_pesos, total_salario_bruto_en_pesos, cuil) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (self.año, self.mes, self.asignacion_en_pesos, self.aguinaldo_en_pesos, self.total_salario_bruto_en_pesos, self.cuil)
        bd.ejecutar_cambios(sql, valores)
    def obtener_salarios(self):
        sql = "SELECT id_salario, año, mes, asignacion_en_pesos, aguinaldo_en_pesos, total_salario_bruto_en_pesos, cuil FROM salarios"
        return bd.consultar_datos(sql)
    def actualizar_salario(self):
        sql = "UPDATE salarios SET año=%s, mes=%s, asignacion_en_pesos=%s, aguinaldo_en_pesos=%s, total_salario_bruto_en_pesos=%s, cuil=%s WHERE id_salario=%s"
        valores = (self.año, self.mes, self.asignacion_en_pesos, self.aguinaldo_en_pesos, self.total_salario_bruto_en_pesos, self.cuil, self.id_salario)
        bd.ejecutar_cambios(sql, valores)
    def columnas(self):
        return bd.obtener_columnas(self.tabla)
    
    def mostrar_tabla(self):
        sql = f"SELECT * FROM {self.tabla}"
        resultados = bd.consultar_datos(sql)
        return resultados