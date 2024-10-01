# p70-sumar-listas - sumar dos listas de numeros introducidas por el ususario

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

c = int(input("Cuantos elementos  ? "))

A = []
B = []
C = []

print("Leer lista A")
for i in range (c):
    n = int(input(f"A[{1}]= "))
    A.append(n)
print(A)

print("Leer lista B")
for i in range(c):
    n = int(input(f"B[{i}]= "))
    B.append(n)
print(B)

print("Suma de listas C = A + B")
for i in range(c):
    C.append(A[i] + B[i])
print(C)
