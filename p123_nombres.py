# p123_nombres - Procesar listas de nombres

# Importa librería para limpiar la terminal
import os

def procesa(nombres1, nombres2):
    todos = nombres1 + nombres2
    todos.sort()
    for i in range(len(todos)):
        todos[i] = todos[i].upper() 
    return todos

def entrada():
    dat = []
    while True:
        d = input("Nombre: ")
        if d=="": break
        dat.append(d)
    return dat

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

n1 = ["Juan", "Pedro", "Luis", "Jose", "Maria"]
#n2 = ["Rocio", "Teresa", "Karla"]
n2 = entrada()

n3 = procesa(n1, n2)

print(n3)