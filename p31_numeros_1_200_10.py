# p31_numeros_1_200_10 - Imprime numeros de 1 a 200 de 10 en 10

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("\nImprime numeros de 1 a 200 de 10 en 10\n")

# Se definen variables
c = 0

# Inicia el ciclo
while c <= 200:
    c = c + 1
    if c % 10 != 0:
        continue
    print(c , end=" ")
