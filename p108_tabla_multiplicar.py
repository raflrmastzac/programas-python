# p108_tabla_multiplicar - Tabla de multiplicar usando funciones

# Importa librería para limpiar la terminal
import os

def tabla_multiplicar(t, n):
    for i in range(1, n+1):
        print(f"{t} x {i} = {t * i}")
    print("\n")

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

#Tabla_multiplicar(10,5)
#Tabla_multiplicar(8,7)
t = int(input("Que tabla deseas  "))
n = int(input("Hasta donde       "))
tabla_multiplicar(t, n)