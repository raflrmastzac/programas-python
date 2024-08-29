# p11_convertir_temperatura - Obtiene una equivalencia en grados farenheit de una temperatura en grados celsius.

# Se importan las librerias a utilizar.
import os

#Se limpia el texto previo en terminal
os.system("cls")

# Se da mensaje de inicio
print("Conversion de grados celsius a farenheit")

# Se definen variables
c = float(input("Dame el valor de temperatura en celsius ?"))

# Se realiza la operacion correspondiente.
f = (c * (9 / 5)) + 32

# Se regresa el resultado
print(f"El valor de la temperatura {c} grados celsius equivale a {f} grados farenheit")
