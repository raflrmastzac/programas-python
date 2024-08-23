# p08_dividir_en_cifras - Dividir en cifras un numero entero

# Se importa la libreria de calculo matematico a el codigo para su uso
import math

# Se da mensaje de inicio 
print("Dividir en unidades, decenas y centenas un numero entero")

# Se definen las variables de trabajo
numero = int(input("Dame un número de 3 cifras: "))   # Se da el mensaje de interraccion
centenas = math.trunc( numero / 100 )
decenas = math.trunc( (numero - centenas * 100) / 10 )
unidades = numero - (centenas * 100 + decenas * 10)

# Se muestra el resultado
print(f"centenas: {centenas}, decenas: {decenas}, unidades: {unidades}")
