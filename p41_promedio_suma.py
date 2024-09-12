# p41_promedio_suma.py - Calcula la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0.

# Importa libreria para limpiar terminal
import os

while True:
    # Limpia el texto de la terminal
    os.system("cls")

    # Se da mensaje de inicio
    print("Calcula la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0.")

    # Se definen variables
    cont_num = 0
    sum_num = 0

    while True:
        num = float(input("Introduce un numero (introduce 0 para terminar)"))
        if num == 0:
            break
        sum_num += num
        cont_num += 1
    
    if cont_num > 0:
        prom = sum_num / cont_num

    else:
        prom = 0
    
    print(f"\nEn total se ingresaron {cont_num} numeros, La suma de los numeros ingresados es: {sum_num}, con un promedio de {prom:.4f}")

    # Se pregunta al usuario si desea continuar
    if input("¿Deseas continuar (S/N)? ").upper().startswith("N"): break

print("\nProceso terminado ...")