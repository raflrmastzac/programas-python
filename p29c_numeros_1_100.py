# p29c_numeros_1_100 - Imprime numeros de 1 a n, en incrementosde p, usando while

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("\nImprime numeros de 1 a n, en incrementosde p, usando while\n")

# Se definen variables
c = 0
n = int(input("Hasta donde quieres llegar ? "))
p = int(input("En incrementos de ? "))

# Se inicia el ciclo
while c <= n :
    print(c, end=" ")
    c = c + p

print("\nCiclo terminado")