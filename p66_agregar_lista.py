# p66–agregar-lista - Agrega elementos a una lista de numeros

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

nums = [80.3, 12.5, 60.2, 30.4]
print("Agrega elementos a una lista de numeros")

print("Los numeros : ", nums, len(nums))

print("Agregar dos elelemtos adicionales")
nums.append(90)
nums.append(100)
print("Queda : ", nums, len(nums))

print("Insertar elememto en la posicion 1")
nums.insert(1,85.5)
print("Queda : ", nums, len(nums))

print("Insertar un rango de elementos")
nums.extend([110, 120, 130])
print("Queda : ", nums, len(nums))
