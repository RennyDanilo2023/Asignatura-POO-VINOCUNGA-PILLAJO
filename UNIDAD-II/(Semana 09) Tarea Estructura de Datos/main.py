from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()

    while True:
        print("\nMenú del Sistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = input("Cantidad del producto: ")
            precio = input("Precio del producto: ")
            try:
                cantidad = int(cantidad)
                precio = float(precio)
                producto = Producto(id, nombre, cantidad, precio)
                inventario.anadir_producto(producto)
            except ValueError:
                print("Error: La cantidad y el precio deben ser numéricos.")
        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad =
