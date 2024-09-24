# p58_combina_colores - genera todas las combinaciones posibles entre los colores dados por el ususario

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

colores = input("Ingresa colores separados por espacio  ?").split()
print(colores)

for color1 in colores:
    for color2 in colores:
        if color1 != color2:
            print(f"{color1.strip()} y {color2.strip()}")
    print()
       