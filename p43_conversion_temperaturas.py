# p43_conversion_temperaturas - Calcula la temperatura convertida de grados centígrados a grados 
# Fahrenheit de un rango de valores dados

# Importa librería para limpiar la terminal
import os

while True:
    # Limpia el texto de la terminal
    os.system("cls")

    # Se da mensaje de inicio
    print("Calcula la temperatura de grados centígrados a Fahrenheit de un rango dado")

    # Se definen variables
    temp_inicial = float(input("Ingresa la temperatura inicial (grados centígrados): "))
    temp_final = float(input("Ingresa la temperatura final (grados centígrados): "))
    temp_actual = temp_inicial

    if temp_inicial < temp_final:
        while temp_actual <= temp_final:
            temp_fahrenheit = (temp_actual * 9/5) + 32
            print(f"{temp_actual}°C = {temp_fahrenheit:.2f}°F")
            temp_actual += 1
            
    elif temp_inicial > temp_final:
        while temp_actual >= temp_final:
            temp_fahrenheit = (temp_actual * 9/5) + 32
            print(f"{temp_actual}°C = {temp_fahrenheit:.2f}°F")
            temp_actual -= 1

    # Se pregunta al usuario si desea continuar
    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"):
        break

print("\nProceso terminado ...")
