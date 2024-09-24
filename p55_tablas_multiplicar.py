# - p55_tablas_multiplicar - imprime las tablas del 1 a la tabla n, desde 1 hasta m

# Importa librería para limpiar la terminal
import os

while True:
    # Limpia el texto de la terminal
    os.system("cls")

    n = int(input("Hasta que tabla quieres      ? ") )
    m = int(input("Hasta donde deseas la tabla  ? ") )

    for i in range(1, n+1):
        print("Tabla del " + str(i) )
        for j in range(1, m+1):
            print(f"{i} x {j} = {i*j}")
        print()

    if input("\nContinuar (s/n)").lower().startswith("n"): break
print("\nProceso terminado")