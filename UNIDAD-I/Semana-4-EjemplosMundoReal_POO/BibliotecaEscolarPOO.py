# Clase Libro
class Book:
    """
    Clase para representar un libro con atributos para el título, autor y ISBN,
    y métodos para actualizar estos atributos.
    """
    def __init__(self, title, author, isbn):
        # Constructor de la clase, inicializa los atributos
        self.title = title  # Título del libro
        self.author = author  # Autor del libro
        self.isbn = isbn  # ISBN del libro

    # Método para actualizar el título del libro
    def update_title(self, new_title):
        self.title = new_title

    # Método para actualizar el autor del libro
    def update_author(self, new_author):
        self.author = new_author

    # Método para actualizar el ISBN del libro
    def update_isbn(self, new_isbn):
        self.isbn = new_isbn

# Clase Estantería
class Shelf:
    """
    Representa una estantería en una biblioteca que sostiene una colección de libros,
    con métodos para agregar o quitar un libro, y para encontrar libros por título o autor.
    """
    def __init__(self):
        # Constructor de la clase, inicializa la lista de libros
        self.books = []

    # Método para agregar un libro a la estantería
    def add_book(self, book):
        self.books.append(book)

    # Método para quitar un libro de la estantería
    def remove_book(self, book):
        self.books.remove(book)

    # Método para encontrar libros por título
    def find_books_by_title(self, title):
        return [book for book in self.books if book.title == title]

    # Método para encontrar libros por autor
    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

# Clase Biblioteca
class Library:
    """
    Representa una biblioteca con una colección de estanterías,
    con métodos para agregar una estantería y buscar libros en todas las estanterías por título o autor.
    """
    def __init__(self):
        # Constructor de la clase, inicializa la lista de estanterías
        self.shelves = []

    # Método para agregar una estantería a la biblioteca
    def add_shelf(self, shelf):
        self.shelves.append(shelf)

    # Método para buscar libros por título en todas las estanterías
    def search_by_title(self, title):
        results = []
        for shelf in self.shelves:
            results.extend(shelf.find_books_by_title(title))
        return results

    # Método para buscar libros por autor en todas las estanterías
    def search_by_author(self, author):
        results = []
        for shelf in self.shelves:
            results.extend(shelf.find_books_by_author(author))
        return results

# Uso de ejemplo:
# Crear algunos libros
book1 = Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227")
book2 = Book("1984", "George Orwell", "978-0451524935")

# Crear una estantería y agregar libros a ella
shelf1 = Shelf()
shelf1.add_book(book1)
shelf1.add_book(book2)

# Crear una biblioteca y agregar la estantería a ella
library = Library()
library.add_shelf(shelf1)

# Buscar libros por título y autor
hobbit_search = library.search_by_title("The Hobbit")
orwell_search = library.search_by_author("George Orwell")

# Imprimir resultados de búsqueda
print(f"Resultados de la búsqueda para 'The Hobbit': {[book.title for book in hobbit_search]}")
print(f"Resultados de la búsqueda para 'George Orwell': {[book.title for book in orwell_search]}")
