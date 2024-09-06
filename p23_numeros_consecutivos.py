# p23_numeros_consecutivos - Verifica si una serie de numeros son consecutivos dados tres numeros consecutivos

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("Verifica si una serie de numeros son consecutivos dados tres numeros consecutivos")

# Se definen variables 
print("Ingresa 3 números separados por enter ?")
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

# Se realiza la clasificacion y seleccion 
if n1 + 1 == n2 and n2 + 1 == n3:
    print("Los números son consecutivos")

elif n1 + 1 == n3 and n3 + 1 == n2:
    print("Los números son consecutivos")

elif n2 + 1 == n1 and n1 + 1 == n3:
    print("Los números son consecutivos")

elif n2 + 1 == n3 and n3 + 1 == n1:
    print("Los números son consecutivos")

elif n3 + 1 == n1 and n1 + 1 == n2:
    print("Los números son consecutivos")

elif n3 + 1 == n2 and n2 + 1 == n1:
    print("Los números son consecutivos")

else:
    print("Error, los números son consecutivos ...")

print("\nGracias por utilizar este programa")