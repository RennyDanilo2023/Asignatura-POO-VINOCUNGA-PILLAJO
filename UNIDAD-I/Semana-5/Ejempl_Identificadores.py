# Programa para gestionar información básica de un registro de empleados

# Función para ingresar y mostrar la información del empleado
def gestionar_registro():
    print("Bienvenido al sistema de gestión de registros de empleados.")
    
    # Solicitar información del empleado
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    salario = float(input("Ingrese el salario del empleado: "))
    estado_civil = input("Ingrese el estado civil del empleado: ")
    
    # Mostrar la información del empleado
    print("\nInformación del empleado:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Salario: ${salario:.2f}")
    print(f"Estado Civil: {estado_civil}")

# Función principal
def main():
    gestionar_registro()

if __name__ == "__main__":
    main()
