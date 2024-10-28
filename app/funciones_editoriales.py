import requests
import models.Editorial as Editorial
import os

def get_all():
    res = requests.get(
        "http://localhost:5050/editoriales"
    )
    
    if res:
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
        
def get_one():
    number = int(input("Introduce el id de la editorial: "))
    res = requests.get("http://localhost:5050/editoriales/" + number)
    if res:
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