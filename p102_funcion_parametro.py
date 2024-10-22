# p102_funcion_parametro - funcion con parametros

# Importa librería para limpiar la terminal
import os

def saluda(nombre):
  print(f"Hola {nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres")

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

saluda("Carlos Castaneda")
saluda("Juan Perez Diaz")
saluda("María Soto García")
saluda(20)