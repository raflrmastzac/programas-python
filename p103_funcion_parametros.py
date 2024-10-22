# p103_funcion_parametros - funcion que recibe dos parametros

# Importa librería para limpiar la terminal
import os

def saluda(apaterno, nombre):
  print(f"Hola {apaterno} {nombre} longitud {len(apaterno+nombre)}")


# Programa principal
# Limpia el texto de la terminal
os.system("cls")

saluda("castañeda", "carlos")
#saluda("soto")
#saluda("soto", "bernal", "rocio")