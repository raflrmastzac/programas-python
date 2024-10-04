# p83-conversion-medida - Conversion a metros de km, m, cm, mm

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

conversiones = {
    "km"  :  1000,  # Kilometros
    "m"   :  1,     # Metros
    "cm"  :  0.01,  # Centimetros
    "mm"  :  0.001  # Milimetros
}

longitud = int(input("Longitud : "))

while True:
    print("Unidades: ", conversiones.keys())
    unidad = input()
    if unidad in conversiones:
        break

resultado = longitud * conversiones[unidad]

print(f"Longitud: {longitud} {unidad} son {resultado} metros")
