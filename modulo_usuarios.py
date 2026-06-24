import json
lista_usuarios = []
RUTA_JSON = "usuarios.json"

#------------validadores------------


#validar nombre no puede ser vacío

def validar_nombre(nombre):
    if len(nombre.strip()) > 0:
        print("nombre agregado")
        return True
    else:
        print("nombre no puede estar vacío")
        return False

#hay que validar sexo 
def validar_sexo(sexo):
    if sexo in ["F", "M"]:
        return True
    else:
        print("ERROR. son validos solo F o M")
        return False
# validar password
def validar_password(password):
    #minimo 8 caracteres
    if len(password.strip()) > 8:
        return False
    #que tenga al menos un nro
    tiene_numero = False
    for numero in password:
        if numero.isnumeric():
            tiene_numero = True
    tiene_letra = False
    for letra in password:
        if letra.isalpha():
            tiene_letra = True
    
    return True
    

#-------JSON-----------
usuario = {
    "nombre" : nombre,
    "sexo" : sexo,
    "password" : password
}

#-----------FUNCIONES TRANSACCIONALES -------------------
# validar que nombre no se repita (revisar lista ya existente)

def agregar_usuario(usuario):
    nombre = str(input("Ingrese nombre: ")).strip().upper()
    while not validar_nombre(nombre):
        nombre = str(input("Ingrese nombre: ")).strip().upper()




#-----------IMPRIMIR USUARIO---------------

def imprimir_usuario(usuario):
    print(f"""
-------------USUARIO------------
Nombre de usuario: {usuario["nombre"]}
Sexo: {usuario["sexo"]}
Contraseña: {usuario["password"]}
""").strip().upper()
    
    
    
    











#------------funciones de la app-------------

#def ingresar_usuario()

#def buscar_usuario()

#def eliminar_usuario()

#def salir()
