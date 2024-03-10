from Libro import Libro
from Usuario import Usuario
from Biblioteca import Biblioteca

# Creación de objetos de libros
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Ficción", "1234567890")
libro2 = Libro("1984", "George Orwell", "Ficción distópica", "0987654321")

# Creación de objetos de usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana López", "002")

# Creación de la biblioteca
biblioteca = Biblioteca()

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar un libro a un usuario
biblioteca.prestar_libro("001", "1234567890")

# Listar los libros prestados a un usuario
print("Libros prestados a Juan Pérez:", biblioteca.listar_libros_prestados("001"))

# Devolver un libro
biblioteca.devolver_libro("001", libro1)

# Verificar la devolución correctamente
print("Libros prestados a Juan Pérez después de la devolución:", biblioteca.listar_libros_prestados("001"))

# Buscar libros por categoría
print("Libros de Ficción distópica:", biblioteca.buscar_libro(categoria="Ficción distópica"))