import os
import subprocess

def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def ejecutar_script(ruta_script):
    try:
        subprocess.run(['python', ruta_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script: {e}")

def mostrar_menu(opciones):
    while True:
        print("\nMenu Principal - Dashboard")
        for key, script_path in opciones.items():
            script_name = os.path.basename(script_path)
            print(f"{key}. {script_name}")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = opciones[eleccion]
            ejecutar_o_mostrar = input("¿Deseas ejecutar (e) o mostrar (m) el script? ")
            if ejecutar_o_mostrar.lower() == 'e':
                ejecutar_script(ruta_script)
            elif ejecutar_o_mostrar.lower() == 'm':
                mostrar_codigo(ruta_script)
            else:
                print("Opción no válida. Por favor, elige 'e' o 'm'.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    opciones = {
        '1': 'UNIDAD-I/Semana-3/ProgTradiTempera.py',
        '2': 'UNIDAD-I/Semana-3/ProPOOTempera.py',
        '3': 'UNIDAD-I/Semana-4-EjemplosMundoReal_POO/BibliotecaEscolarPOO.py',
        '4': 'UNIDAD-I/Semana-4-EjemplosMundoReal_POO/RestuarantePOO.py',
        '5': 'UNIDAD-I/Semana-5/Ejempl_Identificadores.py',
        '6': 'UNIDAD-I/Semana-5/Ejempl1_Identificadores.py',
        '7': 'UNIDAD-I/Semana-6/Ejercicio-POO.py',
        '8': 'UNIDAD-I/Semana-7/Ejercicio_def_unit.py',
        # '8': 'UNIDAD-II/...', # Continúa con las rutas de UNIDAD-II
    }
    mostrar_menu(opciones)