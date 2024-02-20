class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"
    
    @staticmethod
    def from_string(s):
        id, nombre, cantidad, precio = s.split(',')
        return Producto(id, nombre, int(cantidad), float(precio))

    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    def get_cantidad(self):
        return self.cantidad
    
    def get_precio(self):
        return self.precio
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    
    def set_precio(self, precio):
        self.precio = precio
