# p110_numero_mayor - Funcion que calcula el amyor de 3 numeros

# Importa librería para limpiar la terminal
import os

def mayor(n1, n2, n3):
    may = -1
    if n1>n2 and n1>n3:
        may = n1
    elif n2>n1 and n2>n3:
        may = n2
    elif n3>n1 and n3>n2:
        may = n3
    return may

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

n1 = int(input("Numero 1 : "))
n2 = int(input("Numero 2 : "))
n3 = int(input("Numero 3 : "))
r = mayor(n1, n2, n3)

if r != -1:
    print("El mayor es ", r)
else:
    print("Los numeros son iguales, o hay dos iguales, por lo tanto no hay uno que sea el mayor")
