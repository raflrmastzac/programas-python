#p33_conteo_numeros - Cuenta numeros, los suma, cuenta positivos, negativos, ceros, para parar -1

# Se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio
print("Cuenta numeros, los suma, cuenta positivo, negativos, ceros, para parar -1\n")

# Se definen variables
c = s = 0
cp = cn = cc = 0

while True:
    num = int(input("Numero ? "))
    if num == -1:
        break
    else:
        c = c + 1
        s = s + num
        if num > 0:
            cp = cp + 1 
        elif num < 0:
            cn = cn + 1
        else:
            cc = cc + 1

print(f"Capturaste {c} numeros y su suma es {s} ")
print(f"Positivos: {cp}\nNegativos: {cn}\nCeros: {cc}")
print("\nProceso terminado ...")