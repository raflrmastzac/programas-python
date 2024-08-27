# p08_dividir_en_cifras - Divide un numero entero de 3 cifras en centenas, decenas, unidades

# Se importa la libreria de calculo matematico a el codigo para su uso
import os

#Se limpia el texto previo en terminal
os.system("clear")

# Se da mensaje de inicio y el mensaje de interraccion
print("Divide un numero entero de 3 cifras en centenas, decenas y unidades \n")
n = int(input("Dame un numero entero de 3 cifras ?"))

# Se definen variables
c = n // 100
d = ( n - (c* 100) ) // 10
u = ( n - (c * 100 + d * 10))

# Se muestra el resultado
print("El numero original es ", n)
print("Centenas : ", c)
print("Decenas  : ", d)
print("Unidades : ", u)

print("\nNumero de la suerte", c+d+u)

