# p136_circulo - Modelamos un circulo, propiedad radio, metodos: Area, Circunferencia

# Importa librerías a usar
import os
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def obtenerArea(self):
        return math.pi * math.pow(self.radio,2)
    def obtenerCircunferencia(self):
        return 2 * math.pi * self.radio
    def __str__(self):
        return f"Circulo [Radio = {self.radio}, Area = {self.obtenerArea():.2}, Circunferencia = {self.obtenerCircunferencia():.2} ]"

# Programa princial
# Limpia el texto de la terminal
os.system("cls")

print("\nCirculo 1: ")
circulo01 = Circulo(10.40)
print(f"El radio       : {circulo01.radio}")
print(f"Area           : {circulo01.obtenerArea():.2f}")
print(f"Circunferencia : {circulo01.obtenerCircunferencia():.2f}")

print("\nCirculo 2: ")
circulo02 = Circulo(12.45)
print(circulo02)
