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
        print(f"Se ha agregado correctamente el libro.")
    else:
        print(f"Error: {res.content}")
        
    input("Pulsa enter para continuar.")
    
def editar_libro(token):
    id = int(input("Introduce el id del libro a editar: "))
    libro_prev = requests.get(f"http://localhost:5050/libros/{str(id)}")
    if libro_prev.status_code == 200:
        libro_prev_json = libro_prev.json()
        precio = float(input(f"Precio ({libro_prev_json['precio']}):"))
        isbn = input(f"ISBN ({libro_prev_json['isbn']}): ")
        titulo = input(f"Título ({libro_prev_json['titulo']}): ")
        numpag = input(f"Nº de páginas: ({libro_prev_json['numpag']}): ")
        tematica = input(f"Temática ({libro_prev_json['tematica']}): ")
        id_editorial = int(input(f"Id editorial ({libro_prev_json['id_editorial']}): "))
        
        libro = Libro.Libro(id, precio, isbn, titulo, numpag, tematica, id_editorial)
        
        res = requests.put(
            f"http://localhost:5050/libros/{str(id)}",
            json=libro.serialize(),
            headers={"Content-Type": "application/json", "Authorization": "Bearer " + token}
        )
        if res.status_code == 200:
            print("Libro modificado.")
        else:
            print(f"No se pudo modificar la editorial {res.content}")
        
    else:
        print("Hubo un error al intentar acceder a los datos. Error: " + str(libro_prev.content))
    
    input("Pulsa enter para continuar.")
    

def borrar_libro(token):
    id = int(input("Introduce el id del libro a borrar: "))
    confirmation = input("¿Está seguro de querer borrarlo? (Sí/No): ")
    if confirmation.lower() == 's':
        res = requests.delete(
            f"http://localhost:5050/libros/{id}",
            headers={"Authorization": "Bearer " + token}
        )
    
        if res.status_code == 200:
            print("El libro se ha eliminado correctamente.")
        else: 
            print(f"Ha ocurrido un error: {str(res.content)}")
            
    input("Pulsa enter para continuar.")