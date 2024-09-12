# p39_impares_ascendente -  Imprime números impares de forma ascendente desde 1 hasta el número que el usuario
# decida (n) y imprimirse la suma de estos.

# Importa libreria para limpiar terminal
import os

while(True):
    # Limpia el texto de la terminal
    os.system("cls")

    # Se da mensaje de inicio
    print("Imprimiendo números impares y su suma.")

    # Se definen variables
    n = int(input("hasta donde deseas llegar ? "))

    num = 1
    suma_impares = 0

    while num <= n:
        if num % 2 != 0:
            print(num, end=" ")
            suma_impares += num
        num += 1

    print(f"\nLa suma de los números impares es {suma_impares}")

    # Se pregunta al usuario si desea continuar
    if input("¿Deseas continuar (S/N)? ").upper().startswith("N"): break

print("\nProceso terminado ...")
