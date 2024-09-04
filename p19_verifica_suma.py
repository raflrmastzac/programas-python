# p19_verificar suma - verificar si la suma de dos numeros es igual a un terecero
# 4 5 9 ?    4 9 5 ?    9 4 5 ?   4 4 4 ?   3 5 7 ?

# Se limpia texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio 
print("Verificar si la suma de dos numeros es igual a un tercero")
print("Dame 3 numeros enteros separados por espacio?")

#Se definen variables 
n1, n2, n3 = input().split()
n1, n2, n3 = [int(n1), int(n2), int(n3)]

# Se realiza el proceso de seleccion
if n1 + n2 == n3:
    print(f"{n1} + {n2} = {n3}")

elif n1 + n3 == n2:
    print(f"{n1} + {n3} = {n2}")

elif n2 + n3 == n1:
    print(f"{n2} + {n3} = {n1}")

elif n1 == n2 == n3:
    print(f"{n1} = {n2} = {n2}")

else:
    print(f"Los numeros son diferentes:   {n1}, {n2}, {n3}")

print("Proceso terminado ... ")
