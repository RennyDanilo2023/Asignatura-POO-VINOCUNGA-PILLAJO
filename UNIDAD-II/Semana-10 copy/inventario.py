# inventario.py
import pickle
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_inventario()

    def añadir_producto(self, producto):
        self.productos[producto.id] = producto
        self.guardar_inventario()

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            self.guardar_inventario()

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self):
        with open('inventario.pkl', 'wb') as f:
            pickle.dump(self.productos, f)

    def cargar_inventario(self):
        try:
            with open('inventario.pkl', 'rb') as f:
                self.productos = pickle.load(f)
        except FileNotFoundError:
            pass
