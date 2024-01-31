# Definición de la clase base "Animal"
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

# Definición de la clase derivada "Perro" que hereda de "Animal"
class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice Guau!"

# Definición de la clase derivada "Gato" que hereda de "Animal"
class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice Miau!"

# Ejemplo de encapsulación
class Pajaro(Animal):
    def __init__(self, nombre, color_plumaje):
        super().__init__(nombre)
        self.__color_plumaje = color_plumaje  # Atributo privado

    def hablar(self):
        return f"{self.nombre} es un pájaro con plumaje {self.__color_plumaje} y hace pío."

# Función polimórfica
def hacer_hablar(animal):
    return animal.hablar()

# Crear instancias de las clases
mi_perro = Perro("Rex")
mi_gato = Gato("Whiskers")
mi_pajaro = Pajaro("Piolín", "amarillo")

# Llamar al método hablar de las instancias
print(hacer_hablar(mi_perro))  # Output: Rex dice Guau!
print(hacer_hablar(mi_gato))   # Output: Whiskers dice Miau!
print(hacer_hablar(mi_pajaro)) # Output: Piolín es un pájaro con plumaje amarillo y hace pío.
