# p29b_numeros_1_100 - Imprime numeros de 1 a n usando while

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("\nImprime numeros de 1 a n usando while\n")

# Se definen variables
c = 1
n = int(input("Hasta donde quieres llegar ? "))

# Se inicia el ciclo
while c <= n :
    print(c, end=" ")
    c = c + 1

print("\nCiclo terminado")