# p21_aceptar_estudiante_v2 - aceptar estudiante en base a cierto criterios
# >=18   c1 >= 8  y  c2 >= 8

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("Universidad Patito SA de CV")
print("Aceptar un estudiante base a su edad y dos calificicaciones")

#Se definen variables
nombre = input("dame tu nombre ? ")
edad = int(input("dame tu edad ? "))

# Se realiza la primera seleccion
if edad >= 18 :
   print("Dame 2 calificaciones separadas por enter ?")
   # Se definen variables secundarias
   c1, c2 = input().split()
   c1, c2 = int(c1), int(c2)

   # Se realiza la segunda seleccion
   if c1 >= 8 and c2 >= 8:
    print(f"{nombre} bienvenid@ a la Universidad Patito, tu edad {edad} años y calificaciones {c1} y {c2} lo permiten")
   else:
       print("solo aceptamos alumnos con calificaciones mayores oi iguales a 8")

else:
    print("\nSolo aceptamos a mayores de edad")

print("\nGracias por utilizar este programa ...")