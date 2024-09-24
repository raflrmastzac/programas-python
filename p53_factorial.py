# p53_factorial - Calcula el factorial de un numero

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

n = int(input("Dame un numero ?"))
f = 1

print(f"{n}! = ", end=" ")

for i in range(1, n+1):
    f = f * i
    print(f"{i}! {"x" if i!=n else ""}", end=" ")

print(f"\nEl factor es {f}")