# p113_suma_digitos - Funcion que supa los digitos de un numero
# 1971 = 18

# Importa librería para limpiar la terminal
import os

def sumadigitos(n):
    suma=0
    while n!=0:
        dig = n % 10
        suma = suma + dig
        n = n // 10
    return suma

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

n = int(input("Dame un número y sumaré sus dígitos :? "))
print("\nLa suma de los dígitos es ", sumadigitos(n))