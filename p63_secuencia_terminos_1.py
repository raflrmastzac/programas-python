# p63_secuencia_terminos_1 -  Imprime la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

print("Imprime la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma\n")
t = int(input("Cuantos terminos ?? "))
suma = 0
f = 1

for i in range(1, t+1):
    f *= i
    ter = 1 / f
    suma += ter
    print(f"{"1" if i==1 else f"1/{i}!"} {"+" if i!=t else ""}", end=" ")

print(f"\nSuma: {suma}")
print("\nProceso terminado... ")