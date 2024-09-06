# p27_calculo_nota - Evalua el resultado del promedio de 5 calificaciones ingresadas y imprime un mensaje de acuerdo al promedio obtenido.

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("Evalua el resultado del promedio y imprime un mensaje de acuerdo al promedio obtenido")
nombre = input("dame tu nombre ? ")

# Se definen variables
print("Ingresa las calificaciones correspondientes separadas por enter ?")
c1, c2, c3, c4, c5 = input().split()
c1, c2, c3, c4, c5 = int(c1), int(c2), int(c3), int(c4), int(c5)

# Se realizan los calculos necesarios
prom = (c1 + c2 + c3 + c4 + c5) / 5

# Se realiza la clasificacion y seleccion 
if prom >= 0 and prom < 6:
    print(f"{nombre}, Tu calificacion es {prom}, Quedas reprobado")

elif prom >= 6 and prom < 7:
    print(f"{nombre}, Tu calificacion es {prom}, Pasas de panzazo")

elif prom >= 7 and prom < 8:
    print(f"{nombre}, Tu calificacion es {prom}, Muy bien, puedes mejorar")

elif prom >= 8 and prom < 9:
    print(f"{nombre}, Tu calificacion es {prom}, Excelente sigue así")

elif prom >= 9 and prom <= 10:
    print(f"{nombre}, Tu calificacion es {prom}, Perfecto tu esfuerzo valió la pena")

else:
    print("\nLos valores ingresados son incorrectos, vuelve a intentarlo ...")

print("\nGRacias por utilizar este programa ...")