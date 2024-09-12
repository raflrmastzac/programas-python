# p42_suma_200 - calcula la suma de números introducidos por el usuario hasta que la suma sea >=  200 y muestra cuantos números fueron introducidos.
# Importa libreria para limpiar terminal
import os

while True:
    # Limpia el texto de la terminal
    os.system("cls")

    # Se da mensaje de inicio
    print("Calcula la suma de números hasta que sea >= 200.")

    # Se definen variables
    cont_num = 0
    sum_num = 0

    while sum_num <= 200:
        num = float(input("Introduce un numero: ? "))

        sum_num += num
        cont_num += 1

    print(f"\nEn total se ingresaron {cont_num} numeros, La suma de los numeros ingresados es: {sum_num}")

    # Se pregunta al usuario si desea continuar
    if input("¿Deseas continuar (S/N)? ").upper().startswith("N"): break

print("\nProceso terminado ...")