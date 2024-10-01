# p64–acceder-lista - accede a unos elementos de una lista

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

#       0    1   2   3   4   5   6   7   8
nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]
#      -9   -8  -7  -6  -5  -4  -3  -2  -1

print("Acceder a los elementos de una lista")
print("la lista       : ", nums)
print("# Elementos    : ", len(nums))
print("\nAcceder con indices positivos 0 .. 8")
print("Primero        : ", nums[0])
print("Ultimo         : ", nums[8])
print("Del 2 al 6     : ", nums[2:6])
print("Primero 3      : ", nums[:3])
print("Ultimos 3      : ", nums[6:])
print("\nAcceder con indices positivos -9 .. -1")
print("Primero        : ", nums[-9])
print("Ultimo         : ", nums[-1])
print("Del 2 al 6     : ", nums[-7:-3])
print("Primero 3      : ", nums[:-6])
print("Ultimos 3      : ", nums[-3:])
