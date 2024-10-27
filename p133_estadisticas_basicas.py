# p133_estadisticas_basicas - Realiza el calculo de valores estadisticos de una lista de datos proporcionada por el usuario.

# Importa librerías a usar
import os
from math import sqrt

def leerdatos():
    datos=[]
    while True:
        d=int(input("Dame números: "))
        if d==-1: break
        datos.append(d)
    return datos

def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

def media(lista):
    s = 0
    for n in lista:
        s = s + n
        med = s / len(lista)
    return med

def varianza(lista, tipo_varianza):
    med = media(lista)
    suma = sum((n - med) ** 2 for n in lista)
    
    if tipo_varianza == 1:
        # Varianza poblacional
        v = suma / len(lista)
    elif tipo_varianza == 2:
        # Varianza muestral
        v = suma / (len(lista) - 1)
    return v

def desviacion(lista, tipo_varianza):
    v = varianza(lista, tipo_varianza)
    d = sqrt(v)
    return d

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

while True:
    lisval = leerdatos()

        # Pregunta si quiere varianza poblacional o muestral
    print("\nSeleccione el tipo de varianza que desea calcular:")
    print("1. Varianza poblacional")
    print("2. Varianza muestral")
    tipo_varianza = int(input("Elige (1 o 2): "))

    medi = media(lisval)
    may = mayor(lisval)
    men = menor(lisval)
    var = varianza(lisval, tipo_varianza)
    des = desviacion(lisval, tipo_varianza)

    print("Lista de numeros     :", lisval)
    print("La media             :", medi)
    print("Mayor de los datos   :", may)
    print("Menor de los datos   :", men)
    print("Varianza             :", var)
    print("Desviancion estandar :", des)

    # Se pregunta al usuario si desea continuar
    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"):
        break

print("\nProceso terminado ...")