class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f'Se ha creado una nueva persona llamada {self.nombre}.')

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

    def __del__(self):
        print(f'{self.nombre} ha sido eliminado.')

# Crear instancias de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("Maria", 25)

# Mostrar información de las personas
persona1.mostrar_informacion()
persona2.mostrar_informacion()

# Eliminar las instancias
del persona1
del persona2
