# p29_numeros_1_100 - Imprime numeros de 1 a 100 usando while

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("\nImprime numeros de 1 a 100 usando while\n")

# Se definen variables
c = 1

# Se inicia el ciclo
while c <= 100 :
    print(c, end=" ")
    c = c + 1

print("\nCiclo terminado")
