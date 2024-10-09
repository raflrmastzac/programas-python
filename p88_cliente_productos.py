# p88_cliente_productos - 

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

n = int(input("Cuantas compras ? "))

compras = []

for i in range(1, n+1):
    print(f"\n----------Compra {i} ---------")
    compra = {
        "cliente"  : input("Nombre: "),
        "producto" : input("Producto: "),
        "cantidad" : int(input("Cantidad:")),
        "precio"   : float(input("Precio:"))
    }
    compras.append(compra)

print(compras)

# Calcular cantidad de productod y subtotal por el cliente
clientes = {}
for compra in compras:
    cliente = compra["cliente"] # creamos una entrada al diccionario por cada cliente
    if cliente not in clientes:
        clientes[cliente] = {"cantidad":0, "subtotal":0} #creamos un sub diccionario por cada cliente
    clientes[cliente]["cantidad"] += compra["cantidad"]
    clientes[cliente]["subtotal"] += compra["cantidad"] * compra["precio"]

# Imprime clientes y subtotales (diccionario de diccionario)
print(clientes)

print("Datos finales")
for cliente, datos in clientes.items():
    print()
    print("cliente", cliente)
    print("Cantidad", datos["cantidad"])
    print("Subtotal", datos["subtotal"])