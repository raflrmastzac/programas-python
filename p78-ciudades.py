# p78-ciudades - lee n nombres de ciudades en una lista hasta introducir $

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

ciudades = []

print("Introduce los nombres de las ciudades. Para terminar, escribe '$'")
while True:
    ciudad = input("Ciudad: ")
    if ciudad == "$":
        break
    ciudades.append(ciudad)

print(f"\nNúmero de ciudades ingresadas      : ",len(ciudades))
print(f"Lista de ciudades                    : ", ciudades, len(ciudades))
ciudades.sort(reverse=True)
print(f"Ciudades en orden descendente      : ", ciudades)

cons = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
c_cons = [ciudad for ciudad in ciudades if ciudad.lower().startswith(tuple(cons.lower()))]

print("\nNúmero de ciudades que empiezan con consonante   : ", len(c_cons))
print("Ciudades que empiezan con consonante               : ", c_cons)
