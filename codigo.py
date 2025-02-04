# Definimos una función para cada operación matemática

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    # Verificamos que el divisor no sea cero para evitar errores
    if b == 0:
        return "Error: División por cero"
    return a / b

# Función principal de la calculadora
def calculadora():
    while True:
        # Mostramos el menú de operaciones disponibles
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        # Solicitamos la elección del usuario
        opcion = input("Ingrese el número de la operación deseada: ")

        # Si el usuario elige salir, rompemos el bucle
        if opcion == '5':
            print("Saliendo de la calculadora...")
            break

        # Solicitamos los dos números al usuario
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Por favor ingrese valores numéricos válidos.")
            continue

        # Ejecutamos la operación según la elección del usuario
        if opcion == '1':
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {division(num1, num2)}")
        else:
            print("Opción no válida. Intente nuevamente.")

# Llamamos a la función principal para iniciar la calculadora
if __name__ == "__main__":
    calculadora()
