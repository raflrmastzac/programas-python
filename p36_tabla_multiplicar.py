# p36_tabla_multiplicar - Imprime la tabla de multiplicarque el ususario pida hasta donde la pida

# Importa libreria para limpiar terminal
import os

while(True):
    # Limpia el texto de la terminal
    os.system("cls")

    # Se da mensaje de inicio
    print("Imprime la tabla de multiplicarque el ususario pida hasta donde la pida")

    # Se definen variables
    t = int(input("Que tabla quieres ? "))
    n = int(input("Hasta donde       ? "))

    c = 1
    while c <= n:
        print(f"{t} x {c} = {t*c}")
        c += 1
    
    if input("\n\nDeseas Continuar(S/N)? ").upper().startswith("N"): break

print("\nProceso terminado")

