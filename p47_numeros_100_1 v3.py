# p46_numeros_1_100 imprime numeros del 1 al 100 usando for

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

"""print( list( range(1,10) ) )

print( list( range(1,10,2) ) )

print( list( range(1,10,3) ) )

print( list( range(10,0,-1) ) )"""

n = int(input("Desde donde deseas descender ?  "))
i = int(input("Decrementos de               ?  "))

for x in range(n,0,-i):
    print(x, end=" ")