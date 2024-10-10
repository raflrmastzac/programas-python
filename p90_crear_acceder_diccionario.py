# p90-crear-acceder-diccionario - Selecciona un valor dentro de un diccionario de datos

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

dias = {
    1 : "Lunes",
    2 : "Martes",
    3 : "Miercoles",
    4 : "Jueves",
    5 : "Viernes",
    6 : "Sabado",
    7 : "Domingo"
}

# Se imprime el diccionario
print("Diccionario de dias de la semana")
print("Inicial", dias, len(dias))
print()

# Mostrando elementos especificos del diccionario usando []
print("El primer elemento : ", dias[1])
print("El ultimo elemento : ", dias[7])
print()

# Mostrando elementos especificos del diccionario usando get()
print("El quinto elemento: ", dias.get(5))
print("El septimo elemento: ", dias.get(7))
print()

# Se muestra el diccionario en forma de tabla
print("Tabla de valores (dias)")
print("Final\n")
for k, v in dias.items():
        print(f"{k} - {v}")
