# p114_factorial - funcion factorial

# Importa librería para limpiar la terminal
import os

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

n = int(input("Dame un número entero y te regreso su factorial "))
print("\nEl factorial de ", n, "es", factorial(n))