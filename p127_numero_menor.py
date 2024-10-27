# p127_numero_menor - Seleciona el valor menos de 3 datos ingresados

# Importa librería para limpiar la terminal
import os

def leerdatos():
    datos = []
    for i in range(3):
        d = int(input(f"Dame el numero {i+1}: "))
        datos.append(d)
    return datos

def menor(numero1, numero2, numero3):
    if numero1<=numero2 and numero1<=numero3:
        return numero1
    elif numero2<=numero1 and numero2<=numero3:
        return numero2
    else:
        return numero3
    
# Programa principal
# Limpia el texto de la terminal
os.system("cls")

print("Ingresa 3 numeros para comenzar")
nums = leerdatos()
print("Numero ingresados: ", nums)

men = menor(nums[0], nums[1], nums[2])
print(f"El menor numero es: ", men)

