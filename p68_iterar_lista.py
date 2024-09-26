# p68–iterar-lista - iterar por los elementos de una lista de numeros 

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

nums = [2, 4, 6, 8, 10, 12, 14, 16]
print("Iterando sobres los elementos de una lista")

print("Numero : ", nums, len(nums))

print("Iterar usando un ciclo for")
for num in nums:
    print(num, end=" ")

print("\nIterar usando el subindice positivo usando un ciclo for")
for i in range(len(nums)):
    print(nums[i], end=" ")

print("\nMostrar el arreglo donde a cada numero se le suman 2")
for num in nums:
    print(num+2, end=" ")
print("\nQueda : ", nums)

print("Elevar al cuadrado cada elemento del arreglo")
for i in range(len(nums)):
    nums[i] = nums[i] ** 2
print("\nQueda : ", nums)