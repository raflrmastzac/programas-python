# p84-conversion-moneda - Conversion a pesos

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

monedas = {
    "USD" : 20.50,  #Dolares
    "EUR" : 22.38,  #Euros
    "GBP" : 25.80,  #Libra esterlina
    "JPY" : 0.10,   #Yen Japones
    "CAD" : 16.20   #Dolar canadiense
}

print("Conversion de diferentes monedas a pesos mexicanos")
print("Monedas: ")
for m in monedas.keys(): print(f"- {m}")
while True:
    moneda = input("Moneda ? ").upper()
    if moneda in monedas: break

cantidad = float(input("Cantidad ? "))

resultado = cantidad * monedas[moneda]

print(f"{cantidad} {moneda} son {resultado} pesos.")
