# p65–cambiar-lista - Cambia los elementos de una lista de numeros

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

nums = [10, 9, 8.5, 6.5, 7.5, 6.2, 9.5]

print("Cambia o modifica los elementos de una lista")

print(type(nums))
print("La lista    : ", nums, len(nums))

print("Modificar los elementos en las posiciones 0 y 1")
nums[0] = 7
nums[1] = 7
print("Resulta en : ",nums)

print("Modificar los elementos en las posiciones de 2 a 5")
nums[2:5] = [9.0, 9.0, 9.0]
print("Resulta en :, ", nums)