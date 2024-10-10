# p91-modificar-diccionario - Modifica los valores presentes dentro de un diccionario de datos

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

paises = {"Argentina" : 100, "Brasil" : 200, "Colombia" : 300, "Chile" : 400, "Ecuador" : 500, "Bolivia" : 600, "Jamaica" : 700}

print("Inicial ", paises, len(paises))

# Modificando un elemento especifico usando []
paises["Brasil"] = 250
paises["Chile"] = 450

# Modificando un elemento especifico usando update()
paises.update({"Bolivia" : 650})
paises.update({"Jamaica" : 750})

# Se muestra el diccionario en forma de tabla
print("\nFinal")
for k, v in paises.items():
        print(f"{k} = {v}")
