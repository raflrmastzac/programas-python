# p25_dia_de_la_semana - Muestra con letra el dia de la semana correspondiente en base a un numero dado entre 1 y 7,
# tal que 1 sea domingo y 7 viernes

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("Muestra con letra el dia de la semana correspondiente en base a un numero dado entre 1 y 7")

# Se definen variables
num = int(input("Dame un numero ?"))

# Se realiza proceso de seleccion
if num == 1:
    print("\nHoy es domingo")

elif num == 2:
    print("\nHoy es lunes")

elif num == 3:
    print("\nHoy es martes")

elif num == 4:
    print("\nHoy es miercoles")

elif num == 5:
    print("\nHoy es jueves")

elif num == 6:
    print("\nHoy es viernes")
elif num == 7:
    print("\nHoy es sabado")

else:
    print("\nEl valor especificado es incorrecto")

print("\nGracias por utilizar este programa ...")