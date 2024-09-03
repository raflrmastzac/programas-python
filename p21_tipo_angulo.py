# p21_tipo_angulo - Muestra al tipo de angulo en base a su magnitud
# <90 agudo, =90 recto, >90 y <180 obtuso, =180 llano,

# Se limpia el texto de la terminal >180 y <360 concavo
import os; os.system("cls")

print("Mostrando el tipo de angulo en base a su magnitud en grados")

# Se definen variables 
angulo = int(input("Dame un angulo ?"))

# Se realiza el proceso de seleccion
if angulo>=0 and angulo<=360:
    print(f"El angulo tiene {angulo} grados, por lo tanto es un angulo: ",end="")
    if angulo < 90: 
        print("Agudo")
    elif angulo == 90:
        print("Recto")
    elif angulo > 90 and angulo < 180 :
        print("Obtuso")
    elif angulo == 180:
        print("Llano")
    elif angulo > 180 and angulo < 360 :
        print("Concavo")
    else:
        print("Cerrado o completo")
else :
    print("\nEl angulo esta fuera de rango")

print("\nGracias por utilizar este programa ...")