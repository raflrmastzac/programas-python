# p76-meses-dia-nombre - Lee un número de mes, e imprime el mes y sus dias en el mes

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = 0
while True:
    mes = int(input("Numero de mes ? "))
    if 1 <= mes <= 12:
        break

print(f"Mes  : {meses[mes-1]}, {dias[mes-1]}")
