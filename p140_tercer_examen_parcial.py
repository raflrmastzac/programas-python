# p140_tercer_examen_parcial - Aplicacion orientada a objetos que simula los registros de jugadores dentro de una academia en base a su categoria 

class Jugador:
    def __init__(self, nombre, año_nac, sexo, becado):
        self.nombre = nombre
        self.año_nac = año_nac
        self.sexo = sexo
        self.becado = becado
    def __str__(self):
        becado_str = "Becado" if self.becado else "Sin Beca"
        return f"Nombre: {self.nombre:<20} AñoNac: {self.año_nac:<8} Sexo: {self.sexo:<12} Becado: {becado_str}"

class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []
    def obtenerJugador(self, jugador):
        self.jugadores.append(jugador)
    def totalJugadores(self):
        return len(self.jugadores)
    def subtotalIngresos(self):
        subtotal = 0
        for jugador in self.jugadores:
            subtotal += self.costo
        return subtotal
    def __str__(self):
        return f"Nombre: {self.nombre:<10} Rango: {self.rango:<20} Costo: ${self.costo:,.2f}"

class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []
    def obtenerCategoria(self, categoria):
        self.categorias.append(categoria)
    def totalCategorias(self):
        return len(self.categorias)
    def totalHom_Muj(self):
        t_hombres = 0
        t_mujeres = 0
        for categoria in self.categorias:
            for jugador in categoria.jugadores:
                if jugador.sexo == "Hombre":
                    t_hombres += 1
                elif jugador.sexo == "Mujer":
                    t_mujeres += 1
        return t_hombres, t_mujeres
    def total_ingresos(self):
        total = 0
        for categoria in self.categorias:
            total += categoria.subtotalIngresos()
        return total
    def __str__(self):
        t_hombres, t_mujeres = self.totalHom_Muj()
        return f"Nombre: {self.nombre}\nPropietario: {self.propietario}\nDomicilio: {self.domicilio}\nTotal de Categorias: {self.totalCategorias()} \nTotal de Hombres: {t_hombres} \nTotal de Mujeres: {t_mujeres}\n"


# Captura un jugador y lo agrega a una categoría
def capturaJugador(categoria):
    while True:
        print("Dame los datos del jugador")
        nombre = input("Nombre: ")
        año_nac = int(input("Año de Nacimiento: "))
        sexo = input("Sexo (Hombre/Mujer): ")
        becado = input("¿Está becado? (True/False): ").lower() == "True"
        jugador = Jugador(nombre, año_nac, sexo, becado)
        categoria.obtenerJugador(jugador)
        print(f"Jugador {nombre} agregado a la categoría {categoria.nombre}")

        # Confirmación para agregar otro jugador
        continuar = input("¿Desea agregar otro jugador a esta categoría? (Sí/No): ").lower()
        if continuar != "sí":
            break

# Captura una categoría y la agrega a la academia
def capturaCategoria(academia):
    while True:
        print("Dame los datos de la categoría")
        nombre = input("Nombre de la categoría: ")
        rango = input("Rango de edades (ej. 2006/2007/2008): ")
        costo = float(input("Costo de la categoría: "))
        categoria = Categoria(nombre, rango, costo)
        academia.obtenerCategoria(categoria)
        print(f"Categoría {nombre} agregada a la academia {academia.nombre}")

        # Confirmación para agregar otra categoría
        continuar = input("¿Desea agregar otra categoría? (Sí/No): ").lower()
        if continuar != "sí":
            break

# Agrega un jugador a una categoría específica
def agregarJugadorACategoria(academia, nombre_categoria):
    categoria = next((c for c in academia.categorias if c.nombre == nombre_categoria), None)
    if categoria:
        capturaJugador(categoria)
    else:
        print(f"Categoría {nombre_categoria} no encontrada.")

def main():
    # Importa librería para limpiar la terminal
    import os
    os.system("cls")

    # Crear la academia
    academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")

    # Agregar categorías existentes
    categoria_junior_a = Categoria("Junior A", "2006/2007/2008", 1250)
    categoria_junior_b = Categoria("Junior B", "2009/2010/2011", 850)
    categoria_pony_a   = Categoria("Pony A", "2012/2013/2014", 700)

    # Agregar las categorías predefinidas a la academia
    academia.obtenerCategoria(categoria_junior_a)
    academia.obtenerCategoria(categoria_junior_b)
    academia.obtenerCategoria(categoria_pony_a)

    # Agregar jugadores predefinidos a las categorías
    categoria_junior_a.obtenerJugador(Jugador("Alexander Lopez", 2006, "Hombre", False))
    categoria_junior_a.obtenerJugador(Jugador("Uriel Puga", 2007, "Hombre", True))
    categoria_junior_a.obtenerJugador(Jugador("Alejandra Escalona", 2008, "Mujer", False))

    categoria_junior_b.obtenerJugador(Jugador("Armando Santana", 2009, "Hombre", False))
    categoria_junior_b.obtenerJugador(Jugador("Daniel Mijares", 2010, "Hombre", False))
    categoria_junior_b.obtenerJugador(Jugador("Antonio Hernandez", 2011, "Mujer", True))

    categoria_pony_a.obtenerJugador(Jugador("Andrea Solis", 2012, "Mujer", True))
    categoria_pony_a.obtenerJugador(Jugador("Marissa Hernandez", 2013, "Mujer", True))
    categoria_pony_a.obtenerJugador(Jugador("Diana Soto", 2014, "Mujer", False))

    # Agregar nuevas categorías y jugadores hasta que el usuario decida parar
    capturaCategoria(academia)

    while True:
        nombre_categoria = input("Ingrese el nombre de la categoría a la que desea agregar un jugador (o 'salir' para terminar): ")
        if nombre_categoria.lower() == "salir":
            break
        agregarJugadorACategoria(academia, nombre_categoria)


    print("\nREPORTE DEL CLUB DEPORTIVO\n")
    print(academia)


    print("\n>> Datos generales de las Categorías\n")
    for categoria in academia.categorias:
        print(categoria)

    print("\n>> Jugadores por Categoría:\n")
    for categoria in academia.categorias:
        print(f"\n> {categoria.nombre} - {categoria.rango} - ({categoria.totalJugadores()})")
        for jugador in categoria.jugadores:
            print(jugador)
        subtotal = categoria.subtotalIngresos()
        print(f"- SubTotal : ${subtotal:,.2f}")

    total_ingresos_academia = academia.total_ingresos()
    print(f"\n-> Total : ${total_ingresos_academia:,.2f}")

# Programa principal
if __name__ == '__main__':
    main()
