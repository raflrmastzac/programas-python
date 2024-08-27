# p05_promedio_de_calificaciones - Calcular el promedio de 3 calificaciones


# Se inicializa el programa con un mensaje de inicio y se solicitan los datos
print("Calculando el promedio de 3 calificaciones \n")
print("Dame 3 calificaciones separadas por espacios:")

# Se declaran los datos y se aplica la función split para separar una cadena de datos por espacios
c1,c2,c3 = input().split()
c1,c2,c3 = [int(c1), int(c2), int(c3)]

# Se define las variables
suma = (c1+c2+c3)
prom = suma/3

# Se presentan los resultados
print(f"las calificaciones fueron {c1}, {c2}, {c3} ")
print(f"la suma es {suma}")
print(f"el promedio es {prom}")
