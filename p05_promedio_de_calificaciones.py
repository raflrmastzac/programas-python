# p05_promedio_de_calificaciones - Calcular el promedio de 3 calificaciones

# Se inicializa el programa con un mensaje de inicio y se solicitan los datos
print("Calculando el promedio de 3 calificaciones \n")
print("Dame 3 calificaciones separadas por espacios:")

# Se declaran los datos y se aplica la función split para separar una cadena de datos
c1,c2,c3 = input().split()
c1,c2,c3 = [int(c1), int(c2), int(c3)]

# Se solicita el nombre del alumno
nombre = input("Dame tu nombre ?")

# Se define la variable de promedio
prom = (c1+c2+c3)/3

# Se presentan los resultados
print(f"{nombre} el promedio de : {c1},{c2},{c3} es {prom}")
