# p57_factorial_numeros - Calcula el factorial de un numero

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

n = int(input("Dame un numero ?"))

for x in range(1, n+1):
    f = 1
    print(f"{x}! = ", end=" ")
    for i in range(1, x+1):
        f = f * i
        print(f"{i}! {"x" if i!=x else ""}", end=" ")
    print(f"= {f}")