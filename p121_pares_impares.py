# p121_pares_impares - Dada una lista de numeros, devolver los pares, devolver los impares

# Importa librería para limpiar la terminal
import os

def pares_impares(nums):
    p=[]
    i=[]
    for n in nums:
        if n % 2 == 0 : 
            p.append(n)
    else:
        i.append(n)
    return p, i

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

nums = [9, 8, 60, 6, 90, 7, 10, 6, 7]

pares, impares = pares_impares(nums)

print(f"Numeros ", nums, len(nums))
print(f"Los pares son:", pares, len(pares))
print(f"Los impares son:", impares, len(impares))
