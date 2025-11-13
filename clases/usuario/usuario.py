from bd.bd import BD
bd = BD()

class Usuarios:
    def __init__(self,nombre, email, dni,password):
        self.tabla="usuarios"
        self.nombre=nombre 
        self.email=email
        self.dni=dni
        self.user=""
        self.__password=password


    def get_password(self):
        return self.__password
    
    
    def set_password(self,password):
        self.__password=password


    def nombre_valido(self,nombre):

        if nombre.isalpha() and len(nombre)>=1:
            return True
        else:
            return False
        
    def dni_valido(self,dni):

        if int(dni.isdigit()) and len(dni)==8:
            return True
        else:
            return False
        
    def usuario_valido(self,user):

        if user.isalpha() and len(user)>1:
            return True
        else:
            return False
        
    def contrasena_valida(self,password):
        if len(password)>8:
            for letra in password:
                if letra.isdigit():
                    num=True
                if letra.upper()==letra:
                    mayus=True 
                if letra.lower()==letra:
                    minus=True
            if num and mayus and minus:
                return True
            else:
                return False
                
    def email_valido(self, email):
            cont=0
            if "@pioix.edu.ar" in email or "@gmail.com" in email:
                for c in email:
                    if c != "@":
                        cont+=1
                    if c == "@":
                        break
            if cont >=1:
                return True
            else:
                return False
        
    def registrarse(self):
        print("Buen dia, registrese:")
       
        nombre=input("ingrese su nombre")
        while self.nombre_valido(self,nombre) ==False:
            nombre=input("nombre invalido, tiene que tener al menos un digito")
        self.nombre=nombre


        dni=input("ingrese su dni")
        while self.dni_valido(self,dni) ==False:
            dni=input("dni invalido, tiene que tener 8 digitos")    
        self.dni=dni



        email=input("ingrese su email")
        while self.email_valido(self,email) ==False:
            email=input("email invalido, tiene que terminar en @pioix.edu.ar o @gmail.com")
        self.email=email



        usuario=input("ingrese su usuario")
        while self.usuario_valido(self,usuario) ==False:
            usuario=input("usuario invalido, intentelo nuevamente")
        self.user=usuario



        contrasena=input("ingrese su contrasena")
        while self.contrasena_valida(self,contrasena) ==False:
            contrasena=input("contraseña invalida, intentelo nuevamente")
        self.contrasena=contrasena

    def iniciar_sesion(self):
        print("Buen dia, inicie sesion:")
    
        usuario=input("ingrese su usuario")
        while usuario != self.user:
            usuario= input("El usuario no existe, ingrese nuevamente: ")
        
        contra=input("ingrese su usuario")
        while contra != self.contrasena:
            contra=input("La contraseña no es valida, ingrese nuevamente: ")

#funciones con BD

  #INSERTAR USUARIO EN LA BASE DE DATOS DESDE LA CLASE USUARIO
    def insertar_usuario(self):
        sql = f"INSERT INTO {self.tabla} (nombre, email, dni, pass) VALUES (%s,%s,%s,%s)" #%s: es un marcador de posición para cada valor
        valores = (self.nombre, self.email, self.dni, self.get_password() )#Tupla con los valores a insertar
        bd.ejecutar_cambios(sql, valores) #Ejecuto la consulta para insertar el usuario

    #ACTUALIZAR UN USUARIO SEGUN UNA CONDICION DICHA POR PARAMETRO
    def actualizar_usuario(self, condicion, nuevos_valores):
        sql = f"UPDATE {self.tabla} SET nombre=%s, email=%s, dni=%s, pass=%s WHERE {condicion}"
        valores = (nuevos_valores[0], nuevos_valores[1], nuevos_valores[2], nuevos_valores[3])
        bd.ejecutar_cambios(sql, valores)

    #ELIMINAR UN USUARIO SEGUN UNA CONDICION DICHA POR PARAMETRO
    def eliminar_usuario(self, condicion):
        sql = f"DELETE FROM {self.tabla} WHERE {condicion}"
        bd.ejecutar_cambios(sql)

    #BUSCAR USUARIO SEGUN UNA CONDICION DICHA POR PARAMETRO
    def buscar_usuario(self, condicion):
        sql = f"SELECT * FROM {self.tabla} WHERE {condicion}"
        resultados = bd.consultar_datos(sql)
        return resultados
    
    def mostrar_tabla(self):
        sql = f"SELECT * FROM {self.tabla}"
        resultados = bd.consultar_datos(sql)
        return resultados