# p10_tercer_angulo - Calcula el 3er ángulo, dando dos angulos de un triángulo

# Se importan las librerias a utilizar.
import os

#Se limpia el texto previo en terminal
os.system("cls")

# Se da mensaje de inicio
print("Calculo de tercer angulo de un triangulo")

# Se definen variables
angulo1 = float(input("Dame el valor del angulo 1 ?"))
angulo2 = float(input("Dame el valor del angulo 2 ?"))

# Se realiza la operacion correspondiente.
angulo3 = 180 - (angulo1 + angulo2)

# Se regresa el resultado
print(f"angulo 1 : {angulo1}")
print(f"angulo 2 : {angulo2}")
print(f"El valor del tercer angulo es {angulo3}")