class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados al usuario

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, ID={self.user_id}, Libros Prestados={self.libros_prestados})"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)
