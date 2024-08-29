# p13_calculo_tiempo - Calcula la equivalencia en dias, minutos y segundos dada una cantidad en horas 

# Se importan las librerias a utilizar.
import os

#Se limpia el texto previo en terminal
os.system("cls")

# Se da mensaje de inicio
print("Calcula la equivalencia de un valor de horas a dias, minutos y segundos")

# Se definen variables
h = float(input("Dame la cantidad de horas ?"))

# Se realiza la operacion correspondiente.
d = h / 24
m = h * 60
s = m * 60

# Se regresa el resultado
print(f"Teniedo {h} horas, esto equivale a:\n"
f"{d} dias\n"
f"{m} minutos\n"
f"{s} segundos\n")
