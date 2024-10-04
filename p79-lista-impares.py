# p79-lista-impares - Llena una lista con los primeros n números impares, Calcula e imprime la suma y promedio

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

num_impar = []
num_im3 = []
c = suma = promedio = sum_d3 = 0

c = int(input("Cuantos elementos  ? "))

print("Introduce los numeros impares en orden acendente")
for i in range (c):
    c = int(input(f"Numero Impar[{i+1}]= "))
    if c % 2 != 0:
        num_impar.append(c)
    else:
        print("El numero ingresado no es un numero impar")

for c in num_impar:
    suma += c
promedio = suma / len(num_impar)

for c in num_impar:
    if c % 3 == 0:
        sum_d3 += c
        num_im3.append(c)

print("Numeros impares generados               : ", num_impar, len(num_impar))
print("Suma de los numeros impares             : ", suma)
print("Promedio de los numeros impares         : ", promedio)
print("Los numeros impares divisibles entre 3  : ", num_im3)
print("Suma de numeros divisibles entre 3      : ", sum_d3)

while True:
    el_busca = int(input("Intodruce un elemento a buscar ? "))

    if el_busca in num_impar:
        pos= num_impar.index(el_busca)
        print(f"El numero {el_busca} se encuentra en la lista, en la posicion {pos}")
    else:
        print("El numero ingresado no se encuentra en la lista")

    if input("\nContinuar (s/n)").lower().startswith("n"): break

print("\nProceso terminado")