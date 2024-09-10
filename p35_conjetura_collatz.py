# p35_conjetura_collatz - Calcula y imprime los numeros de la conjetura de Collatz

# Importa libreria para limpiar terminal
import os

while(True):
    # Limpia el texto de la terminal
    os.system("cls")

    # Se da mensaje de inicio
    print("Calcula y imprime los numeros de la conjetura de Collatz")

    # Se definen variables
    num = int(input("Dame un entero positivo "))
    
    while num != 1:
        print(num, end=" ")
        if num % 2 == 0:
            num = num // 2
        
        else:
            num = num * 3 + 1
    
    print(num, end=" ")
    if input("\n\nDeseas Continuar(S/N)? ").upper().startswith("N"): break

print("\nProceso terminado")
