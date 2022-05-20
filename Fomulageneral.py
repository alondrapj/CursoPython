#Bibliotecas
import math

# Variables
a = int(input("Ingresa el valor de a: "))
b = int(input("ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))

#Proceso
x1 = -b -math.sqrt(b*b-(4*a*c))/(2*a)
x2 = -b +math.sqrt(b*b-(4*a*c))/(2*a)

#Salida de datos
print("El resultado de x1 :", x1)
print("El resultado de x2 :", x2)