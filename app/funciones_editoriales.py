import requests
import models.Editorial as Editorial
import os

def get_all():
    res = requests.get(
        "http://localhost:5050/editoriales"
    )
    
    if res.status_code == 200:
        # limpia la consola
        os.system('cls||clear')
        print("Editoriales: ")
        for editorial in res.json():
            new_editorial = Editorial.Editorial(
                id=editorial['id'], 
                cif=editorial['cif'],
                razon=editorial['razon'], 
                direccion=editorial['direccion'], 
                web=editorial['web'],
                correo=editorial['correo'], 
                tlf=editorial['tlf'])
            print(new_editorial)
            
        input("Pulsa enter para continuar.")
    else:
        print("Error: " + str(res.content))
        input("Pulsa enter para continuar.")
        
def get_one():
    number = int(input("Introduce el id de la editorial: "))
    res = requests.get("http://localhost:5050/editoriales/" + str(number))
    if res.status_code == 200:
        os.system("cls||clear")
        editorial_json = res.json()
        print(f"Editorial {number}: ")
        new_editorial = Editorial.Editorial(
                id=editorial_json['id'], 
                cif=editorial_json['cif'],
                razon=editorial_json['razon'], 
                direccion=editorial_json['direccion'], 
                web=editorial_json['web'],
                correo=editorial_json['correo'], 
                tlf=editorial_json['tlf'])
        print(new_editorial)
        input("Pulsa enter para continuar.")
    else:
        print(f"Error: {str(res.content)}")
        input("Pulsa enter para continuar.")
        
def get_data_editorial():
    id = int(input("Id de la editorial: "))
    cif = input("CIF de la editorial: ")
    razon = input("Razón social de la editorial: ")
    direccion = input("Dirección de la editorial: ")
    web = input("Web de la editorial: ")
    correo = input("Correo electrónico de la editorial: ")
    tlf = int(input("Teléfono de la editorial: "))
    
    return Editorial.Editorial(id, cif, razon, direccion, web, correo, tlf)
    

def agregar_editorial(token):
    print("Introduce los datos de la editorial: ")
    editorial = get_data_editorial()
    res = requests.post(
        "http://localhost:5050/editoriales",
        json=editorial.serialize(),
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + token}
    )
    
    if res.status_code == 201:
        print(f"Se ha agregado correctamente la editorial con id {editorial.id}")
    else:
        print("Error: " + str(res.content))
        
    input("Pulsa enter para continuar.")
    

def editar_editorial(token):
    id = int(input("Introduce el id de la editorial a editar: "))
    editorial_prev = requests.get(f"http://localhost:5050/editoriales/{str(id)}")
    if editorial_prev.status_code == 200:
        editorial_prev_json = editorial_prev.json()
        cif = input(f"Introduce el nuevo cif ({editorial_prev_json['cif']}): ")
        razon = input(f"Introduce la nueva razon social ({editorial_prev_json['razon']}): ")
        direccion = input(f"Introduce la nueva dirección ({editorial_prev_json['direccion']}): ")
        web = input(f"Introduce la nueva web ({editorial_prev_json['web']}): ")
        correo = input(f"Introduce el nuevo correo ({editorial_prev_json['correo']}): ")
        tlf = input(f"Introduce el nuevo número de teléfono ({editorial_prev_json['tlf']}): ")
        
        nueva_editorial = Editorial.Editorial(id, cif, razon, direccion, web, correo, tlf)
        
        res = requests.put(
            "http://localhost:5050/editoriales/"+ str(id),
            json=nueva_editorial.serialize(),
            headers={"Content-Type": "application/json", "Authorization": "Bearer " + token}
        )    
        if res.status_code == 200:
            print("Editorial modificada correctamente.")
        else:
            print(f"No se pudo modificar la editorial: {res.content}")
    else:
        print("Hubo un error al intentar acceder a los datos. Error" + editorial_prev.content)
    
    input("Pulsa enter para continuar.")
    
def borrar_editorial(token):
    id = int(input("Introduzca el id de la editorial a borrar: "))
    confirmation = input("¿Está seguro de querer borrarlo? (Sí/No): ")
    if confirmation.lower()[0] == 's':
        res = requests.delete(
            f"http://localhost:5050/editoriales/{id}",
            headers={"Authorization": "Bearer " + token}
        )
    
        if res.status_code == 200:
            print("La editorial se ha eliminado correctamente")
        else:
            print("Ha ocurrido un error: " + str(res.content))
        
    input("Pulsa enter para continuar.")