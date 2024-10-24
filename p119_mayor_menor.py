# p119_mayor_menor - Dada una lista de numeros introducidos por el usuario, regresar el mayor y el menor

# Importa librería para limpiar la terminal
import os

def leerdatos():
    datos = []
    while True:
        d = int(input("Número ?"))
        if d == -1: break
        datos.append(d)
    return datos

def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

nums = leerdatos()
print(nums)
may = mayor(nums)
men = menor(nums)
print(f"El mayor es: ", may)
print(f"El menor es: ", men)

