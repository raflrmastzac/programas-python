# p20_ley_de_newton - segunda ley de newton (fuerza = masa * aceleracion)

# se limpia el texto de la terminal
import os; os.system("cls")

# Se da mensaje de inicio y se definen los metodos a aplicar
print("Calculando los valores de la segunda ley de newton (f=m*a)")
print("[F] calcular la fuerza        (F=m*a)")
print("[M] calcular la masa          (m=f/a)")
print("[A] calcular la aceleracion   (a=f/m)")

# Se definen variables
op = input("Elige una opcion ? ").upper()

# Se realiza el proceso de seleccion
if op=="F":
    print("\nCalculando la fuerza ...")
    m = float(input("dame la masa         ? "))
    a = float(input("dame la aceleración  ? "))
    f = m * a
    print(f"la fuerza es {f}")

elif op=="M":
    print("\nCalculando la masa ..")
    f = float(input("dame la fuerza       ? "))
    a = float(input("dame la aceleración  ? "))
    m = f / a
    print(f"la masa es {m}")

elif op=="A":
    print("\nCalculando la aceleración ..")
    f = float(input("dame la fuerza  ? "))
    m = float(input("dame la masa    ? "))
    a = f / m
    print(f"la aceleración es {a}")

else :
    print("\nOpcion invalida ..")

print("\nProceso termninado ...")
