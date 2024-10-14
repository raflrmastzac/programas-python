# p96_trabajando_conjuntos - Realiza las operaciones basicas en un conjunto

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

muns = {"zacatecas", "guadalupe", "jerez", "fresnillo", "fresnillo"}

print("El conjunto : ", muns, len(muns))

print(" Lista de municipios")
for mun in muns:
    print(mun, end=" ")

print("\nEsta zacatecas en los municipios - ", "zacatecas" in muns)

muns.add("teul")
print("El conjunto : ", muns, len(muns))

mas = {"luis moya", "ojocaliente", "tepetongo", "rio grande"}

muns.update(mas)
print("El conjunto : ", muns, len(muns))

muns.remove("luis moya")
print("El conjunto : ", muns, len(muns))

muns.discard("luis moya")
print("El conjunto : ", muns, len(muns))

mun = muns.pop()
print(mun)
print("El conjunto : ", muns, len(muns))

muns.clear()
print("El conjunto . ", muns, len(muns))