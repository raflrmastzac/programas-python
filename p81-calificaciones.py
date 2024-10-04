# p81-calificaciones - Materias y calificaciones en un diccionario 

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

materias = ["fisica", "Quimica", "Matematicas", "Geografia", "Estadistica"]
califs = [10, 9, 8, 7.5, 6]

print("Listas originales : ", materias, califs)

notas = dict(zip(materias,califs))

print("Todo : ", notas, len(notas))

notas.update({"Ingles":10})
notas.update({"Programacion":7})
print("Todo : ", notas, len(notas))
# Actualizar
notas.update({"Fisica":9,"Quimica":10})
print("Todo : ", notas, len(notas))
#Remover
notas.pop("Fisica")
notas.popitem()
print("Todo : ", notas, len(notas))
#Actualizar
notas["Geografia"] = 8
notas["Estadisticas"] = 7
print("Todo : ", notas, len(notas))
#Iterar
s=0
print("\nMaterias y Calificaciones")
for m, c in notas.items():
    print(f"{m:15} - {c:5}")
    s = s + c
print(f"\nSuma: {s} - promedio: {s/len(notas)}")

# Borrar
notas.clear()
print(notas, len(notas))
