# p46_numeros_1_100 imprime numeros del 1 al 100 usando for

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

"""print( list( range(1,10) ) )

print( list( range(1,10,2) ) )

print( list( range(1,10,3) ) )

print( list( range(10,0,-1) ) )"""

for x in range(1,101):
    print(x, end=" ")