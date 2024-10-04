# p75-lista-multiplica - Lee dos listas con 5 elementos, las multiplica y imprime las 3 listas

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

A = []
B = []
C = []

print("Introduce 5 elementos para la primera lista")
for i in range (5):
    n = int(input(f"A[{i+1}]= "))
    A.append(n)

print("Introduce 5 elementos para la segunda lista")
for i in range(5):
    n = int(input(f"B[{i+1}]= "))
    B.append(n)

print("\nMultiplicando ambas listas entre sí ...")
for i in range(5):
    C.append(A[i] * B[i])

print("\nLista A")
print(A)
print("Lista B")
print(B)
print("Lista C")
print(C)
