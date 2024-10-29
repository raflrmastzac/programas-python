# p134_empleado1 - Creamos una clase empleado con atributos y metodos 

# Importa librería para limpiar la terminal
import os

# Código de clase
class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


# Programa principal
# Limpia el texto de la terminal
os.system("cls")

emp01 = Empleado("Carlos Castañeda", 35) # Creamos una instancia
emp02 = Empleado("Juan Perez", 66)

print("\nDatos del Empleado 1")
print(f"Nombre   : {emp01.nombre}")
print(f"Edad     : {emp01.edad}")
print(f"Empleado : {emp01}")
emp01.edad = 40
print(f"Empleado : {emp01}")

print("\nDatos del Empleado 2")
print(f"Nombre   : {emp02.nombre}")
print(f"Edad     : {emp02.edad}")
print(f"Empleado : {emp02}")
