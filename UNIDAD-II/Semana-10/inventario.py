from producto import Producto
import os

class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_productos()

    def guardar_productos(self):
        try:
            with open("inventario.txt", "w") as f:
                for producto in self.productos:
                    f.write(str(producto) + "\n")
        except Exception as e:
            print(f"Error al guardar en el archivo: {e}")

    def cargar_productos(self):
        if os.path.exists("inventario.txt"):
            try:
                with open("inventario.txt", "r") as f:
                    for line in f:
                        producto = Producto.from_string(line.strip())
                        self.productos.append(producto)
            except Exception as e:
                print(f"Error al cargar el archivo: {e}")
        else:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al añadir productos.")

    def anadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: Ya existe un producto con el mismo ID.")
            return
        self.productos.append(producto)
        self.guardar_productos()
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id:
                del self.productos[i]
                self.guardar_productos()
                print("Producto eliminado con éxito.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_productos()
                print("Producto actualizado con éxito.")
                return
        print("Producto no encontrado.")
    
    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")
    
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        for producto in self.productos:
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio()}")
