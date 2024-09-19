# p50_suma_numeros - Suma n muneros introducidos por el usuario

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

suma = 0
n = int(input("Cuantas calificaciones ? "))

for i in range(1, n+1):
    print(f"Calificacion {i} ? ", end="")
    x = float(input())
    suma = suma + x

print(f"\nLa suma es {suma}")
print(f"\nEl promedio {suma / n}")