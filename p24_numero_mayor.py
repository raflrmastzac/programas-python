# p24_numero_mayor - Verifica cual numero es el mayor dados 3 números enteros

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("Verifica cual numero es el mayor dados 3 números enteros")

# Se definen variables
print("Ingresa 3 números separados por enter ?")
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

# Se realiza la clasificacion y seleccion 
if n1 >= n2 and n1 >= n3:
    print(f"El numero mayor es: {n1}")

elif n2 >= n1 and n2 >= n3:
    print(f"El numero mayor es: {n2}")

else:
    print(f"El numero mayor es: {n3}")

print("\nGracias por usar este programa ...")