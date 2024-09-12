# p43_numero_mayor - Calcula el número mayor de una serie de números introducidos por el teclado se detiene al introducir 0.

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

while True:
    # Se da mensaje de inicio
    print("Encuentra el número mayor de una serie de números. El proceso se detiene al introducir 0.")

    # Se definen variables
    mayor = None

    while True:
        # Solicita un número al usuario
        num = float(input("Introduce un número (0 para detener): "))
        
        if num == 0:
            break
        
        if mayor is None or num > mayor:
            mayor = num

    # Imprime el número mayor encontrado
    if mayor is not None:
        print(f"\nEl número mayor introducido es: {mayor}")
    else:
        print("\nNo se introdujeron números.")

    # Pregunta al usuario si desea continuar
    if input("\n¿Deseas realizar otra operación (S/N)? ").upper().startswith("N"): break

print("\nProceso terminado ...")
