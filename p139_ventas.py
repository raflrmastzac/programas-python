# p139_ventas - Aplicacion orientada a objetos que simula las ventas de una tienda 

class Venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio
        self.total = cantidad * precio
    def __str__(self):
        return f"Articulo:{self.articulo:<20}  Cantidad:{self.cantidad:>10}  Precio:{self.precio:>10,.2f}   Total:{self.total:>10,.2f}"

class Cliente:
    def __init__(self, rfc, nombre, domicilio, correo):
        self.rfc = rfc
        self.nombre = nombre
        self.domicilio = domicilio
        self.correo = correo
        self.ventas = list()
    def agregarVenta(self, venta):
        self.ventas.append(venta)
    def totalTienda(self):
        total=0
        for venta in self.ventas:
            total += venta.total
        return total
    def __str__(self):
        return f"Cliente  [Nombre:{self.nombre:<20}  RFC:{self.rfc:<15}  Domicilio:{self.domicilio:<20}  Correo:{self.correo:<30}]"
    
class Tienda:
    def __init__(self, nombre, domicilio, propietario):
        self.nombre = nombre
        self.domicilio = domicilio
        self.propietario = propietario
        self.clientes = list()
    def agregarCliente(self, cliente):
        self.clientes.append(cliente)
    def totalVentas(self):
        total = 0
        for cliente in self.clientes:
            total += len(cliente.ventas)
        return total
    def totalImporteVentas(self):
        total = 0
        for cliente in self.clientes:
            total += len(cliente.ventas)
        return total
    def __str__(self):
        return f"Tienda [Nombre: {self.nombre:<25}  Domicilio: {self.domicilio:<25} Propietario: {self.propietario:<25} - Total ventas: {self.totalImporteVentas()}]"


# permite capturar un cliente
def capturaCliente():
    print("Dame los datos del ciente")
    rfc       = input("RFC       :")
    nombre    = input("Nombre    :")
    domicilio = input("Domicilio :")
    correo    = input("Correo    :")
    cliente = Cliente(rfc, nombre, domicilio, correo)
    return cliente

# Permite agregar las ventas de cada cliente 
def agregarVentas(cliente):
    print("Captura de Ventas ", cliente.nombre)
    while True:
        articulo = input("Articulo:   ")
        if articulo=="":
            break
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio:  "))
        cliente.agregarVenta(Venta(articulo, cantidad, precio))
    

def main():
    # Importa librería para limpiar la terminal
    import os

# Limpia el texto de la terminal
    os.system("cls")
    # Crea una tienda
    mitienda = Tienda("Ferreteria las lomas", "Av Luis Moya 345)", "Carlos Castañeda")
    # Agrega un cliente a la tienda
    mitienda.agregarCliente(Cliente("CARC711202", "Carlos Castañeda", "Av Mexico 115", "castr@uaz.edu.mx"))
    # Agrega ventas al cliente
    mitienda.clientes[0].agregarVenta(Venta("Martillo", 10, 200))
    mitienda.clientes[0].agregarVenta(Venta("Pala", 5, 200))
    mitienda.clientes[0].agregarVenta(Venta("Cinta de aislar", 15, 35))
    # Agrega un segundo cliente a la tienda
    mitienda.agregarCliente(Cliente("JOSE850324", "Jose Perez",  "Sierra Nevada 354", "Jose@gmail.com"))
    # Agrega ventas al segundo cliente
    mitienda.clientes[1].agregarVenta(Venta("Pinzas", 10, 650.33)) 
    mitienda.clientes[1].agregarVenta(Venta("Thiner", 50, 65))
    # Agrega un tercer cliente a la tienda
    mitienda.agregarCliente(Cliente("SOBR731123", "Rocio Soto",  "Sierra Tecuan 354", "rocio@gmail.com"))
    # Agrega ventas al tercer cliente
    mitienda.clientes[2].agregarVenta(Venta("Talache", 2, 1650.33))     

    cliente = capturaCliente()
    agregarVentas(cliente)
    mitienda.agregarCliente(cliente)

    # Reporte
    print("\nReporte de ventas :\n", mitienda)
    print("Clientes            :", len(mitienda.clientes))
    print("Ventas              :", mitienda.totalVentas())
    for cliente in mitienda.clientes:
        print(cliente)
        for venta in cliente.ventas:
            print(venta)
        print()

# Programa principal
if __name__ == '__main__':
    main()