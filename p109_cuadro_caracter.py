# p109_cuadro_caracter - Funcion que dibuja un cuadro r x c, del caracter deseado

# Importa librería para limpiar la terminal
import os

def cuadro(r, c, car) :
    for i in range(1, r+1):
        for j in range(1, c+1):
            print(car, end=" ")
        print()

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

#cuadro(5,25,"$")
#cuadro(10,10,"@")
r = int(input("Cuantos renglones ? "))
c = int(input("Cuantas columnas  ? "))
car = input("De que catacter ? ")
cuadro(r, c, car)