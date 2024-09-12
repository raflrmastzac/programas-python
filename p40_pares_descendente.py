# p40_pares_descendente - Imprime números pares de forma desendiente desde 100 hasta el número que el usuario
# decida (n) y imprimirse la suma de estos.

# Importa libreria para limpiar terminal
import os

while(True):
    # Limpia el texto de la terminal
    os.system("cls")

    # Se da mensaje de inicio
    print("Imprimiendo números pares de forma desendiente desde 100 hasta un numero decidido y su suma.")

    # Se definen variables
    n = int(input("Introduce un número entero positivo menor o igual a 100: "))

    if n > 100:
        print("El número debe ser menor o igual a 100.")
        continue

    num = 100
    suma_pares = 0

    while num >= n:
        if num % 2 == 0:
            print(num, end=" ")
            suma_pares += num
        num -= 1
    

    print(f"\nLa suma de los números pares es {suma_pares}")

    # Pregunta al usuario si desea continuar
    if input("¿Deseas continuar (S/N)? ").upper().startswith("N"): break

print("\nProceso terminado ...")
