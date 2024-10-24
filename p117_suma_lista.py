# p117_suma_lista - Suma una lista de numeros, usando una funcion

# Importa librería para limpiar la terminal
import os

def suma_lista(lista):
    s = 0
    for n in lista:
        s += n
    return s

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

nums = [10, 20, 30, 40, 50, 30, 20, 40, 30, 40, 50, 70]

res = suma_lista(nums)

print("La suma de la lista es :", res)