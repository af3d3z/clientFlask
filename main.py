import requests
from getpass import getpass
import app.funciones_editoriales as Editoriales
import app.funciones_libros as Libros
import os

def menu():
    print("GESTOR DE LIBROS Y EDITORIALES")
    print("Editoriales:")
    print("\t1. Listar editoriales")
    print("\t2. Agregar una editorial.")
    print("\t3. Editar una editorial.")
    print("\t4. Consultar una editorial.")
    print("\t5. Borrar una editorial.")
    print("Libros:")
    print("\t6. Listar libros.")
    print("\t7. Agregar un libro.")
    print("\t8. Editar un libro.")
    print("\t9. Consultar un libro.")
    print("\t10. Borrar un libro.")
    print("0. Salir.")
    

username = input("User: ")
password = getpass("Password: ")
token = ""

res = requests.post(
    "http://localhost:5050/users/login",
    json={"username": username, "password": password},
    headers={"Content-Type": "application/json"}
    )

if res:
    token = res.json().get("token")
else:
    print("Credenciales incorrectas.")
    

option = 20

while option > 0:
    #limpia la consola
    os.system('cls||clear')
    menu()
    option = int(input("Elige la opción: "))
    match option:
        case 1:
            Editoriales.get_all()
        case 2:
            Editoriales.agregar_editorial(token)
        case 3: 
            Editoriales.editar_editorial(token)
        case 4:
            Editoriales.get_one()    
        case 5: 
            Editoriales.borrar_editorial(token)
        case 6:
            Libros.get_all()
        case 9:
            Libros.get_one()
        