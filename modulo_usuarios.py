lista_usuarios = []

#------------validadores------------

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
    
    
# validar que nombre no se repita (revisar lista ya existente)





def imprimir_usuario(usuario):
    print(f"""
-------------USUARIO------------
Nombre de usuario: {usuario["nombre"]}

          
          
          
          
          """).strip().upper()










#------------funciones de la app-------------

#def ingresar_usuario()

#def buscar_usuario()

#def eliminar_usuario()

#def salir()
