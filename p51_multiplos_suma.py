# p51_multiplos_suma - imprime y suma los multiplos m entre 1 y n

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

n = int(input("Desde 1 hasta ? "))
m = int(input("Multiplos de  ? "))

c = s = 0

for i in range(1, n+1):
    if i % m == 0:
        print(i, end=" ")
        c = c + 1
        s = s + i

print(f"\nLos multiplos de {m} fueron {c} y su suma es {s}")