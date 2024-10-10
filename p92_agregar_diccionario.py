# p92_agregar_diccionario - Agrega elementos dentro de un diccionario

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

ventas = {
    "Juan"  : 1550,
    "Jose"  : 2600,
    "Maria" : 2220
}

# Se imprime el diccionario
print("Diccionario de ventas realizadas\n")
print("Inicial", ventas, len(ventas))
print()

# Agrega elementos especificos dentro del diccionario usando []
ventas["Rocio"] = 2500
ventas["Mateo"] = 1567

# Agrega elementos especificos dentro del diccionario usando update()
ventas.update({"Andrea" : 9567})
ventas.update({"Miguel" : 1234})

# Se muestra el diccionario en forma de tabla
print("\nForma de tabla")
print("\nFinal")
for k, v in ventas.items():
        print(f"{k} = {v}")

# Se muestra el diccionario en su forma original
print("\nForma de original")
print("\nFinal", ventas, len(ventas))