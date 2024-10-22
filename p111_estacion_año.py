# p111_estacion_año - Funcion que regresa una cadena con la estacion del año, recibe como parametro un numero entre 1 y 4

# Importa librería para limpiar la terminal
import os

# Estacion del año
def estacion(n):
    if n==1:
        est="Primavera"
    elif n==2:
        est="Verano"
    elif n==3:
        est="Otoño"
    elif n==4:
        est="Invierno"
    else:
        return "Error"


# Programa principal
# Limpia el texto de la terminal
os.system("cls")

n = int(input("Dame la estacion del año (1-4) y te la doy con letra: " ))
print(f"La estacion es {estacion(n)}")