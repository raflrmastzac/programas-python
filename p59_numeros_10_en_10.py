# p59_numeros_10_en_10 - Imprime los números de 1 a n de 10 en 10

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

x = int(input("Hasta donde deseas llegar ? "))
for n in range(1, x+1 ,10):
    print(n, end=" ")

print("\nProceso terminado... ")
