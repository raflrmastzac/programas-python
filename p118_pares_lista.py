# p118_pares_lista - 

# Importa librería para limpiar la terminal
import os

def pares(lista):
    p = []
    for n in lista:
        if n % 2 == 0:
            p.append(n)
    return p

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(nums)
res = pares(nums)
print(type(res))
print(res)