# p82-nombres y edades - El usuario introduce nombres y edades, se calcula la suma y el promedio

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

datos = {}

print("Introduce nombres y edades (vacio para terminar) ")
while True:
    nombre = input("Nombre ? ")
    if nombre != "":
        datos[nombre] = int(input("Edad ? "))
    else:
        break

print("Datos : ", datos, len(datos))

s = 0
for n, e in datos.items():
    print(f"{n:<20} - {e:2} ")
    s = s + e

print(f"\nSuma : {s} - Promedio: {s/len(datos)}")
