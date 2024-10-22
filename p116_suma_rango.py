# p116_suma_rango - Suma rango de valores

# Importa librería para limpiar la terminal
import os

def sumarango(ini, fin):
    s = 0
    for i in range(ini, fin+1):
        s += i
    return s

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

while True:
    ini = int(input("Dame el valor inicial: "))
    fin = int(input("Dame el valor final  : "))
    if fin>ini : break

print(f"La suma del rango de valores es ", sumarango(ini, fin))