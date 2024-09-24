# p56_piramide_caracter - imprime un cuadradode un caracter determinado

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

r = int(input("Renglones ? "))
#c = int(input("Columnas  ? "))
car = input("Caracter ")

for i in range(1, r+1):
    for j in range(1, i+1):
        print(car, end="")
    print()
