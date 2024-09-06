# p32_numeros_suma_100 - imprime numeros hasta llegar a una suma de 100

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("\n imprime numeros hasta llegar a una suma de 100\n")

# Se definen variables
c = 0
s = 0

# Se inicia el ciclo
while c + 300:
    c = c + 1
    s = s + c
    print(c , end=" ")
    if s >= 8000:
        print("\n")
        break

# imprime el resultado
print(f"La suma es {s}, sumando {c} numeros")
