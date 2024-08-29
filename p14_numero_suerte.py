# p14_numero_suerte - calcula el numero de la suerte resultante de la suma de los digitos individuales presentes en la fecha de nacimiento.

# Se importan las librerias a utilizar.
import os

#Se limpia el texto previo en terminal
os.system("cls")

# Solicita al usuario la fecha de nacimiento en formato ddmmaaaa
print("Divide una fecha de nacimiento en formato ddmmaaaa en sus dígitos individuales.\n")
n = int(input("Introduce tu fecha de nacimiento en formato ddmmaaaa: "))

# Se definen las variables para extraer cada dígito usando operaciones matemáticas
d8 = n // 100000000
d7 = (n // 10000000) % 10
d6 = (n // 1000000) % 10
d5 = (n // 100000) % 10
d4 = (n // 10000) % 10
d3 = (n // 1000) % 10
d2 = (n // 100) % 10
d1 = (n // 10) % 10
d0 = n % 10

# Se realiza la suma de cada digito para obtener el numero de suerte
ns = d8 + d7 + d6 + d5 + d4 + d3 + d2 + d1 + d0

# Muestra los dígitos separados
print("Dígitos separados:", d8, d7, d6, d5, d4, d3, d2, d1, d0)

# Muestra el numero de suerte
print(f"El numero de suerte es {ns}")