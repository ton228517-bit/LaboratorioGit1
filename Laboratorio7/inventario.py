# ==========================================
# SISTEMA DE INVENTARIO
# ==========================================

# Lista donde se almacenan los productos
inventario = []

# Registrar un producto
def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")

    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese nuevamente el nombre: ")

    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(producto)
    print("Producto registrado correctamente.\n")


# Mostrar todos los productos
def mostrar_productos():
    if len(inventario) == 0:
        print("No existen productos registrados.\n")
    else:
        print("\n===== INVENTARIO =====")
        for producto in inventario:
            print("-----------------------------------")
            print("Nombre :", producto["nombre"])
            print("Cantidad :", producto["cantidad"])
            print("Precio : S/.", producto["precio"])
        print()


# Buscar un producto
def buscar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    encontrado = False

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print("\nProducto encontrado")
            print("Nombre :", producto["nombre"])
            print("Cantidad :", producto["cantidad"])
            print("Precio : S/.", producto["precio"])
            encontrado = True

    if encontrado == False:
        print("Producto no encontrado.\n")


# Programa principal
while True:
    print("========== SISTEMA DE INVENTARIO ==========")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "0":
        print("Gracias por utilizar el sistema.")
        break
    else:
        print("Opción inválida.\n")