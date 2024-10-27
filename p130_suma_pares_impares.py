# p130_suma_pares_impares - Suma la cantidad de numeros impares y pares dentro de un rango especifico

# Importa librería para limpiar la terminal
import os

def sum_rango(n1, n2, type):
    sum = 0
    # Numeros pares
    if type == "p":
        for n in range(n1, n2+1):
            if n % 2 == 0:
                sum += 1
    #Numeros impares
    elif type == "i":
        for n in range(n1, n2+1):
            if n % 2 != 0:
                sum += 1
            
    return sum

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

while True:
    print("[ 1 ] Sumar numeros pares en el rango")
    print("[ 2 ] Sumar numeros impares en el rango")
    op = int(input("Elige una opcion?"))

    if op == 1:
        n1 = int(input("Introduce el valor inicial del rango: "))
        n2 = int(input("Introduce el valor final del rango:   "))
        res = sum_rango(n1, n2, "p")
        print(f"\nLa suma de los números pares entre {n1} y {n2} es:", res)
    
    elif op == 2:
        n1 = int(input("Introduce el valor inicial del rango: "))
        n2 = int(input("Introduce el valor final del rango:   "))
        res = sum_rango(n1, n2, "i")
        print(f"\nLa suma de los números impares entre {n1} y {n2} es:", res)

    else:
        print("\nEl valor ingresado es incorrecto")
    
    # Se pregunta al usuario si desea continuar
    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"):
        break

print("\nProceso terminado ...")
