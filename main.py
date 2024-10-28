import requests
from getpass import getpass
import app.funciones_editoriales as Editoriales
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
    print("\t1. Listar libros.")
    print("\t2. Agregar un libro.")
    print("\t3. Editar un libro.")
    print("\t4. Consultar un libro.")
    print("\t5. Borrar un libro.")
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
    

option = 10

while option > 0:
    #limpia la consola
    os.system('cls||clear')
    menu()
    option = int(input("Elige la opción: "))
    match option:
        case 1:
            Editoriales.get_all()
        case 4:
            Editoriales.get_one()    
        