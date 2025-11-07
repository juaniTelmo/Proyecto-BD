# Para instalar la librería, en la consola ejecutamos:
# py -m pip install mysql-connector-python
import mysql.connector #Importa el módulo mysql.connector para conectar con bases de datos MySQL

class BD:
    def __init__(self):
        #CREO LA CONEXIÓN QUE PERMITE COMUNICARSE CON LA BASE DE DATOS
        self.conexion = mysql.connector.connect(
            host="10.1.5.205", #186.23.248.252 remota 10.1.5.205 local
            user="2025-4INF-Grupo01",
            password="carlitostevez",
            database="2025-4INF-Grupo01"
        )
        #CREO EL CURSOR QUE PERMITE EJECUTAR CONSULTAS
        self.cursor = self.conexion.cursor() 

# Método para generar consultas para obtener datos (SELECT)
    def consultar_datos(self, sql):
        self.cursor.execute(sql) #Ejecuta la consulta SQL
        return self.cursor.fetchall() #Devuelve todos los registros obtenidos
    
# Método para ejecutar consultas para modificar datos (DELETE|INSERT|UPDATE)
    def ejecutar_cambios(self, sql, valores=None): #NONE: Si no se pasan valores
        self.cursor.execute(sql, valores or ()) #Ejecuta la consulta SQL según los valores o todos los registros
        self.conexion.commit() #Guarda los cambios

    def cerrar(self):
        self.conexion.close() #Cierra la conexión
        
    def obtener_columnas(self, tabla):
        self.cursor.execute(f"SHOW COLUMNS FROM {tabla}")
        return [col[0] for col in self.cursor.fetchall()]

