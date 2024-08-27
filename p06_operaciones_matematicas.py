# p06_operaciones_matematicas - Resuelve Distintas Operaciones Matematicas

# Se define cada una de las variables a emplear
#x = 10.5
#y = 2.5

x= float(input("Dame el primer valor ?"))
y= float(input("Dame el segundo valor ?"))

# se realizan las correspondientes operaciones Matematicas 
suma = x+y
resta = x-y
mult = x*y
div = x/y
res = x % y
exp = x ** y
dive = x // y

# Se presentan los resultados en cada caso
print(f" suma {suma}\n resta {resta}\n multiplicacion {mult}\n division {div:,.4f}")
print(f" residuo {res}\n potencia {exp:,.4f}\n division entera {dive}")
