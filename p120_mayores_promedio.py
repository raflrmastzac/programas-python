# p120_mayores_promedio - Calcula el promedio de una lista, luego se regresa los que son mayores al promedio

# Importa librería para limpiar la terminal
import os

def promedio(nums):
    s = 0
    for n in nums:
        s += n
    return s / len(nums)

def mayoresprom(nums, prom):
    mp = []
    for n in nums:
        if n > prom:
            mp.append(n)
    return mp

def leerdatos():
    datos=[]
    while True:
        d=int(input("Número ? "))
        if d==-1: break
        datos.append(d)
    return datos

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

#nums = [9, 8, 7.5, 5, 9.5, 7, 10, 6, 7]
nums = leerdatos()
print(nums)
prom = promedio(nums)
print("Promedio ", prom)

mayprom = mayoresprom(nums, prom)
print(mayprom, len(mayprom))