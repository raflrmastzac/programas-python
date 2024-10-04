# p77-lista-aleatorios-suma - Genera 2 listas de 10 números aleatorios, las Suma en una tercera, sumando solo elementos de cada lista si ambos son impares

# Importa librerías
import os
import random

# Limpia el texto de la terminal
os.system("cls")

A = []
B = []
C = []

print("Generando aleatorios ...")
for x in range(10):
    A.append(random.randint(1,100))
    B.append(random.randint(1,100))

print("A = ", A)
print("B = ", B)
print()

for x in range(10):
    if A[x] % 2 != 0 and B[x] % 2 != 0:
        C.append(A[x] + B[x])
    else:
        C.append(0)  # Se coloca 0 si no son ambos impares

print("A = ", A)
print("B = ", B)
print("C = ", C)
