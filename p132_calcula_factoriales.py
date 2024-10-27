# p132_calcula_factoriales - obtiene el factorial de una lista de valores ingresados por el ususario

# Importa librería para limpiar la terminal
import os

def leerdatos():
    datos=[]
    while True:
        d=int(input("Dame los números: "))
        if d==-1: break
        datos.append(d)
    return datos

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

def list_fac(list):
    list_datos = []
    for n in list:
        list_datos.append(factorial(n))
    return list_datos

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

while True:
    print("Calculando factorial de una lista de datos\n")
    lisval = leerdatos()
    list_datos = list_fac(lisval)
    print("La lista de los numero originales :", lisval)
    print("La lista con los factoriales      :", list_datos)

    # Se pregunta al usuario si desea continuar
    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"):
        break

print("\nProceso terminado ...")