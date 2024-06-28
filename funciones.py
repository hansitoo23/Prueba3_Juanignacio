import csv

def agregar_producto():
    print("Agregar producto")
    id = int(input("Ingrese el ID del producto"))
    nombre = input("Ingrese el nombre del producto")
    categoria = input("Ingrese una opcion")
    if categoria == 1:
        categoria = "Electronica"
    elif categoria == 2:
        categoria = "Textil"
    elif categoria == 3:
        categoria = "Calzado"
    


    with open('inventario.csv','a', newline='') as agregar_producto:
        escribir = csv.writer(agregar_producto)
        escribir.writerow()
    print()

def leer_inventario():
    leer = csv.reader(agregar_producto)
    print(agregar_producto)

def Clasificar_productos():
    nombre = 
