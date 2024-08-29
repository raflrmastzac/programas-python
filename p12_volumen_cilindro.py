# p12_volumen_cilindro - Calcula el volumen de un cilindro dado su radio y altura.

# Se importan las librerias a utilizar.
import math
import os

#Se limpia el texto previo en terminal
os.system("cls")

# Se da mensaje de inicio
print("Calculando volumen de un cilindro")

# Se definen variables
r = float(input("Dame el valor del radio ?"))
h = float(input("Dame el valor de la altura ?"))

r2= r ** 2

# Se realiza la operacion correspondiente.
v = math.pi * r2 * h

# Se regresa el resultado
print(f"Teniendo un cilindro con un radio de {r} y una altura de {h} El valor del volumen es {v:.4f}")