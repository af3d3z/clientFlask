import os
import models.Libro as Libro
import requests

def get_all():
    res = requests.get(
        "http://localhost:5050/libros"
    )
    
    if res.status_code == 200:
        os.system('cls||clear')
        print("Libros: ")
        for libro in res.json():
            new_libro = Libro.Libro(
                id=libro['id'],
                precio=libro['precio'],
                isbn=libro['isbn'],
                titulo=libro['titulo'],
                numpag=libro['numpag'],
                tematica=libro['tematica'],
                id_editorial=libro['id_editorial']
            )
            print(new_libro)
    else:
        print("Error: " + str(res.content))
        
    input("Pulsa enter para continuar.")
    
def get_one():
    id = int(input("Introduce el id del libro: "))
    res = requests.get(f"http://localhost:5050/libros/{id}")
    if res.status_code == 200:
        libro_json = res.json()
        libro = Libro.Libro(
            id=libro_json['id'],
            precio=libro_json['precio'],
            isbn=libro_json['isbn'],
            titulo=libro_json['titulo'],
            numpag=libro_json['numpag'],
            tematica=libro_json['tematica'],
            id_editorial=libro_json['id_editorial']
        )
        print(libro)
    else:
        print(f"Error: {res.content}")
    
    input("Pulsa enter para continuar.")

def get_data_libro():
    id = int(input("Id del libro: "))
    precio = float(input("Precio del libro: "))
    isbn = input("ISBN del libro: ")
    titulo = input("Título del libro: ")
    numpag = int(input("Número de páginas: "))
    tematica = input("Temática del libro: ")
    id_editorial = int(input("Id de la editorial: "))
    
    return Libro.Libro(id, precio, isbn, titulo, numpag, tematica, id_editorial)

def agregar_libro(token):
    print("Introduce los datos del libro: ")
    libro = get_data_libro()
    res = requests.post(
        f"http://localhost:5050/libros",
        json=libro.serialize(),
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + token}    
    )
    
    if res.status_code == 201:
        print(f"Se ha agregado correctamente el libro con el id {libro['id']}")
    else:
        print(f"Error: {res.content}")
        
    input("Pulsa enter para continuar.")