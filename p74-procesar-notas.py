# p74-procesar-notas - Lee n notas entre 0 y 100 hasta introducir un 0

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

n = suma = promedio = 0
nums = []

while True:
    n = float(input("Ingresa la nota ? "))

    if n == 0:
        break

    if n > 0 and n <=100:
        nums.append(n)
    else:
        print("La nota ingresada es incorrecta, fuera del rango de calificaciones")

print("< fin")

for n in nums:
    suma += n
promedio = suma / len(nums)

mp = []
for n in nums:
    if n < promedio:
        mp.append(n)

print("Notas ingresadas     : ", len(nums))
print("La calificaciones    : ", nums, len(nums))
print("Suma de las notas    : ", suma)
print("Promedio             : ", promedio)
print("Menores al promedio  : ", mp, len(mp))
print("Cantidad menores al promedio : ", len(mp))
print("Nota maxima          : ", max(nums))
print("Nota minima          : ", min(nums))
