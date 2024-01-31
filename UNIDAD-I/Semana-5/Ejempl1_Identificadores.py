# Programa para calcular el área de un triángulo
# El usuario proporcionará la base y la altura como entrada

# Función para calcular el área del triángulo
def calcular_area(base, altura):
    area = 0.5 * base * altura
    return area

# Función principal
def main():
    print("Este programa calcula el área de un triángulo.")
    
    # Solicitar la base del triángulo al usuario
    base = float(input("Por favor, ingrese la base del triángulo: "))
    
    # Solicitar la altura del triángulo al usuario
    altura = float(input("Por favor, ingrese la altura del triángulo: "))
    
    # Calcular el área llamando a la función calcular_area
    area = calcular_area(base, altura)
    
    # Mostrar el resultado
    print(f"El área del triángulo con base {base} y altura {altura} es: {area}")

if __name__ == "__main__":
    main()
