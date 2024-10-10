# p93_eliminar_diccionario - Elimina elementos dentro de un diccionario y posteriormente eliminia el diccionario por completo

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

municipios = {
    "Apozol"    : 1863, 
    "Calera"    : 1868, 
    "Fresnillo" : 1554, 
    "Guadalupe" : 1821,
    "Jalpa"     : 1824,
    "Jerez"     : 1824,
    "Loreto"    : 1931,
    "Mazapil"   : 1824,
    "Momax"     : 1857
}

# Se imprime el diccionario
print("Diccionario de municipios\n")
print("Inicial", municipios, len(municipios))
print()

# Se elimina un elementos especifico usando del
del municipios["Apozol"]
print("Elimina Apozol", municipios, len(municipios))
print()

# Se elimina un elementos especifico usando pop()
municipios.pop("Fresnillo")
print("Elimina Fresnillo", municipios, len(municipios))
print()

# Se elimina un elementos especifico usando popitem()
municipios.popitem() # Elimina el ultimo valor del diccionario, en este caso Momax
print("Elimina Momax", municipios, len(municipios))
print()

# Se elimina el diccionario usando clear()
municipios.clear()
print("Elimina todos los elementos", municipios, len(municipios))
print()

# Muestra la forma final del diccionario
print("\nFinal")
for k, v in municipios.items():
        print(f"{k} = {v}")