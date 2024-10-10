# p95_contar_caracteres - 

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

# Limpia el texto de la terminal
import os
os.system("cls")

# Lee una cadena de valores
cadena = input("Escribe una cadena: ")

# Se inicializa un diccionario vacio
cont_caracter = {}

# comprueba los valores leidos dentro del diccionario
for caracter in cadena:
    if caracter in cont_caracter:
        cont_caracter[caracter] += 1
    else:
        cont_caracter[caracter] = 1

# Mostrar el diccionario con el conteo de apariciones
print("\nCantidad de apariciones de cada carácter:")
print("resultado final", cont_caracter, len(cont_caracter))
