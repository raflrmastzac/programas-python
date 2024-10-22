# p107_funcion_retorno - Funcion con parametros, que regresa un valor

# Importa librería para limpiar la terminal
import os

def suma(n1, n2): 
    s = n1 + n2
    return s

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

# caso 1 - el resultado se guarda en una variable
r = suma(100,200)
print("El resultado es ", r)

# caso 2 - el resultado se calcula y se imprime directamente
print("\nOtra suma ", suma(100,200))

# caso 3 - el usuario proporciona el valor de los parametros
print("\nDame dos numeros a sumar, separados por <ente> ")
a , b = int(input()), int(input())
print(f"La suma del usuario es ", suma(a,b))