# p104_funcion_mas_parametros - numeros de parametros desconocido

# Importa librería para limpiar la terminal
import os


def saludatodos(*todos):
  print(todos)
  print("Hola", todos[0])
  print(f"Separados por - {",".join(todos)}")
  for n in todos:
    print("Hola : ", n.upper())

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

saludatodos("Juan","Pedro","Luis","rocio","maria")
saludatodos("Luis","Jose")
saludatodos("Carlos")

