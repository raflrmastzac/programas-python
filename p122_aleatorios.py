# p122_aleatorios - Procesa dos listas de cadenas (nombres )

def genera_aleatorios(n):
    lista = []
    for i in range(n):
        lista.append( random.randint(1,100))
    return lista

def suma_listas(lista1, lista2, n):
    lista3 = []
    for i in range(n):
        lista3.append( lista1[i] + lista2[i] )
    return lista3

# Programa principal

# Importa librerías
import random
import os

# Limpia el texto de la terminal
os.system("cls")

MAX = 10

nums1 = genera_aleatorios(MAX)
nums2 = genera_aleatorios(MAX)
nums3 = suma_listas(nums1, nums2, MAX)

print("Lista 1 ", nums1)
print("Lista 2 ", nums2)
print("Lista 3 ", nums3)