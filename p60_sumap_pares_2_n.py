# p60_sumap_pares_2_n - Imprime los pares de 2 a n y su suma

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

print("Imprimiendo numeros pares de 2 a n")
n = int(input("Hasta que valor deseas llegar ?"))
s = 0

n = n if n%2==0 else n-1
for x in range(2, n+1 , 2):
    print(x, end=" ")
    s = s + x
print("\n\nLa suma de los numeros pares es " + str(s))
print("\nProceso terminado... ")