# p100_segundo_examen_parcial - Procesar los datos de empleados de una empresa de muebles

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

empleados = []

print("Muebleria Muebles Dico S.A. de C.V.")
print("Sistema de Procesamiento de Empleados\n")
print("-----Captura de datos de los empleados------\n")

while True:
    nombre = input("Introduce el nombre del empleado: ")
    edad = int(input("Introduce la edad del empleado: "))
    sexo = input("Introduce el sexo del empleado (h/m): ")
    pasatiempo = input("Introduce los pasatiempos (separados por comas): ").split(", ")
    sueldo = float(input("Introduce el sueldo del empleado: "))

    empleado = {
        "nombre"     : nombre,
        "edad"       : edad,
        "sexo"       : sexo,
        "pasatiempo" : pasatiempo,
        "sueldo"     : sueldo
    }

    empleados.append(empleado)

    contin = input("Deseas agregar otro empleado? (s/n): ")
    if contin.lower() != "s":
        break

print("\nLista de Empleados:")
for emp in empleados:
    if emp == "*":
        break
    else:
        print(emp)
        print()

print("\nTabla de datos:")
print(f"{"Nombre":<10} {"Edad":<5} {"Sexo":<5} {"Sueldo":<10} {"Pasatiempo"}")

for emp in empleados:
    print(f"{emp["nombre"]:<10} {emp["edad"]:<5} {emp["sexo"]:<5} {emp["sueldo"]:<10.2f} {", ".join(emp["pasatiempo"])}")


print("\nResumen:")
# Variables
total_empleados = len(empleados)
total_hombres = total_mujeres = suma_edad = suma_sueldo = 0
pasatiempo_contador = {}
empleado_mayor = empleado_menor = empleados[0]

for emp in empleados:
    # Contar hombres y mujeres
    if emp["sexo"] == "h":
        total_hombres += 1
    elif emp["sexo"] == "m":
        total_mujeres += 1
    
    # Sumar edad y sueldo
    suma_edad += emp["edad"]
    suma_sueldo += emp["sueldo"]
    
    # Buscar el empleado mayor y menor
    if emp["edad"] > empleado_mayor["edad"]:
        empleado_mayor = emp
    if emp["edad"] < empleado_menor["edad"]:
        empleado_menor = emp
    
    # Contar pasatiempos
    for hobby in emp["pasatiempo"]:
        if hobby in pasatiempo_contador:
            pasatiempo_contador[hobby] += 1
        else:
            pasatiempo_contador[hobby] = 1

# Calcular promedios
promedio_edad = suma_edad / total_empleados
promedio_sueldo = suma_sueldo / total_empleados

# Mostrar resumen
print(f"Total de Empleados  : {total_empleados}")
print(f"Mujeres             : {total_mujeres}")
print(f"Hombres             : {total_hombres}")

print("\nPasatiempos:")
for hobby, count in pasatiempo_contador.items():
    print(f"{hobby}: {count}")

print(f"\nSuma de edades      : {suma_edad}")
print(f"Promedio de edades    : {promedio_edad:.2f}")
print(f"Suma de sueldos       : {suma_sueldo:.2f}") 
print(f"Promedio de sueldos   : {promedio_sueldo:.2f}")

print(f"\n{empleado_mayor['nombre']} de {empleado_mayor['edad']} años es el(a) mayor.")
print(f"{empleado_menor['nombre']} de {empleado_menor['edad']} años es el(a) menor.")