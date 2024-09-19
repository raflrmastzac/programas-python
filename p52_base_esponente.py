# p52_base_esponente - Eleva un numero base a su exponente

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

base = int(input("Base        ?"))
exp = int(input("Exponente    ?"))

#print(f"La base {base} elevado a la {exp} es {base ** exp})

p = 1
for i in range(exp):
    p = p * base
print(f"La base {base} elevado a la {exp} es {p}")

p = 1
for _ in range(exp):
    p = p * base
else:
    print("\nEl ciclo termino correctamente")

print(f"La base {base} elevado a la {exp} es {p}")

