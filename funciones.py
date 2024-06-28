import csv

def agregar_producto():
    print("Agregar producto")
    id = int(input("Ingrese el ID del producto"))
    nombre = input("Ingrese el nombre del producto")
    categoria = input("Ingrese una opcion  1. Electronica  2. Textil  3. Calzado")
    if categoria == 1:
        categoria = "Electronica"
    elif categoria == 2:
        categoria = "Textil"
    elif categoria == 3:
        categoria = "Calzado"
    precio = float(input("Ingrese el precio del producto"))
    print("Producto agregado correctamente")
    
    with open('inventario.csv','a', newline='') as inventario:
        escribir = csv.writer(inventario)
        escribir.writerow([id, nombre, categoria, precio])
    
def leer_inventario():
    with open('inventario.csv', 'r') as inventario:
        leer = csv.reader(inventario)
        for row in leer:
            print("ID, Nombre, Categoria, Precio")
            print(row)

def clasificar_producto():
    print("Clasificar Producto")
    categorias = {
        "Electronica": [],
        "Textil": [],
        "Calzado": []
    }
    with open('inventario.csv', 'r') as inventario:
        leer = csv.reader(inventario)
        for row in leer:
            if row[2] == "Electronica":
                categorias["Electronica"].append(row)
            elif row[2] == "Textil":
                categorias["Textil"].append(row)
            elif row[2] == "Calzado":
                categorias["Calzado"].append(row)
    with open('inventario_clasificado.txt', 'w', newline='') as inventario_clasificado:
        for categoria, productos in categorias.items():
            inventario_clasificado.write(f"{categoria}\n")
            for producto in productos:
                inventario_clasificado.write(f"{producto}\n")
            inventario_clasificado.write("\n")
        print("Inventario clasificado correctamente")
