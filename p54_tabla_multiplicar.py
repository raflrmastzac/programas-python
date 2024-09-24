# p54_tabla_multiplicar - imprime la tabla de multiplicar un ciclo for

# Importa librería para limpiar la terminal
import os

while True:
    # Limpia el texto de la terminal
    os.system("cls")

    t = int(input("Dame la tabla que deseas imprimir ? ") )
    n = int(input("Hasta donde deseas la tabla       ? ") )

    for i in range(1, n+1, 1):
        print(f"{t} x {i} = {t*i}")

    if input("\nContinuar (s/n)").lower().startswith("n"): break
print("\nProceso terminado ...")