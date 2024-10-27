# p128_dia_semana - Ingresa un numero entre 1 y 7 y regresa el dia de la semana especifico

# Importa librería para limpiar la terminal
import os

def leerdatos():
    d = int(input(f"Ingresa un numero: "))
    return d

def diasemana (dia):
    dias=["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    if dia < 1 or dia > 7:
        return "El valor ingresado es incorrecto"
    else:
        return dias[dia-1]

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

print("Dia de la semana mediante numeros")
nums = leerdatos()
ndias = diasemana (nums)
print("El dia de la semana es:", ndias)