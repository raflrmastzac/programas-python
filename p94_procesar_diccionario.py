# p94_procesar_diccionario - crea un diccionario a partir de dos listas y intera entre sus valores, realiza la suma y el promedio de los valores de sueldo

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

nombres = ["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]


trabajadores = dict(zip(nombres, sueldos))
print("Ambas listas resultando en el diccionario:\n")
print("Inicial", trabajadores, len(trabajadores))
print()

# Interando las llaves usando keys()
print("\nLas llaves:")
for k in trabajadores.keys():
    print(k, end=", ")
print()

# interando los valores usando values()
print("\nLos valores:")
for v in trabajadores.values():
    print(v, end=", ")
print()

# Interando la llave y el valor en base a la llave
print("\nLlaves y valores a la vez :")
for k, v in trabajadores.items():
    print(f"{k} - {v}")
print()

# Interando usando items() 
print("Diccionario utilizando items():")
for nombre, sueldo in trabajadores.items():
    print(f"{nombre} - {sueldo}")
print()

# Se definen variables
suma = prom = 0

# Se obtiene la suma y el promedio de los valores
for k, v in trabajadores.items():
    print(f"{k:<12} - {v}")
    suma += v
print("Sumando los valores de los sueldos de cada trabajador y obteniendo su promedio:")
prom = suma / len(trabajadores)
print(f"La suma de los valores totales es {suma}, el promedio de estos es {prom:.4f}")