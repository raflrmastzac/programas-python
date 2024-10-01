# p65-procesar-calificaciones - Procesa una lista de calificaciones introducidas por el usuario

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

# nums = [9.5, 10, 7, 6, 4.5, 8.5, 10, 7, 5]
n = suma = promedio = 0
nums = []

while n!=99:
    n = float(input("Numero ? "))
    if n >= 0 and n <=10:
        nums.append(n)
    else:
        print("x")

print("< fin")

for n in nums:
    suma += n
promedio = suma / len(nums)

mp = []
for n in nums:
    if n > promedio:
        mp.append(n)

print("La calificaciones    : ", nums, len(nums))
print("La suma es           : ", suma)
print("El promedio es       : ", promedio)
print("Mayores al promedio  : ", mp, len(mp))
print("Mayor y Menor        : ", max(nums), min(nums))
nums.sort(reverse=True)
print("Ordenada             : ", nums)
