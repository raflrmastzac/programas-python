# p99_numeros - 

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

A = {50,60,70,80,90,100,200}
B = {60,90,100,300,400,500}
C = {10,20,60,90,70,100,600,700}

print("El conjunto A: ", A, len(A))
print("El conjunto B: ", B, len(B))
print("El conjunto C: ", C, len(C))

print("\nUnion:")
print("Union de los conjuntos A y B: ", A | B)
print("Union de los conjuntos B y C: ", B | C)

print("\nDiferencia")
print("Diferencia de A y C (A - C): ", A - C)

print("\nDiferencia simetrica")
print("Diferencia simetrica de B y C: ", B ^ C)

print("\nIntereseccion")
print("Intersección de B y C: ", B & C)

print("\nProbar subconjunto")
print("A es subconjunto de B: ", A <= B)
print("C es subconjunto de A: ", C <= A)

print("\nVerificar pertenencia o no pertenencia al conjunto")
print("100 esta en A", 100 in A)
print("60 esta en A", 60 in A)
print("60 esta en B", 60 in B)
print("60 esta en C", 60 in C)
print("900 no esta en C", 900 not in C)