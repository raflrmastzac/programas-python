# p17_convertir_temperatura - convertir temperaturas de centigrados de farenheit y vicebersa

import os; os.system("cls")

print("convertir temperaturas de centigrados de farenheit y vicebersa")
print("[1] convertir Farenheit a Celsius ")
print("[2] convertir Celsius a Farenheit ")
op = int(input("Elige ? "))

if op == 1:
    print("convirtiendo de Farenheit a celsius")
    temp = float(input("Dame los grados Farenheit ?"))
    res = (temp - 32) * 5/9
    print(f"{temp} Farenheit equivale a {res} Celsius")
else:
    print("convertiendo de Celsius a Farenheit")
    temp = float(input("Dame los grados Celsius ? "))
    res = (temp * 9/5) + 32
    print(f"{temp} Celsius equivale a {res} Frenheit")


