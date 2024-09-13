# p43_inscripcion_evento - Control de inscripción a un evento académico de la Universidad Patito.

# Importa librería para limpiar la terminal
import os


# Inicializar el total de ventas del día
total_ventas = 0.0

while True:

    # Limpia el texto de la terminal
    os.system("cls")

    # Se da mensaje de inicio
    print("Universidad Patito SA de CV")
    print("Sistema de Inscripción Congreso de Sistemas\n")

    # Se definen variables

    # Tipos de usuario
    Alumno = 100
    Trabajador = 200
    Docente = 500

    # Tipos de paquete
    conferens = 600
    event_social = 800
    kit_acces = 900


    # Preguntas de seleccion
    t_usuario = int(input("Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500 ? "))
    t_paquete = int(input ("Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900 ? "))
    cantidad =  int(input("Cantidad ? :"))

    # Costos
    subtotal = 0
    descuento = 0
    total = 0

    # Se definen las condiciones
    if t_usuario == 1 and t_paquete == 1:
        subtotal = ( Alumno + conferens) * cantidad
        if subtotal > 5000:
            descuento = subtotal * 0.20
        total = subtotal - descuento
        
        print(f"\nTu pedido fue: {cantidad}, Tipo de usuario: Alumno, Tipo de paquete: Solo conferencias")
        print(f"Subtotal: {subtotal} con un descuento de: {descuento:.4f} y un total de {total:.4f}")


    elif t_usuario == 1 and t_paquete == 2:
        subtotal = ( Alumno + event_social) * cantidad
        if subtotal > 5000:
            descuento = subtotal * 0.20
        total = subtotal - descuento

        print(f"\nTu pedido fue: {cantidad}, Tipo de usuario: Alumno, Tipo de paquete: Con eventos sociales")
        print(f"Subtotal: {subtotal} con un descuento de: {descuento:.4f} y un total de {total:.4f}")


    elif t_usuario == 1 and t_paquete == 3:
        subtotal = ( Alumno + kit_acces) * cantidad
        if subtotal > 5000:
            descuento = subtotal * 0.20
        total = subtotal - descuento

        print(f"\nTu pedido fue: {cantidad}, Tipo de usuario: Alumno, Tipo de paquete: Con kit de acceso")
        print(f"Subtotal: {subtotal} con un descuento de: {descuento:.4f} y un total de {total:.4f}")


    elif t_usuario == 2 and t_paquete == 1:
        subtotal = (Trabajador + conferens) * cantidad
        if subtotal > 5000:
            descuento = subtotal * 0.10
        total = subtotal - descuento

        print(f"\nTu pedido fue: {cantidad}, Tipo de usuario: Trabajador, Tipo de paquete: Solo conferencias")
        print(f"Subtotal: {subtotal} con un descuento de: {descuento:.4f} y un total de {total:.4f}")


    elif t_usuario == 2 and t_paquete == 2:
        subtotal = (Trabajador + event_social) * cantidad
        if subtotal > 5000:
            descuento = subtotal * 0.10
        total = subtotal - descuento
        
        print(f"\nTu pedido fue: {cantidad}, Tipo de usuario: Trabajador, Tipo de paquete: Con eventos sociales")
        print(f"Subtotal: {subtotal} con un descuento de: {descuento:.4f} y un total de {total:.4f}")


    elif t_usuario == 2 and t_paquete == 3:
        subtotal = (Trabajador + kit_acces) * cantidad
        if subtotal > 5000:
            descuento = subtotal * 0.10
        total = subtotal - descuento

        print(f"\nTu pedido fue: {cantidad}, Tipo de usuario: Trabajador, Tipo de paquete: Con kit de acceso")
        print(f"Subtotal: {subtotal} con un descuento de: {descuento:.4f} y un total de {total:.4f}")


    elif t_usuario == 3 and t_paquete == 1:
        subtotal = (Docente + conferens) * cantidad
        if subtotal > 5000:
            descuento = subtotal * 0.05
        total = subtotal - descuento

        print(f"\nTu pedido fue: {cantidad}, Tipo de usuario: Docente, Tipo de paquete: Solo conferencias")
        print(f"Subtotal: {subtotal} con un descuento de: {descuento:.4f} y un total de {total:.4f}")


    elif t_usuario == 3 and t_paquete == 2:
        subtotal = (Docente + event_social) * cantidad
        if subtotal > 5000:
            descuento = subtotal * 0.05
        total = subtotal - descuento
        
        print(f"\nTu pedido fue: {cantidad}, Tipo de usuario: Docente, Tipo de paquete: Con eventos sociales")
        print(f"Subtotal: {subtotal} con un descuento de: {descuento:.4f} y un total de {total:.4f}")


    elif t_usuario == 3 and t_paquete == 3:
        subtotal = (Docente + kit_acces) * cantidad
        if subtotal > 5000:
            descuento = subtotal * 0.05
        total = subtotal - descuento
        
        print(f"\nTu pedido fue: {cantidad}, Tipo de usuario: Docente, Tipo de paquete: Con kit de acceso")
        print(f"Subtotal: {subtotal} con un descuento de: {descuento:.4f} y un total de {total:.4f}")

    
    else:
        print("\nEl valor ingresado es incorrecto")
        continue

    # Acumular el total de ventas del día
    total_ventas += total
    
    # Se pregunta al usuario si desea continuar
    if input("¿Deseas continuar (S/N)? ").upper().startswith("N"): break

print(f"\nImporte Total de la Venta: {total_ventas:.4f}")
print("\nProceso terminado ...")