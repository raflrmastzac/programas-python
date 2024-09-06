# p26_numero_romanos - Muestra la equiuvalencia a numero romano dado un numero entre un rango de 1 a 10

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("Muestra la equiuvalencia a numero romano dado un numero entre un rango de 1 a 10")

# Se definen variables
num = int(input("Dame un numero entre 1 a 10 ?"))

# Se realiza proceso de seleccion
if num == 1:
    print(f"\nEl numero {num} equivale a I")
    
elif num == 2:
   print(f"\nEl numero {num} equivale a II")
    
elif num == 3:
    print(f"\nEl numero {num} equivale a III")
    
elif num == 4:
    print(f"\nEl numero {num} equivale a IV")
    
elif num == 5:
    print(f"\nEl numero {num} equivale a V")
    
elif num == 6:
    print(f"\nEl numero {num} equivale a VI")
    
elif num == 7:
    print(f"\nEl numero {num} equivale a VII")
    
elif num == 8:
    print(f"\nEl numero {num} equivale a VIII")
    
elif num == 9:
    print(f"\nEl numero {num} equivale a IX")
    
elif num == 10:
    print(f"\nEl numero {num} equivale a X")

else:
    print("\nEl valor especificado es incorrecto")

print("\nGracias por utilizar este programa ...")