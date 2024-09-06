# p28_aceptar_estudiante_v2 - aceptar un estudiante en base a cierto criterios

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("Universidad Kitty Kat SA de CV")
print("Aceptar un estudiante base a su edad, sexo y tres calificicaciones")

#Se definen variables
nombre = input("dame tu nombre ? ")
edad = int(input("dame tu edad ? "))

# Se realiza la primera seleccion
if edad >= 21 :
   # Se realiza la segunda seleccion
   sexo = input("Cual es tu sexo [M] masculino, [F] femenino ?").upper()
   
   if sexo == "F":
     print("Dame 3 calificaciones separadas por enter ?")
     # Se definen variables secundarias
     c1, c2, c3 = input().split()
     c1, c2, c3 = int(c1), int(c2), int(c3)

     prom = (c1 + c2 + c3)/ 3
   
     if 8 <= prom <= 9.5:
       print(f"\n{nombre} has sido aceptada, tu edad de {edad} y tus calificaciones {c1}, {c2} y {c3}, con un promedio de {prom:.4f} lo permiten")
    
     else:
       print(f"\n{nombre} Eres mujer, tienes la edad, pero tu promedio no alcanza solo promedios de 8 a 9.5")
    
   else:
     print("\nSolo aceptamos a mujeres")

else:
    print("\nSolo aceptamos a personas mayores de 21 años")

print("\nGracias por utilizar este programa ...")