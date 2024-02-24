# main.py
from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()
    while True:
        print("\n1. Añadir producto\n2. Eliminar producto\n3. Actualizar producto\n4. Buscar producto por nombre\n5. Mostrar productos\n6. Salir")
        eleccion = input("Elige una opción: ")
        if eleccion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif eleccion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif eleccion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif eleccion == '4':
            nombre = input("Introduce el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif eleccion == '5':
            inventario.mostrar_productos()
        elif eleccion == '6':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
