# p30_numeros_100_1 - Imprime numeros de 100 a 1 usando while

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("\nImprime los numeros de 100 a 1\n")

# Se definen variables
c = 100

while c >= 1:
    print(c, end=" ")
    c = c - 1

print("\nCiclo terminado")
