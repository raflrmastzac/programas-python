# p115_calificacion_letra

# Importa librería para limpiar la terminal
import os

# Calificación con letra
def califletra(cal):
    if cal>=90 and cal<100:
        return "A", "Excelente"
    elif cal>=80 and cal<90:
        return "B", "Bien"
    elif cal>=70 and cal<=80:
        return "C", "Suficiente"
    elif cal>=60 and cal<70:
        return "D", "Deficiente"
    elif cal>=0 and cal<60:
        return "F", "Reporbado"

# Principal
# Limpia el texto de la terminal
os.system("cls")

cal = int(input("Calificacion entre 1 y 100 ? "))
letra , mensaje = califletra(cal)
print(f"Tu calificacion de {cal} corresponde a {letra} y esta {mensaje}")