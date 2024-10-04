# p80-estudiante - Datos de un estudiante usando diccionario

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

estudiante = { "Nombre"  : "Juan Perez",
               "Edad"    : 45,
               "Correo"  : "jperez@msn.com",
               "Carrera" : "Sistemas"}

print("El estudiante:  ", estudiante, len(estudiante))

estudiante["Calificacion"] = 9.5
estudiante["Correo"] = "juanp@gmail.com"
print("El estudiante: ", estudiante, len(estudiante))

print("\nLlaves ", estudiante.keys())
for k in estudiante.keys():
    print(k, end=" ")

print("\n\nValores ", estudiante.values())
for v in estudiante.values():
    print(v, end=" ")

print("\n\nLlaves y valores al mismo tiempo")
for k, v in estudiante.items():
    print(f"{k:<15}  : {v}")

print("\n\nLlaves y valores al mismo tiempo - forma 2")
for k in estudiante.keys():
    print(f"{k:<15} : {estudiante[k]}")
