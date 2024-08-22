# p01_hola_mundo - Recibe datos del ususario y los imprime en la pantalla

nombre = input ("Dame tu nombre ? ")
edad = int(input("Edad ?"))
peso = float( input("Peso ?"))

print (nombre)
print (edad)
print (peso)

print(f"{nombre} Bienvenido a Python, tu edad es {edad} tu peso es {peso}")

print(type(nombre))
print(type(edad))
print(type(peso))