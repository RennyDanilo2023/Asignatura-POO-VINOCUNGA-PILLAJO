class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros con ISBN como clave
        self.usuarios = {}  # Diccionario de usuarios con user_id como clave
        self.usuarios_ids = set()  # Conjunto para manejar IDs únicos

    def añadir_libro(self, libro):
        """Añade un libro al catálogo de la biblioteca."""
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        """Quita un libro del catálogo de la biblioteca."""
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca."""
        if usuario.user_id not in self.usuarios_ids:
            self.usuarios[usuario.user_id] = usuario
            self.usuarios_ids.add(usuario.user_id)

    def dar_de_baja_usuario(self, user_id):
        """Elimina un usuario del registro de la biblioteca."""
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.usuarios_ids.remove(user_id)

    def prestar_libro(self, user_id, isbn):
        """Presta un libro a un usuario."""
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros.pop(isbn)  # Quita el libro de la colección disponible
            self.usuarios[user_id].prestar_libro(libro)

    def devolver_libro(self, user_id, libro):
        """Un usuario devuelve un libro a la biblioteca."""
        if user_id in self.usuarios:
            self.usuarios[user_id].devolver_libro(libro)
            self.añadir_libro(libro)  # Añade el libro de nuevo a la colección disponible

    def buscar_libro(self, **kwargs):
        """Busca libros por diversos criterios como título, autor o categoría."""
        resultados = []
        for libro in self.libros.values():
            if all(getattr(libro, clave, None) == valor for clave, valor in kwargs.items()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, user_id):
        """Lista todos los libros prestados a un usuario."""
        if user_id in self.usuarios:
            return self.usuarios[user_id].libros_prestados
        else:
            return "Usuario no encontrado."

