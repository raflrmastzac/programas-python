# p61_secuencia_numeros_1 - Imprime la secuencia de números mostrados el numero de renglones que el usuario desee

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

print("Imprime la secuencia de números mostrados el numero de renglones que el usuario desee\n")
r = int(input("Dame el numero ? "))

for i in range(1, r+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

print("\nProceso terminado... ")


