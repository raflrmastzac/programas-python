# p105_funcion_parametros_nombre - Funciones con nombres en los parametros

# Importa librería para limpiar la terminal
import os

def saluda(apaterno, amaterno, nombre):
  print(f"Hola {apaterno}, {amaterno}, {nombre}")


# Programa principal
# Limpia el texto de la terminal
os.system("cls")

saluda("Castañeda", "Ramirez", "Carlos")
saluda(nombre="Carlos",apaterno="Ramirez",amaterno="Castañeda")
saluda(nombre="Bernal",apaterno="Rocio",amaterno="Soto")