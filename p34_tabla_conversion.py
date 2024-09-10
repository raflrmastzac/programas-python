# p34_tabla_conversion - Imprimir una tabla de coversion peso a dollar

while(True):
    # Se limpia el texto de la terminal
    import os; os.system("cls")
    
    # Se da mensaje de inicio
    print("Imprimir una tabla de coversion peso a dollar\n")

    # Se definen variables
    tc = 19.87

    while(True):  # Pide valores hasta que pi < pf
        pi = float(input("Valor en pesos inicia: "))
        pf = float(input("Valor en pesos final : "))
        if pi < pf:
            break
    
    c = pi

    print("\nPeso\tDollar")
    print("-"*15)
    while c <= pf :
        print(f"{c}\t{c/tc:.2f}")
        c+=1
    print("-"*15)

    if input("Deseas continuar (S/N) ? ").upper().startswith("N"): break

print("\nProceso terminado")
