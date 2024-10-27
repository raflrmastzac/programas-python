# p129_medidas_longitud - Realiza la conversion de pulgadas a centimetros y de metros a pies segun el usuario lo seleccione

# Importa librería para limpiar la terminal
import os

def cent_pulg(pulg):
    cent = pulg * 2.54
    return cent

def pies_metr(metr):
    pies = metr * 3.28084
    return pies

# Programa principal
# Limpia el texto de la terminal
os.system("cls")

print("[ 1 ] conversion pulgadas a centimetros")
print("[ 2 ] Conversion metros a pies")
op = int(input("Elige ?"))

if op==1 :
    pulg = float(input("Dame un valor en pulgadas: "))
    print(f"El valor en centimetros corresponde a {cent_pulg(pulg):.4f}cm")

elif op==2: 
    metr = float(input("Dame un valor en metros: "))
    print(f"El valor en pies corresponde a {pies_metr(metr):.4f}ft")