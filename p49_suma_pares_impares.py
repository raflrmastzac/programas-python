# p49_suma_pares_impares - Imprime numeros pares de n a 2 y suma numeros impares de 1 a n, la suma en ambos casos

# Importa librería para limpiar la terminal
import os

while True:
    # Limpia el texto de la terminal
    os.system("cls")

    print("[1] Imprimir numeros pares de n a 2")
    print("[2] Imprimir numeros impares de 1 a n")
    print("[3] Salir            ")
    op = int(input("Elige ? "))
    s = 0

    if op==1:
        print("Imprimiendo numeros pares de n a 2")
        n = int(input("Desde donde ?"))
        n = n if n%2==0 else n-1
        for x in range(n, 1, -2):
            print(x, end=" ")
            s = s + x
        print("\nLa suma de pares es" + str(s))

    elif op==2:
        print("Imprimiendo numeros impares de 1 a n")
        n = int(input("Hasta donde ?"))
        n = n if n%2!=0 else n-1
        for x in range(1, n+1, 2):
            print(x, end=" ")
            s = s + x
        print("\nLa suma de impares es" + str(s))

    elif op==3:
        break
    else:
        print("\nOpcion invalida")

    input("\n < preciona cualquier tecla para continuar >")
print("\nproceso terminado ...")