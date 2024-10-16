# p98_personas - Operaciones de conjuntos de nombres de personas

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

print("El conjunto A: ", A, len(A))
print("El conjunto B: ", B, len(B))

print("\nUnion")
print("Union de los conjuntos (A|B): ", A.union(B))

print("\nIntersección")
print("Intersección de los conjuntos (A & B): ", A & B)

print("\nDiferencia")
print("Diferencia de los conjuntos (A -B): ", A - B)

print("\nDiferencia simetrica")
print("Diferencia simetrica de los conjuntos (A ^ B): ", A ^ B)

print("\nPrueba de subconjuntos")
if {"Pablo", "Mateo"}.issubset(B):
    print("El conjunto de nombres {Pablo, Mateo} es subconjunto de B")
else:
    print("El conjunto de nombres {Pablo, Mateo} no es un subconjunto de B")

print("\nPrueba de superconjunto")
if A.issuperset({"Reynaldo", "Angelica"}):
    print("A es superconjunto del conjunto de nombres {Reynaldo, Angelica}")
else:
    print("A no es superconjunto del conjunto de nombres {Reynaldo, Angelica}")

print("\nVerificar pertenencia o no pertenencia al conjunto")
print("Pedro esta en A: ", "Pedro" in A)
print("Lilia no esta en B: ", "Lilia" not in B)
