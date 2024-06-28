from funciones import agregar_producto, leer_inventario, clasificar_producto
while True:
    print("Inventario")
    print("1. Agregar producto")
    print("2. Leer Inventario")
    print("3. Clasificar Producto")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion"))
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        leer_inventario()
    elif opcion == 3:
        clasificar_producto()
    elif opcion == 4:
        break