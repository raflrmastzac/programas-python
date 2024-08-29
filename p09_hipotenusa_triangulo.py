# p09_hipotenusa_triangulo - Calcula la hipotenusa de un triangulo rectangulo dadas las longitudes de sus lados.

# Se importan las librerias a utilizar.
import math
import os

#Se limpia el texto previo en terminal
os.system("cls")

# Se da mensaje de inicio
print("Calculo de hipotenusa de triangulo rectangulo")

# Se definen variables
longlado1 = float(input("Dame la longitud de lado 1 ?"))
longlado2 = float(input("Dame la longitud de lado 2 ?"))

# Se realiza la operacion correspondiente.
l1 = longlado1 ** 2
l2 = longlado2 ** 2

hipotenusa = math.sqrt(l1 + l2) 

# Se regresa el resultado
print(f"La hipotenusa de un triangulo de lado {longlado1} y {longlado2} es {hipotenusa:,.4f}")
