# p138_articulo.py - Creamos una clase Articulo con atributos y metodos: codigo de identificacion (id), descripcion, cantidad, precio y el total del valor por artuculo.

# Importa librería para limpiar la terminal
import os

class Articulo:
    def __init__(self, id, descripcion, cantidad, precio):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
    def obtenerTotal(self):
        return self.precio * self.cantidad
    def __str__(self):
        return f"ID: {self.id}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}, Precio: {self.precio}, Total: {self.obtenerTotal()}"

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

art01 = Articulo("A101", "Pluma Roja", 888, 0.08)
print(art01)

art01.cantidad = 999
art01.precio = 0.99
print("\nPrimer Articulo")
print("ID          = ", art01.id)
print("Descripcion = ", art01.descripcion)
print("Cantidad    = ", art01.cantidad)
print("Precio      = ", art01.precio)
print("Total       = ", art01.obtenerTotal())

print("\nSegundo Articulo")
art02 = Articulo("A102", "Pluma Azul", 934, 1.2)
print(art02)

print("\nTercer Articulo")
art03 = Articulo("P103", "Lapiz del 12", 456, 0.5)
print(art03)

print("\nTotal obtenido")
print(f"Articulo 1: {art01.obtenerTotal()}")
print(f"Articulo 2: {art02.obtenerTotal()}")
print(f"Articulo 3: {art03.obtenerTotal()}")

total = art01.obtenerTotal() + art02.obtenerTotal() + art03.obtenerTotal()
print("Total todos:", total)
