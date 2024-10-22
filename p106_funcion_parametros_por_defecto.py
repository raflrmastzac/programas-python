# p106_funcion_parametros_por_defecto - Funciones con valores por defecto para los parametros

# Importa librería para limpiar la terminal
import os

def saluda(nombre="Alumno X", edad = 15):
  print(f"Hola {nombre}, tienes {edad} años de edad")

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

saluda("Carlos")
saluda()
saluda("Rocio", 35)