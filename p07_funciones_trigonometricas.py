# p07_funciones_trigonometricas - Uso de las funciones trigonometricas en python

# Se importa la libreria de calculo matematico a el codigo para su uso
import math as mt

# Se da mensaje de inicio
print("Calculo de las funciones trigonometricas")

# Se definen variables
angulod = float(input("Dame un angulo ? :"))
angulor = mt.radians(angulod)

print(f"Angulo original : {angulod} , Angulo en radianes : {angulor}")

# Se formula la salida del calculo
salida=("Resumen de funciones trigonometricas\n" 
f"Seno     : {mt.sin(angulor):.3f}\n" 
f"Coseno   : {mt.cos(angulor):.3f}\n" 
f"Tangente : {mt.tan(angulor):.3f}\n" )

# Se muestra el valor de salida como resultado
print(salida)
