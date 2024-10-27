# p131_suma_digitos_lista - suma los digitos de una lista de numeros ingresados por el usuario

# Importa librería para limpiar la terminal
import os

def leerdatos():
    datos=[]
    while True:
        d=int(input("Dame los números: "))
        if d==-1: break
        datos.append(d)
    return datos

def sumadigitos(n):
    suma=0
    while n!=0:
        dig = n % 10
        suma = suma + dig
        n = n // 10
    return suma

def sumdiglist(list):
    sulist_datos = []
    for n in list:
        sulist_datos.append(sumadigitos(n))
    return sulist_datos

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

while True:
    print("Contando los digitos de una lista de datos\n")
    lisdat = leerdatos()
    sulist_datos = sumdiglist(lisdat)
    print("La lista de los numero originales              :", lisdat)
    print("La lista con la suma de digitos de los numeros :", sulist_datos)

    # Se pregunta al usuario si desea continuar
    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"):
        break

print("\nProceso terminado ...")
